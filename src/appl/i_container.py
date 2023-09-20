from __future__ import annotations

import abc
import inspect
from typing import Any, Type, TypeVar

T = TypeVar("T")


class IContainer(abc.ABC):
    def __init__(self) -> None:
        self.obj_map = {}

    def register(self, obj: Any) -> None:
        self.obj_map[type(obj)] = obj

    def resolve(self, type_: Type[T]) -> T:
        impl_type = type_
        if inspect.isabstract(type_):
            impl_types = type_.__subclasses__()
            if len(impl_types) == 0:
                raise NotRegisteredTypeError(f"type: {type_}")

            impl_type = impl_types[0]

        try:
            obj = self.obj_map[impl_type]
        except KeyError:
            raise NotRegisteredTypeError(f"type: {type_}")

        return obj

    @abc.abstractmethod
    def compose(self) -> None:
        pass


class NotRegisteredTypeError(Exception):
    pass
