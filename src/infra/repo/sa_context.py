import contextlib
from typing import Iterator

from src.domain.repo.i_db_context import IDBContext
from src.infra.repo.sa import SA


class SAContext(IDBContext):
    def __init__(self, sa: SA) -> None:
        self.sa = sa

    @contextlib.contextmanager
    def begin_tx(self) -> Iterator[None]:
        if self.sa.session.in_transaction():
            yield
        else:
            self.sa.session.begin()

            try:
                yield
                self.sa.session.commit()
            except:
                self.sa.session.rollback()
                raise
            finally:
                self.sa.remove_session()
