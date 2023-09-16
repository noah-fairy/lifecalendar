from __future__ import annotations

import datetime
import uuid


class Calendar:
    id: uuid.UUID
    name: str
    birthday: datetime.date
    lifespan: int
    years: list[Year]

    def __init__(
        self,
        *,
        id: uuid.UUID,
        name: str,
        birthday: datetime.date,
        lifespan: int,
        years: list[Year],
    ) -> None:
        self.id = id
        self.name = name
        self.birthday = birthday
        self.lifespan = lifespan
        self.years = years

    @classmethod
    def create(cls, name: str, birthday: datetime.date, lifespan: int) -> Calendar:
        return cls(
            id=uuid.uuid4(),
            name=name,
            birthday=birthday,
            lifespan=lifespan,
            years=[
                Year(yearnum=yearnum)
                for yearnum in range(birthday.year, birthday.year + lifespan + 1)
            ],
        )


class Year:
    yearnum: int
    weeks: list[Week]

    def __init__(self, *, yearnum: int) -> None:
        self.yearnum = yearnum
        self.weeks = [
            Week(yearnum=yearnum, weeknum=weeknum) for weeknum in range(1, 53)
        ]


class Week:
    yearnum: int
    weeknum: int

    def __init__(self, *, yearnum: int, weeknum: int) -> None:
        self.yearnum = yearnum
        self.weeknum = weeknum
