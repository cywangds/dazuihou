import base64
import json
from Crypto.Cipher import AES
from binascii import b2a_hex
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Union
import uvicorn as uvicorn
from common import dycode



app = FastAPI()

class People(BaseModel):
    name: str

@app.get('/dyshua')
def index():
    c=dycode.Mydy().dy()
    return c

@app.get('/szwjshua')
def indexsz():
    c=dycode.Mydy().szwj()
    return c

@app.post('/jiemi')
async def shua11(people: People):

    name=people.name
    print(name)
    return {"status":'200'}

@app.get('/szwjshua')
def indexsz():
    c=dycode.Mydy().szwj()
    return c

if __name__ == '__main__':

    uvicorn.run(app=app,
                host="10.0.20.114",
                port=8097,
                workers=1,
                debug=True)