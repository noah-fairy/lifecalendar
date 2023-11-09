from __future__ import annotations

import datetime
import uuid

import bcrypt


class User:
    id: uuid.UUID
    email: str
    password: str

    session: Session

    def __init__(
        self,
        *,
        id: uuid.UUID,
        email: str,
        password: str,
        session: Session,
    ) -> None:
        self.id = id
        self.email = email
        self.password = self._hash_password(password)
        self.session = session

    @classmethod
    def create(cls, email: str, password: str, password_confirm: str) -> User:
        if password != password_confirm:
            raise ValueError("password and confirm must be same.")

        id = uuid.uuid4()
        user = cls(id=id, email=email, password=password, session=Session.create(id))
        return user

    def authenticate_with_password(self, password: str) -> None:
        if not self._is_password_correct(password):
            raise WrongPasswordError

        self.session.refresh_token()
        self.session.force_extend()

    def authenticate(self) -> None:
        self.session.extend()

    def unauthenticate(self) -> None:
        self.session.expire()

    def _hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode(), salt)
        return hashed.decode()

    def _is_password_correct(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode(), self.password.encode())


class Session:
    id: uuid.UUID
    user_id: uuid.UUID
    token: str
    expired_at: datetime.datetime
    last_accessed_at: datetime.datetime

    def __init__(
        self,
        *,
        id: uuid.UUID,
        user_id: uuid.UUID,
        token: str,
        expired_at: datetime.datetime,
        last_accessed_at: datetime.datetime,
    ) -> None:
        self.id = id
        self.user_id = user_id
        self.token = token
        self.expired_at = expired_at
        self.last_accessed_at = last_accessed_at

    @classmethod
    def create(cls, user_id: uuid.UUID) -> Session:
        now = datetime.datetime.now()
        return cls(id=uuid.uuid4(), user_id=user_id, token=uuid.uuid4().hex, expired_at=now + datetime.timedelta(days=7), last_accessed_at=now)

    def refresh_token(self) -> None:
        self.token  = uuid.uuid4().hex

    def extend(self) -> None:
        if self._is_expired:
            raise ExpiredSessionError

        self._extend()

    def force_extend(self) -> None:
        self._extend()

    def expire(self) -> None:
        if self._is_expired:
            return

        self.expired_at = datetime.datetime.now()

    def _extend(self) -> None:
        now = datetime.datetime.now()
        self.expired_at = now + datetime.timedelta(days=7)
        self.last_accessed_at = now

    @property
    def _is_expired(self) -> bool:
        return self.expired_at < datetime.datetime.now()


class AuthError(Exception):
    pass


class WrongPasswordError(AuthError):
    pass


class ExpiredSessionError(AuthError):
    pass


class InvalidSessionIDError(AuthError):
    pass
