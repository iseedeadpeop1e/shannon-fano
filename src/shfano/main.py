from fastapi import FastAPI
import uvicorn

from algorithm import encode

app = FastAPI()


@app.get('/index')
async def index():
    return 'Hello, Web!'


@app.post('/encode')
async def encode_text(text: str):
    return await encode(text)


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
