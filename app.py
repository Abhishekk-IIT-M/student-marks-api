from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json

# Load student marks from the JSON file
with open("q-vercel-python.json", "r") as file:
    students = json.load(file)

# Convert to dictionary for quick lookup
marks_dict = {student["name"]: student["marks"] for student in students}

app = FastAPI()

# Enable CORS to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
async def get_marks(name: list[str] = Query(...)):
    """
    API to fetch marks for given student names.
    Example request: /api?name=Alice&name=Bob
    """
    results = [marks_dict.get(n, None) for n in name]  # Get marks for names, return None if not found
    return JSONResponse(content={"marks": results})
