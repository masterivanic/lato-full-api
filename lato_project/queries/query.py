from uuid import UUID

from lato import Query


class GetAllTodos(Query): ...


class GetSomeTodos(Query): ...


class GetTodoDetails(Query):
    todo_id: UUID
