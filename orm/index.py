from fastapi import FastAPI
from .routes import post, user, auth, vote
from . import models, database
from .config import settings

from fastapi.middleware.cors import CORSMiddleware

# print(settings.database_username)


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins =  origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)


models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def root():
    return {"data": "hello"}



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
