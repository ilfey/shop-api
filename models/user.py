from pydantic import PositiveInt, SecretStr

from .ext import ExtBaseModel


class User(ExtBaseModel):
    id: int
    username: str
    password: SecretStr
    products_id: list[PositiveInt]
