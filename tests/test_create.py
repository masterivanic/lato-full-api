from uuid import UUID

from lato import Application

from lato_project.commands import command
from lato_project.queries import query


def test_create_and_complete_todo_scenario(app: Application):
    app.execute(command.CreateTodo(todo_id=UUID(int=1), title="Publish this tutorial"))
    todos = app.execute(query.GetAllTodos())
    assert len(todos) == 1

    app.execute(command.CompleteTodo(todo_id=UUID(int=1)))
    assert len(app.execute(query.GetSomeTodos(completed=True))) == 1
    assert len(app.execute(query.GetSomeTodos(completed=False))) == 0
