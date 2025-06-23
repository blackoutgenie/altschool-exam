import uuid

from app.models import Speaker, Event, Registration, User

users: dict[str, User] = {}
speakers: dict[str, Speaker] = {}
registrations: dict[str, Registration] = {}
events: dict[str, Event] = {}


for name, topic in [
    ("Mr Sagacity", "Future of technology"),
    ("Mr Rotimi", "Learning Python"),
    ("Ms Supanova", "Data Science"),
]:
    
    speaker_id = str(uuid.uuid4())
    speakers[speaker_id] = Speaker(
        id=speaker_id,
        name=name,
        topic=topic
    )