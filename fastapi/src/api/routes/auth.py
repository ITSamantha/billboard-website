from fastapi import APIRouter, Depends
from src.api.dependencies.router import IsAuthenticated

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/register")
async def read_items():
    return "you registered"


@router.post("/login")
async def read_items():
    return "you logged in"


@router.post("/logout", dependencies=[Depends(IsAuthenticated())])
async def read_items():
    return "you logged out"
