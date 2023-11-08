import uuid

from sqlalchemy import select

from src.domain.entity.calendar import Calendar
from src.domain.repo.i_calendar_repo import ICalendarRepo
from src.domain.repo.i_repo import RepositoryNotFoundError
from src.infra.repo.sa import SA


class SACalendarRepo(ICalendarRepo):
    def __init__(self, sa: SA) -> None:
        self.sa = sa

    def get(self, id: uuid.UUID) -> Calendar | None:
        return self.sa.session.get(Calendar, id)

    def get_by_id_and_user_id(
        self, id: uuid.UUID, user_id: uuid.UUID
    ) -> Calendar | None:
        stmt = select(Calendar).where(Calendar.id == id, Calendar.user_id == user_id)
        return self.sa.session.execute(stmt).scalars().first()

    def get_by_id_and_user_id_or_error(
        self, id: uuid.UUID, user_id: uuid.UUID
    ) -> Calendar:
        cal = self.get_by_id_and_user_id(id, user_id)
        if cal is None:
            raise RepositoryNotFoundError(f"{str(id)}")

        return cal

    def get_all_by_user_id(self, user_id: uuid.UUID) -> list[Calendar]:
        stmt = select(Calendar).where(Calendar.user_id == user_id)
        return list(self.sa.session.execute(stmt).scalars().all())

    def save(self, entity: Calendar) -> None:
        self.sa.session.add(entity)
