import uuid

from src.domain.entity.calendar import Calendar
from src.domain.repo.i_calendar_repo import ICalendarRepo
from src.infra.repo.sa import SA


class SACalendarRepo(ICalendarRepo):
    def __init__(self, sa: SA) -> None:
        self.sa = sa

    def get(self, id: uuid.UUID) -> Calendar | None:
        return self.sa.session.get(Calendar, id)

    def save(self, entity: Calendar) -> None:
        self.sa.session.add(entity)
