import abc
import uuid

from src.domain.entity.auth import User
from src.domain.repo.i_repo import IRepo


class IUserRepo(IRepo[User]):
    @abc.abstractmethod
    def get_by_email(self, email: str) -> User | None:
        ...

    @abc.abstractmethod
    def get_by_email_or_error(self, email: str) -> User:
        ...

    @abc.abstractmethod
    def get_by_session_id(self, session_id: uuid.UUID) -> User | None:
        ...
