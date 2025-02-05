from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import user_api
from app.db.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

origins = [
    "*"
]

app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

app.include_router(user_api.router)
