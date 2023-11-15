import datetime

from sqlalchemy import Column, Date, DateTime, Integer, MetaData, String, Table, Uuid

metadata = MetaData()

calendar = Table(
    "calendar",
    metadata,
    Column("id", Uuid, primary_key=True),
    Column("user_id", Uuid),
    Column("name", String(100)),
    Column("birthday", Date),
    Column("lifespan", Integer),
    Column("inserted_at", DateTime, default=datetime.datetime.utcnow),
)

calendar_period = Table(
    "calendar_period",
    metadata,
    Column("id", Uuid, primary_key=True),
    Column("calendar_id", Uuid),
    Column("name", String(100)),
    Column("start_year", Integer),
    Column("start_week", Integer),
    Column("end_year", Integer),
    Column("end_week", Integer),
    Column("color", String(30)),
    Column("inserted_at", DateTime, default=datetime.datetime.utcnow),
)

user = Table(
    "user",
    metadata,
    Column("id", Uuid, primary_key=True),
    Column("email", String(500)),
    Column("password", String(500)),
    Column("inserted_at", DateTime, default=datetime.datetime.utcnow),
)

auth_session = Table(
    "auth_session",
    metadata,
    Column("id", Uuid, primary_key=True),
    Column("user_id", Uuid),
    Column("token", String(500)),
    Column("expired_at", DateTime),
    Column("last_accessed_at", DateTime),
    Column("inserted_at", DateTime, default=datetime.datetime.utcnow),
)
