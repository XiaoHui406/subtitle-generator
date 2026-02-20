from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn
from router.asr_router import asr_router
from router.output_format_router import output_format_router

app = FastAPI()

app.include_router(asr_router)
app.include_router(output_format_router)


@app.get('/', include_in_schema=False)
def to_docs():
    return RedirectResponse(url='/docs')


if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
