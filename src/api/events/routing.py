from fastapi import APIRouter,Depends,HTTPException,Query,Body
from .models import *
import os
from api.db.config import DATABASE_URL
from api.db.session import get_session
from sqlmodel import Session,select
router = APIRouter()


@router.get("/", response_model=EventListSchema)
def read_events(session : Session = Depends(get_session)):
    print("Database URL:", os.environ.get("DATABASE_URL"), DATABASE_URL)
    query = select(EventModel).order_by(EventModel.updated_at.desc()).limit(3)
    results = session.exec(query).all()
    print(results)
    return {"results": results,
            "count":len(results)}




@router.post("/",response_model=EventModel)
def create_event(payload:EventCreateSchema,session : Session = Depends(get_session)) -> EventModel:
    # return {
    #     "results" : [
    #         {"id" : 1} ,()
    #         {"id" : 2} , 
    #         {"id" : 3} 
    #     ]
    # }
    data = payload.model_dump()
    obj = EventModel.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj


@router.get("/{event_id}",response_model=EventModel)
def get_event(event_id:int,session : Session = Depends(get_session)) -> EventModel:
    query = select(EventModel).where(EventModel.id == event_id)
    result = session.exec(query).first()
    if not result:
        raise HTTPException(status_code=404, detail="Event not found")
    return result

@router.put("/{event_id}",response_model=EventModel)
def update_event(event_id : int , payload : EventUpdateSchema,session : Session = Depends(get_session)) -> EventModel:
    query = select(EventModel).where(EventModel.id == event_id)
    result = session.exec(query).first()
    if not result:
        raise HTTPException(status_code=404, detail="Event not found")
    data = payload.model_dump()
    for key, value in data.items():
        setattr(result, key, value)
    result.updated_at = get_utc_now()
    session.add(result)
    session.commit()
    session.refresh(result)
    return result


@router.delete("/{event_id}")
def delete_event(event_id: int) -> EventModel:
    return EventModel(id=event_id)
