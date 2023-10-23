from pydantic import BaseModel

import models
import yaml


class ExtBaseModel(BaseModel):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._storage = []

    @classmethod
    def save_list(cls, L: list[dict]):
        cls._storage = list(map(lambda x: cls(**x), L))

    @classmethod
    def get_by_id(cls, id: int):
        return filter(lambda x: x.id == id, cls._storage)

    @classmethod
    def get_by_id(cls, id: int):
        for item in cls._storage:
            if item.id == id:
                return item

    @classmethod
    def get_all(cls) -> list:
        return cls._storage


def load_data(path = "data.yml"):
    with open(path, "r") as f:
        data = yaml.safe_load(f)

        if "products" in data:
            models.Product.save_list(data["products"])

        if "users" in data:
            models.User.save_list(data["users"])
