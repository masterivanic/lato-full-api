from lato import ApplicationModule

from lato_project.commands.command import CreateTodo
from lato_project.events import TodoWasCompleted


class TodoCounter:
    def __init__(self) -> None:
        self.created_todos: int = 0
        self.completed_todos: int = 0


analytics = ApplicationModule("analytics")


@analytics.handler(CreateTodo)
def handle_create_todo(command: CreateTodo, counter: TodoCounter):
    counter.created_todos += 1


@analytics.handler(TodoWasCompleted)
def handle_completed_todo(event: TodoWasCompleted, counter: TodoCounter):
    counter.created_todos += 1
