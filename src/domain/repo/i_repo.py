from __future__ import annotations

import abc
import uuid
from typing import Generic, TypeVar

Entity = TypeVar("Entity")


class IRepo(abc.ABC, Generic[Entity]):
    @abc.abstractmethod
    def get(self, id: uuid.UUID) -> Entity | None:
        ...

    @abc.abstractmethod
    def save(self, entity: Entity) -> None:
        ...

    def get_or_error(self, id: uuid.UUID) -> Entity:
        entity = self.get(id)
        if entity is None:
            raise RepositoryNotFoundError(f"{str(id)}")

        return entity

    def is_exist(self, id: uuid.UUID) -> bool:
        return self.get(id) is not None


class RepositoryError(Exception):
    pass


class RepositoryNotFoundError(RepositoryError):
    pass
