from fastapi import FastAPI
from pydantic import BaseModel

class Mon(BaseModel):
    name: str
    description: str | None = None
    attack: float
    defense: float | None = None
    speed: float


app = FastAPI()


@app.post("/mons/")
async def create_item(mon: Mon):
    
    mon_dict = mon.model_dump()
    if mon.defense is not None:
        total_defense = mon.attack + mon.defense
        mon_dict.update({"total_defense": total_defense})
    return mon_dict