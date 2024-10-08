from typing import Optional

from pydantic import BaseModel

from schemas.level_three import EnumLevelThree


class LevelTwo(BaseModel):
    three: EnumLevelThree
    some: Optional[EnumLevelThree]
    others: list[EnumLevelThree]
