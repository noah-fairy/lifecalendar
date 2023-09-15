from __future__ import annotations

import datetime
import uuid


class Calendar:
    id: uuid.UUID
    name: str
    birthday: datetime.date
    lifespan: int
    years: list[Year]


class Year:
    yearnum: int
    weeks: list[Week]


class Week:
    yearnum: int
    weeknum: int