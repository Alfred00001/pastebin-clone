from uuid import uuid4
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
pastes: dict[str, str]={}
@app.get('/')
def home():
    return {'message':'Pastebin Clone is running!'}
class PasteCreate(BaseModel):
    content:str
@app.post("/pastes", status_code=201)
def create_paste(paste:PasteCreate):
    paste_id= str(uuid4())
    pastes[paste_id]=paste.content
    return {'id':paste_id,'content':paste.content}
@app.get('/pastes/{paste_id}')
def get_paste(paste_id:str):
    if paste_id not in pastes:
        raise HTTPException(status_code=404,detail='Paste not found')
    return {'id':paste_id,'content':pastes[paste_id]}

