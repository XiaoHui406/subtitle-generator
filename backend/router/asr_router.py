from fastapi import APIRouter, UploadFile
from typing import List
import os
import shutil
from model.transcription_segment import TranscriptionSegment
import registry
from model.load_asr_model_request import LoadASRModelRequest


asr_router = APIRouter(
    prefix='/asr',
    tags=['语音识别']
)


@asr_router.post("/load_model")
def load_model(load_request: LoadASRModelRequest) -> str:
    registry.asr_model_manager = registry.asr_model_adapter.get_model_manager(
        model_name=load_request.model_name,
        device=load_request.device
    )
    registry.asr_model_manager.load_model()
    return "load asr model successed"


@asr_router.get('/unload_model')
def unload_model() -> str:
    registry.asr_model_manager.unload_model()
    return "unload asr model successed"


@asr_router.post('/transcribe')
def transcribe(file: UploadFile) -> List[TranscriptionSegment]:
    temp_file = f'temp_{file.filename}'
    with open(temp_file, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    result: List[TranscriptionSegment] = registry.asr_model_manager.transcribe(
        audio=temp_file
    )

    if os.path.exists(temp_file):
        os.remove(temp_file)

    return result
