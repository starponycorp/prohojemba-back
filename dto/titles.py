from typing import Optional, List

from pydantic import BaseModel, Field

from dto.types import TypeDTO
from models.enums.state import State


class StatusDTO(BaseModel):
    state: State


class CreateTitleDTO(BaseModel):
    name: str = Field(max_length=128)
    cover_url: Optional[str] = None
    type_id: int


class UpdateTitleDTO(CreateTitleDTO):
    name: Optional[str] = Field(None, max_length=128)
    type_id: Optional[int] = None


class TitleDTO(BaseModel):
    id: int
    name: str
    cover_url: Optional[str] = None
    type: Optional[TypeDTO] = None

    user_status: Optional[StatusDTO] = Field(
        None,
        validation_alias="status_for_user"
    )


class TitleListDTO(BaseModel):
    items: List[TitleDTO]
