from dataclasses import dataclass

from marshmallow import EXCLUDE, Schema, post_load
from marshmallow.fields import Str
from marshmallow_enum import EnumField

from source.models import Hash, Size


@dataclass
class OrderRequest:
    first: str
    last: str
    email: str
    phone: str
    size: Size


class OrderRequestSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    first = Str(required=True)
    last = Str(required=True)
    email = Str(required=True)
    phone = Str(required=True)
    size = EnumField(Size, required=True)

    @post_load
    def __post_load__(self, data, **kwargs) -> OrderRequest:
        return OrderRequest(**data)


@dataclass
class OrderResponse:
    succeeded: bool


@dataclass
class HashResponse:
    hashes: list[Hash]
