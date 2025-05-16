from fastapi import FastAPI
from enums import read_name

app = FastAPI()

@app.get("/pokemon/{mon_name}")
async def root(mon_name: str):
    return await read_name(mon_name)
