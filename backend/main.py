from fastapi import FastAPI
import uvicorn
import whisper
from whisper import Whisper

app = FastAPI()

model: Whisper | None = None


@app.get("/load_asr_model/{model_name}")
def load_asr_model(model_name: str) -> str:
    model = whisper.load_model(model_name)
    return "load asr model successed"


if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
