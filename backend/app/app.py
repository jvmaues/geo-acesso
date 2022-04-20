from fastapi import FastAPI, File, UploadFile
import shutil
from typing import Optional, List
from pydantic import BaseModel
import uuid

app = FastAPI()

@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return {"message": "Hey, you are in GEOACESSO API"}

@app.get("/grass/")
async def grass():
    return {"message": "grass function running..."}

@app.post("/namefile/")
async def post_name(name: str):
    return {"name_file":name}

@app.post("/uploadfile/")
async def upload_image(files: List[UploadFile] = File(...)):
    for img in files:
        id = str(uuid.uuid4())
        name_file = id+'-'+img.filename
        with open(f'./uploads/{name_file}', "wb") as buffer:
            shutil.copyfileobj(img.file, buffer)
    
    return {"message":"Uploaded"}
