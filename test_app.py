from uuid import UUID
from main import create_application
from lato_project.commands.command import CreateTodo, CompleteTodo
from lato_project.queries.query import GetAllTodos

app = create_application()

app.execute(CreateTodo(todo_id=UUID(int=1), title="Publish the tutorial"))
app.execute(CreateTodo(todo_id=UUID(int=2), title="Play game"))

all_todos = app.execute(GetAllTodos())
print(all_todos, "------ all todos ---------")

app.execute(CompleteTodo(todo_id=UUID(int=1)))
app.execute(CompleteTodo(todo_id=UUID(int=2)))

all_todos = app.execute(GetAllTodos())
print(all_todos, "------ all__todos ---------")