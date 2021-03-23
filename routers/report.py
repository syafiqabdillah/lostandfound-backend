from fastapi import APIRouter, HTTPException
from typing import Optional
from pydantic import BaseModel

import services.report as db

name = "report"

router = APIRouter(
    prefix=f"/{name}",
    tags=[name]
)


class FormCreate(BaseModel):
    category: str
    description: str


@router.post('/')
def create(form: FormCreate):
    return db.create(form.category, form.description)

@router.get('/')
def getAll(q: str = ""):
    return db.getAll(q)