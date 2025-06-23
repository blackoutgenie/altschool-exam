from fastapi import FastAPI
from app.router.event import event_router
from app.router.registration import registration_router
from app.router.speaker import speaker_router
from app.router.user import user_router
from app.schemas.event import EventCreate


app = FastAPI()

app.include_router(speaker_router, prefix="/speakers", tags=["speakers"])
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(event_router, prefix="/events", tags=["events"])
app.include_router(registration_router, prefix="/registrations", tags=["registrations"])


@app.get("/")
def home ():
    return {"message": "Welcome to Event management!"}