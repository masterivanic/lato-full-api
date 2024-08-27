from datetime import datetime
from typing import List

from lato import Application
from lato import TransactionContext

from lato_project.commands.command import CompleteTodo
from lato_project.commands.command import CreateTodo
from lato_project.domain.todo import TodoModel
from lato_project.domain.todo_read import TodoReadModel
from lato_project.events import TodoWasCompleted
from lato_project.queries.query import GetAllTodos
from lato_project.queries.query import GetSomeTodos
from lato_project.queries.query import GetTodoDetails
from lato_project.repositories.todo_repo import TodoRepository


app = Application(name="todos")


def todo_model_to_read_model(todo: TodoModel, now: datetime) -> TodoReadModel:
    return TodoReadModel(
        id=todo.id,
        title=todo.title,
        description=todo.description,
        is_due=todo.is_due(now),
        is_completed=todo.is_completed,
    )


@app.handler(CreateTodo)
def handler_create_todo(command: CreateTodo, repo: TodoRepository):
    new_todo = TodoModel(
        id=command.todo_id,
        title=command.title,
        description=command.description,
        due_at=command.due_at,
    )
    repo.add(new_todo)


@app.handler(CompleteTodo)
def handler_complete_todo(
    command: CompleteTodo, repo: TodoRepository, ctx: TransactionContext, now: datetime
):
    a_todo = repo.get_by_id(command.todo_id)
    a_todo.mark_as_completed(when=now)
    ctx.publish(TodoWasCompleted(todo_id=a_todo.id))  # publish event


@app.handler(GetAllTodos)
def get_all_todos(
    query: GetAllTodos, repo: TodoRepository, now: datetime
) -> List[TodoModel]:
    result = repo.get_all()
    return [todo_model_to_read_model(todo, now) for todo in result]


@app.handler(GetSomeTodos)
def get_some_todos(query: GetSomeTodos, repo: TodoRepository, now: datetime):
    if query.completed is None:
        result = repo.get_all()
    else:
        result = (
            repo.get_all_completed()
            if query.completed
            else repo.get_all_not_completed()
        )

    return [todo_model_to_read_model(todo, now) for todo in result]


@app.handler(GetTodoDetails)
def get_todo_details(query: GetTodoDetails, repo: TodoRepository) -> TodoModel:
    todo_details = repo.get_by_id(item_id=query.todo_id)
    return todo_details
