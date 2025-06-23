This system allows users to register for events, track attendance, and manage both event information and speaker details

Setup Instructions

clone the repository:

git clone https://github.com/blackoutgenie/second-semester-project.git


Navigate into project directory:

cd project


Create a virtual environment:

python -m venv venv
A
ctivate the virtual environment:
On macOS/Linux:

  source .venv/bin/activate

On Windows use(Powershell):
 venv/Scripts/Activate

Install fastapi pip install "fastapi[standard]"

Access the Application

Open your browser and go to:

http://localhost:8000

You should see the API documentation at:

http://localhost:8000/docs

HOW THE API WORKS
/home
This returns "Message": "Welcome to event management"

Feature

/SPEAKERS
this display all the speakers in the database

/USERS
GET all users: this endpoint get all the users registrated in the database
POST create user: this display the registration endpoint for the user and also generate a unique identity
GET user_id: it access a detail for a specific user without dispalying all the users in database
PUT user_id: this allow to update or correct user detail after registred and it is access with user ID
DELETE user_id: It erase a specific user from the database -PATCH user_id: this endpoint allow user to disactivate their account but will still have access to it by using GET user_id
/ EVENTS
GET all events: this endpoint display all the events that is being registred in the database
POST create events: this create the event and generate a unique identity
GET event_id: it access the details of an event by passing the ID
PUT event_id: This is to update or edit the event registred in the database
DELETE event_id: using this method means it will delete the event in database and won't have access to it
PATCH event_id: this option is to close an event registration for a specfic user
/REGISTRATIONS
GET all registrations: this is to display all the registred details that includes; user_id, event_id, registration_id
POST : its allow a user to be able to register by passing the event_id, user_id and it generate a unique identity
PATCH : this endpoint allows to mark an attendance for those who attended the event
GET registration_id : it get a specific detail by usng the id