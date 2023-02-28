from fastapi import FastAPI
from pydantic import BaseModel, Field

from fastapi.responses import HTMLResponse, JSONResponse

from fastapi.security import HTTPBearer

app = FastAPI()
app.title = "PACTO con FastAPI"
app.version = "0.0.1"


@app.get('/',tags=['home'])

def message():
    return HTMLResponse('<h1>Hello World PACTO</h1>')


@app.get('/info',tags=['info'])

def message():
    return HTMLResponse('<h1>Hello INFO PACTO</h1>')
