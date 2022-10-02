from dataclasses import dataclass

from marshmallow import EXCLUDE, Schema, post_load
from marshmallow.fields import String

from source.models import Hash


@dataclass
class OrderRequest:
    item: str
    phone: str


class OrderRequestSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    item = String(required=True)
    phone = String(required=True)

    @post_load
    def __post_load__(self, data, **kwargs) -> OrderRequest:
        return OrderRequest(**data)


@dataclass
class OrderResponse:
    succeeded: bool


@dataclass
class HashResponse:
    hashes: list[tuple[Hash, str]]
