from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn
from router.asr_router import asr_router

app = FastAPI()

app.include_router(asr_router)


@app.get('/')
def to_docs():
    return RedirectResponse(url='/docs')


if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
