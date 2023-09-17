from src.domain.entity.calendar import Calendar
from src.domain.repo.i_repo import IRepo


class ICalendarRepo(IRepo[Calendar]):
    ...
