from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/")
async def get_users():
    return {"message": "all users"}


@router.get("/{user_id}")
async def get_user(user_id:str):
    return {"message": "user id is {user_id}"}


@router.post("/")
async def create_user(request: Request):
    return {"message": request.get()}
