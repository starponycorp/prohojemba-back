from typing import Optional, List

from pydantic import BaseModel, Field


class CreateTypeDTO(BaseModel):
    view_name: str = Field(max_length=32)


class UpdateTypeDTO(BaseModel):
    view_name: Optional[str] = Field(None, max_length=32)


class TypeDTO(CreateTypeDTO):
    id: int


class TypeListDTO(BaseModel):
    items: List[TypeDTO]
