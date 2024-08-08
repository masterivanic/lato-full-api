from dataclasses import dataclass
from uuid import UUID


@dataclass
class TodoReadModel:
    id: UUID
    title: str
    description: str
    is_due: bool
    is_completed: bool
