from datetime import datetime
from typing import Optional
from uuid import UUID

from lato import Command


class CreateTodo(Command):
    todo_id: UUID
    title: str
    description: str = ""
    due_at: Optional[datetime] = None


class CompleteTodo(Command):
    todo_id: UUID
