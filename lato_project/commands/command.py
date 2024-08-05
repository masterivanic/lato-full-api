from datetime import datetime
from lato import Command
from typing import Optional
from uuid import UUID


class CreateTodo(Command):
    todo_id:UUID
    title:str
    description:str=""
    due_at:Optional[datetime] = None

class CompleteTodo(Command):
    todo_id:UUID
