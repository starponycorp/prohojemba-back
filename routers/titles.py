from typing import Annotated, Optional

from fastapi import APIRouter, Depends, Query, HTTPException

from dto.titles import (
    CreateTitleDTO,
    TitleDTO,
    TitleListDTO
)
from models.enums.state import State
from repositories.titles import TitlesRepository


router = APIRouter(prefix="/titles", tags=["Тайтлы"])


@router.get("/", response_model=TitleListDTO)
async def read_titles(
        titles_repository: Annotated[TitlesRepository, Depends(TitlesRepository)],
        type_id: Optional[int] = None,
        name: Optional[str] = None,
        status: Optional[State] = None,
        page: int = 1
):
    titles = await titles_repository.get_page(
        user_id=1,
        page=page,
        type_id=type_id,
        name=name,
        status=status
    )
    return TitleListDTO(items=[TitleDTO.model_validate(title, from_attributes=True) for title in titles])


@router.get("/{title_id}", response_model=TitleDTO)
async def read_title(
        titles_repository: Annotated[TitlesRepository, Depends(TitlesRepository)],
        title_id: int):
    title = await titles_repository.get_by_id(title_id, user_id=0)
    if not title:
        raise HTTPException(status_code=404, detail=f"Title with id={title_id} not found")

    return TitleDTO.model_validate(title, from_attributes=True)


@router.post("/")
async def create_title(
        titles_repository: Annotated[TitlesRepository, Depends(TitlesRepository)],
        create_title_dto: CreateTitleDTO
):
    pass


@router.patch("/{title_id}")
async def update_title(title_id: int):
    pass


router.delete("/{title_id}")
async def delete_title(title_id: int):
    pass
