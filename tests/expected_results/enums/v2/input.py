from enum import Enum
from typing import List, Optional

from pydantic import BaseModel

from .schemas.schema_one import ModelOne  # noqa: F401
from .schemas.schema_two import ModelTwo  # noqa: F401


class Cat(BaseModel):
    name: str
    age: int
    declawed: bool


class Dog(BaseModel):
    name: str
    age: int


class AnimalShelter(BaseModel):
    address: str
    cats: List[Cat]
    dogs: List[Dog]
    owner: Optional[Dog]
    master: Cat


class Standalone(Enum):
    something = "something"
    anything = "anything"
