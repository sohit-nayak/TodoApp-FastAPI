from fastapi import FastAPI
from starlette import status

from .routers import auth, todos, admin, users
from .database import engine
from .models import Base
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()

Base.metadata.create_all(bind=engine)


app.mount("/static", StaticFiles(directory="TodoApp/static"), name="static")

@app.get("/")
def test(request: Request):
    return RedirectResponse("/todos/todo-page", status_code=status.HTTP_302_FOUND)

@app.get("/healthy", status_code=status.HTTP_200_OK)
def healthcheck():
    return {"status": "ok"}


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)

