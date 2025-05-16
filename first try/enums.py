## in this file, we will try coding with enums!

from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class pokemon(str, Enum):
    charmander = "charmander"
    bulbasaur = "bulbasaur"
    squirtle = "squirtle"


@app.get("/pokemon/{mon_name}")
async def read_name(mon_name: int):
    if mon_name == pokemon.charmander:
        return {"mon_name": mon_name}
    elif mon_name == pokemon.bulbasaur:
        return {"mon_name": mon_name}
    elif mon_name == pokemon.squirtle:
        return {"mon_name": mon_name}
    else:
        return {"mon_name": "not found"}