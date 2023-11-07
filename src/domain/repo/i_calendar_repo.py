import abc
import uuid

from src.domain.entity.calendar import Calendar
from src.domain.repo.i_repo import IRepo


class ICalendarRepo(IRepo[Calendar]):
    @abc.abstractmethod
    def get_all_by_user_id(self, user_id: uuid.UUID) -> list[Calendar]:
        ...
