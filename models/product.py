from pydantic import PositiveInt, PositiveFloat

from .ext import ExtBaseModel


class Product(ExtBaseModel):
    id: PositiveInt
    name: str
    summary: str
    description: str
    price: PositiveFloat
