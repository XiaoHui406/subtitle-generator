from fastapi import APIRouter, UploadFile
from typing import List
import os
import shutil
from model.transcription_segment import TranscriptionSegment
from registry import asr_model_manager


asr_router = APIRouter(
    prefix='/asr',
    tags=['asr']
)


@asr_router.get("/load_asr_model")
def load_model(model_name: str, model_size: str) -> str:
    asr_model_manager.load_model()
    return "load asr model successed"


@asr_router.post('/transcribe/{output_format}')
def transcribe(file: UploadFile, output_format: str) -> List[TranscriptionSegment]:
    temp_file = f'audio/temp_{file.filename}'
    with open(temp_file, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    result: List[TranscriptionSegment] = asr_model_manager.transcribe(
        audio=temp_file,
        output_format=output_format
    )

    if os.path.exists(temp_file):
        os.remove(temp_file)

    return result
