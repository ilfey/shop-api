from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import routers
from models import ext as models_ext

# load data from data.yml
models_ext.load_data("data.yml")

origins = [
    "http://localhost",
    "http://127.0.0.1",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# include routers
for router in routers:
    app.include_router(router)
