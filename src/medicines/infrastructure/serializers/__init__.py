from typing import List

from pydantic import BaseModel, Field, ValidationError


class Test2(BaseModel):
    # Field allows you to add descriptions and validation logic
    name: str = Field(..., min_length=1)

class Test(BaseModel):
    # This validates that the root of your JSON is a list under a specific key
    data: List[Test2]