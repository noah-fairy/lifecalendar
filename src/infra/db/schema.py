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
