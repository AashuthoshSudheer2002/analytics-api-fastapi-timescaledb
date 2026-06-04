from pydantic import BaseModel
from typing import List

class EventSchema(BaseModel):
    id : int

class EventCreateSchema(BaseModel):
    name : str

class EventUpdateSchema(BaseModel):
    description : str
    
class EventListSchema(BaseModel):
    items: List[EventSchema]