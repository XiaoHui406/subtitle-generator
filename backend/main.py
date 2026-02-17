from fastapi import FastAPI
import uvicorn
from registry import asr_model_manager
from router.asr_router import asr_router

app = FastAPI()

app.include_router(asr_router)


if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
