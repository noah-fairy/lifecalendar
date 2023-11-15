from sqlalchemy.orm import registry, relationship

from src.domain.entity.auth import Session, User
from src.domain.entity.calendar import Calendar
from src.domain.entity.calendar.period import Period
from src.infra.db.schema import auth_session, calendar, calendar_period, user


def map_between_model_and_schema():
    mapper_registry = registry()
    mapper_registry.map_imperatively(
        Calendar,
        calendar,
        properties=dict(
            periods=relationship(
                Period,
                foreign_keys=[calendar_period.c.calendar_id],
                primaryjoin=calendar.c.id == calendar_period.c.calendar_id,
            )
        ),
    )
    mapper_registry.map_imperatively(Period, calendar_period)
    mapper_registry.map_imperatively(
        User,
        user,
        properties=dict(
            session=relationship(
                Session,
                uselist=False,
                foreign_keys=[auth_session.c.user_id],
                primaryjoin=user.c.id == auth_session.c.user_id,
            ),
        ),
    )
    mapper_registry.map_imperatively(Session, auth_session)
