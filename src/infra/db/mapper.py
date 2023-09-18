from sqlalchemy.orm import registry

from src.domain.entity.calendar import Calendar
from src.infra.db.schema import calendar


def map_between_model_and_schema():
    mapper_registry = registry()
    mapper_registry.map_imperatively(Calendar, calendar)
