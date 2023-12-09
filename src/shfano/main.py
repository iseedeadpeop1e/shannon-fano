from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/index')
async def index():
    return 'Hello, Web!'


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
