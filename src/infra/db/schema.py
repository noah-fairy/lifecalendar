import datetime

from sqlalchemy import Column, Date, DateTime, Integer, MetaData, String, Table, Uuid

metadata = MetaData()

calendar = Table(
    "calendar",
    metadata,
    Column("id", Uuid, primary_key=True),
    Column("name", String(100)),
    Column("birthday", Date),
    Column("lifespan", Integer),
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
    Column("expired_at", DateTime),
    Column("last_accessed_at", DateTime),
    Column("inserted_at", DateTime, default=datetime.datetime.utcnow),
)
