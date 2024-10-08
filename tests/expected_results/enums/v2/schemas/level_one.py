from pydantic import BaseModel

from schemas.level_two import LevelTwo


class LevelOne(BaseModel):
    two: LevelTwo
