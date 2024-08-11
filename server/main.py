import os
import random
import string
import time
import json
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

# Create the app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Directories
box_dir = f"../boxes"

# Create a key for the box
async def create_box_key(dir):
    letters = string.ascii_letters
    key_length = 10
    max_attempts = 1000
    random.seed(time.time())
    for attempt in range(1, max_attempts + 1):
        if attempt >= max_attempts:
            break
        key = "".join(random.choice(letters) for _ in range(key_length))
        path = f"../{dir}/{key}.json"
        if not os.path.exists(path):
            return key.lower()
    return ""

@app.get("/")
async def root():
    return {"status": 200}

@app.post("/save")
async def save_box(request: Request):
    req = await request.json()
    _data = {"name": req["name"], "code": req["code"]}
    if not os.path.exists(box_dir):
        os.mkdir(box_dir)
    key = await create_box_key(box_dir)
    file_path = f"../boxes/{key}.json"
    with open(file_path, "w") as file:
        json.dump(_data, file, indent=4)
    return {"key": key}

@app.get("/get/{key}")
async def get_box(key: str):
    file_path = f"../boxes/{key}.json"
    if not os.path.exists(file_path):
        return {"error": "Box not found"}
    with open(file_path, "r") as file:
        data = json.load(file)
    return data
