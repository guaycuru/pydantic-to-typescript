import os
import sys
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel

# Make absolute imports work
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

from .schemas.schema_one import ModelOne  # noqa: F401
from .schemas.schema_two import ModelTwo  # noqa: F401
from schemas.sub_model import (
    SubModel,
)  # this tests absolute imports


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


class ImportedSubModule(BaseModel):
    sub: SubModel
