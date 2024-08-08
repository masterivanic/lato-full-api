from typing import Annotated
from uuid import UUID
from fastapi import Depends, FastAPI, Request
from lato_project.commands.command import CreateTodo
from main import create_application, Application
from lato_project.queries.query import GetAllTodos

api = FastAPI()
api.lato_application = create_application()

def get_application(request: Request) -> Application:
    app = request.app.lato_application
    app.execute(CreateTodo(todo_id=UUID(int=1), title="Publish the tutorial"))
    app.execute(CreateTodo(todo_id=UUID(int=2), title="Play game"))
    return app

@api.get("/")
def root(app: Annotated[Application, Depends(get_application)]):
    result = app.execute(GetAllTodos())
    return dict(todos=result)