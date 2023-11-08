import abc
import uuid

from src.domain.entity.calendar import Calendar
from src.domain.repo.i_repo import IRepo


class ICalendarRepo(IRepo[Calendar]):
    @abc.abstractmethod
    def get_by_id_and_user_id(
        self, id: uuid.UUID, user_id: uuid.UUID
    ) -> Calendar | None:
        ...

    @abc.abstractmethod
    def get_by_id_and_user_id_or_error(
        self, id: uuid.UUID, user_id: uuid.UUID
    ) -> Calendar:
        ...

    @abc.abstractmethod
    def get_all_by_user_id(self, user_id: uuid.UUID) -> list[Calendar]:
        ...
