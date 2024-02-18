import uvicorn
from fastapi import FastAPI

from source.history_api import router as history_router
from source.prompt_api import router as prompt_router

app = FastAPI()


# Mount router sapp
@app.get("/")
async def Home():
    return {"Model ": "TasksLLMMOdel",
            "version": "1.0"}


app.include_router(history_router, prefix="/history")

app.include_router(prompt_router, prefix="/prompt")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
