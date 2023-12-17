from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from algorithm import encode

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/index')
async def index():
    return 'Hello, Web!'


@app.post('/encode')
async def encode_text(text: str):
    return await encode(text)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
