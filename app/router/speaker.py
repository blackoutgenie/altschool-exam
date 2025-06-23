from fastapi import APIRouter
from app.database import speakers

speaker_router = APIRouter()

@speaker_router.get("/",)
def list_speakers():

    return {
        speaker_id: {
            "id": speakers.id,
            "name": speakers.name,
            "topic": speaker.topic
       }
       for speaker_id, speaker in speakers.items()
    }