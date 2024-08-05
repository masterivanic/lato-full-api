from uuid import UUID

from lato import Application

from lato_project.commands import command


def test_create_and_complete_todo_scenario(app: Application):
    app.execute(command.CreateTodo(todo_id=UUID(int=1), title="Publish this tutorial"))
    todos = app.execute(GetAllTodos())  # type: ignore
    assert len(todos) == 1

    app.execute(command.CompleteTodo(todo_id=UUID(int=1)))  # type: ignore
    assert len(app.execute(GetSomeTodos(completed=True))) == 1  # type: ignore
    assert len(app.execute(GetSomeTodos(completed=False))) == 0  # type: ignore
