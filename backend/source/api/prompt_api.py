from fastapi import APIRouter

router = APIRouter(prefix="/prompt")


@router.post("/prompt/{task_number}")
async def post_prompt_by_task (task_number: int):
    return {"message": " Response"}


@router.get("/prompt/{prompt_id}")
async def get_prompt(prompt_id: str):
    return {"message": " Response"}


@router.put("/prompt/{prompt_id}")
async def update_prompt(prompt_id: str):
    return {"message": " Response"}
# Add other LLM model-related endpoints