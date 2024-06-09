from fastapi import FastAPI
import logging

logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
async def root():
    logger.info(f"request / endpoint!")
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
