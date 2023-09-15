import datetime
import uuid


class Calendar:
    id: uuid.UUID
    name: str
    birthday: datetime.date
    lifespan: int