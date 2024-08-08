from typing import List
from uuid import UUID

from lato_project.domain.todo import TodoModel


class TodoRepository:
    def __init__(self) -> None:
        self._items = List[TodoModel] = []

    def add(self, item: TodoModel) -> None:
        self._items.append(item)

    def get_by_id(self, item_id: UUID) -> TodoModel:
        for item in self._items:
            if item_id == item.id:
                return item
        raise ValueError(f"Todo with id {item_id} does not exist")

    def get_all(self) -> List[TodoModel]:
        return self._items

    def get_all_completed(self) -> List[TodoModel]:
        return [todo for todo in self._items if todo.is_completed]

    def get_all_not_completed(self) -> List[TodoModel]:
        return [todo for todo in self._items if not todo.is_completed]

    def delete_by_id(self, item_id: UUID) -> None:
        todo = self.get_by_id(item_id=item_id)
        if todo:
            self._items.pop(todo)
