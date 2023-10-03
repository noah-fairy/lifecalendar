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
            impl_type = None
            for t, o in self.obj_map.items():
                if isinstance(o, type_):
                    impl_type = t
                    break  # just use first implementation

            if impl_type is None:
                raise NotRegisteredTypeError(f"type: {type_}")

        try:
            obj = self.obj_map[impl_type]
        except KeyError:
            raise NotRegisteredTypeError(f"type: {type_}")

        return obj

    @abc.abstractmethod
    def compose_by_env(self) -> None:
        ...

    @abc.abstractmethod
    def compose(self) -> None:
        ...


class NotRegisteredTypeError(Exception):
    pass
