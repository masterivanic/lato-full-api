from uuid import UUID

from lato import Query


class GetAllTodos(Query): ...


class GetSomeTodos(Query):
    completed: bool


class GetTodoDetails(Query):
    todo_id: UUID
