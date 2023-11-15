from __future__ import annotations

import uuid


class Period:
    id: uuid.UUID
    calendar_id: uuid.UUID
    name: str
    start_year: int
    start_week: int
    end_year: int
    end_week: int
    color: str

    def __init__(
        self,
        *,
        id: uuid.UUID,
        name: str,
        start_year: int,
        start_week: int,
        end_year: int,
        end_week: int,
        color: str,
    ) -> None:
        self.id = id
        self.name = name
        self.start_year = start_year
        self.start_week = start_week
        self.end_year = end_year
        self.end_week = end_week
        self.color = color

    @classmethod
    def create(
        cls,
        name: str,
        start_year: int,
        start_week: int,
        end_year: int,
        end_week: int,
        color: str,
    ) -> Period:
        return cls(
            id=uuid.uuid4(),
            name=name,
            start_year=start_year,
            start_week=start_week,
            end_year=end_year,
            end_week=end_week,
            color=color,
        )
