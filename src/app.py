"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
git revert HEAD
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Drama Club": {
        "description": "Perform in school plays and musicals",
        "participants": []
    },
    "Debate Team": {
        "description": "Compete in debate competitions",
        "participants": []
    },
    "Science Club": {
        "description": "Explore scientific experiments and projects",
        "participants": []
    },
    "Chess Club": {
        "description": "Play and learn chess strategy",
        "participants": []
    },
    "Basketball Team": {
        "description": "Join the school basketball team and compete",
        "participants": []
    },
    "Soccer Team": {
        "description": "Play competitive soccer matches",
        "participants": []
    },
    "Art Studio": {
        "description": "Create paintings, sculptures, and digital art",
        "participants": []
    },
    "Music Band": {
        "description": "Practice and perform in the school band",
        "participants": []
    },
    "Robotics Club": {
        "description": "Build and program robots for competitions",
        "participants": []
    },
    "Math Olympiad": {
        "description": "Solve challenging math problems and compete",
        "participants": []
    }
}

@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Validate student is not already signed up    if email in activity["participants"]:
    raise HTTPException(status_code=400, detail="Student already signed up for this activity")

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
