from sqlalchemy import create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker


class SA:
    def __init__(self, url: str, options: dict) -> None:
        self.engine = create_engine(url, **options)
        self.session_factory = sessionmaker(bind=self.engine, expire_on_commit=False)
        self.scoped_session_factory = scoped_session(self.session_factory)

    @property
    def session(self) -> Session:
        return self.scoped_session_factory()

    def remove_session(self) -> None:
        self.scoped_session_factory.remove()
