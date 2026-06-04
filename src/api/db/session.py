import sqlmodel
from sqlmodel import SQLModel , Field , Session
import timescaledb
from api.db.config import DATABASE_URL,DB_TIMEZONE

if DATABASE_URL == "":
    raise NotImplementedError("DATABASE_URL is not set in environment variables")

engine = timescaledb.create_engine(DATABASE_URL,timezone=DB_TIMEZONE)

def init_db():
    # print("Initializing databases...")
    # SQLModel.metadata.create_all(engine)
    print("Creating Hypertables...")
    timescaledb.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session