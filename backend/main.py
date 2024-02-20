from fastapi import FastAPI

from source.api.history_api import router as history_router
from source.api.prompt_api import router as prompt_router
from config.settings import Appconfig

config = Appconfig()
app = FastAPI(title=config.app_name)


# Mount router sapp
@app.get("/")
async def home():
    return {"Model ": "TasksLLMMOdel",
            "version": "1.0"}


app.include_router(history_router, prefix="/history")

app.include_router(prompt_router, prefix="/prompt")

#another method to run uvicorn server
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=5000)
