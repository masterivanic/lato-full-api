from uuid import UUID

from lato_project.commands.command import CompleteTodo
from lato_project.commands.command import CreateTodo
from lato_project.queries.query import GetAllTodos
from main import create_application

app = create_application()

app.execute(CreateTodo(todo_id=UUID(int=1), title="Publish the tutorial"))
app.execute(CreateTodo(todo_id=UUID(int=2), title="Play game"))

all_todos = app.execute(GetAllTodos())
print(all_todos, "------ all todos ---------")

app.execute(CompleteTodo(todo_id=UUID(int=1)))
app.execute(CompleteTodo(todo_id=UUID(int=2)))

all_todos = app.execute(GetAllTodos())
print(all_todos, "------ all__todos ---------")
