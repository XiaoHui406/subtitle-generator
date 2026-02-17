from fastapi import FastAPI, UploadFile
import uvicorn
import shutil
import os
from typing import List
from registry import asr_model_manager
from model.transcription_segment import TranscriptionSegment
from router.asr_router import asr_router

app = FastAPI()

app.include_router(asr_router)


if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
