import abc
import contextlib
from typing import Iterator


class IDBContext(abc.ABC):
    @contextlib.contextmanager
    @abc.abstractmethod
    def begin_tx(self) -> Iterator[None]:
        ...
