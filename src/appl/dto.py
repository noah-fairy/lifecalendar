from typing import Self

from pydantic import BaseModel, ConfigDict


class Resp(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def create(cls, obj) -> Self:
        return cls.model_validate(obj)
