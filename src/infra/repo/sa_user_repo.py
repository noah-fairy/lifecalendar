import uuid

from sqlalchemy import select

from src.domain.entity.auth import Session, User
from src.domain.repo.i_repo import RepositoryNotFoundError
from src.domain.repo.i_user_repo import IUserRepo
from src.infra.repo.sa import SA


class SAUserRepo(IUserRepo):
    def __init__(self, sa: SA) -> None:
        self.sa = sa

    def get(self, id: uuid.UUID) -> User | None:
        return self.sa.session.get(User, id)

    def save(self, entity: User) -> None:
        self.sa.session.add(entity)

    def get_by_email(self, email: str) -> User | None:
        stmt = select(User).where(User.email == email).limit(1)
        return self.sa.session.execute(stmt).scalars().first()

    def get_by_email_or_error(self, email: str) -> User:
        user = self.get_by_email(email)
        if user is None:
            raise RepositoryNotFoundError
        return user

    def get_by_token(self, token: str) -> User | None:
        stmt = select(User).join(User.session).where(Session.token == token).limit(1)
        return self.sa.session.execute(stmt).scalars().first()
