from typing import List, Optional

from pydantic import BaseModel


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
