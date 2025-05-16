from fastapi import FastAPI

app = FastAPI()

mons_db = [{"mon_name": "charmander"}, {"mon_name": "bulbasaur"}, {"mon_name": "squirtle"}]


@app.get("/items/")
async def read_name(skip: int = 0, limit: int = 10):
    return mons_db[skip : skip + limit]