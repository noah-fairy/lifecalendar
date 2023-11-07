import uuid

import pytest

from src.domain.entity.auth import (
    ExpiredSessionError,
    Session,
    User,
    WrongPasswordError,
)


class TestUser:
    def test_create(self):
        email = "asdf@gmail.com"
        password = "asdf"
        password_confirm = "asdf"

        user = User.create(
            email=email, password=password, password_confirm=password_confirm
        )

        assert user.email == email
        assert user._is_password_correct(password)
        assert user.session is not None

    def test_create_fail_when_invalid_password_confirm(self):
        email = "asdf@gmail.com"
        password = "asdf"
        password_confirm = "not asdf"

        with pytest.raises(ValueError):
            User.create(
                email=email, password=password, password_confirm=password_confirm
            )

    def test_authenticate_with_password(self):
        email = "asdf@gmail.com"
        password = "asdf"
        password_confirm = "asdf"
        user = User.create(
            email=email, password=password, password_confirm=password_confirm
        )
        expired_at_before_auth = user.session.expired_at
        last_accessed_at_before_auth = user.session.last_accessed_at

        user.authenticate_with_password(password)

        assert user.session is not None
        assert user.session.expired_at > expired_at_before_auth
        assert user.session.last_accessed_at > last_accessed_at_before_auth

    def test_authenticate_with_password_fail_when_wrong_password(self):
        email = "asdf@gmail.com"
        password = "asdf"
        password_confirm = "asdf"
        user = User.create(
            email=email, password=password, password_confirm=password_confirm
        )

        with pytest.raises(WrongPasswordError):
            user.authenticate_with_password("wrong password")


class TestSession:
    def test_extend(self):
        session = Session.create(uuid.uuid4())
        expired_at_before_extend = session.expired_at
        last_accessed_at_before_extend = session.last_accessed_at

        session.extend()

        assert session.expired_at > expired_at_before_extend
        assert session.last_accessed_at > last_accessed_at_before_extend

    def test_extend_fail_when_already_expired(self):
        session = Session.create(uuid.uuid4())
        session.expire()

        with pytest.raises(ExpiredSessionError):
            session.extend()

    def test_expired(self):
        session = Session.create(uuid.uuid4())

        session.expire()

        assert session._is_expired
