from fastapi import FastAPI
from config.user import engine, Base
from fastapi.responses import HTMLResponse, JSONResponse

# CATCH ERROR
from middlewares.error_handler import Errorhandler

# ROUTES
from routers.user import user_router


app = FastAPI()
app.title = "PACTO con FastAPI"
app.version = "0.0.1"

app.add_middleware(Errorhandler)
app.include_router(user_router)


Base.metadata.create_all(bind=engine)

@app.get('/',tags=['home'])
def message():
    return HTMLResponse('<h1>Hello World PACTO</h1>')


@app.get('/info',tags=['info'])
def message():
    return HTMLResponse('<h1>Hello INFO PACTO</h1>')

