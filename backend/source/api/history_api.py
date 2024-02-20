from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_history():
    return {"message": "Get all history routers"}

@router.get("/{id}")
async def read_history_item(id:int):
    return {"message": f"Get history with id  {id}"}

@router.delete("/{id}")
async def delete_history_item(id:int):
    return {"message": f"Deleted history with id  {id}"}

@router.delete("/")
async def delete_history_item():
    return {"message": f"Deleted  all histories"}


#Adding anothers history-related endpoints

