from lato_project.events import TodoWasCompleted
from lato_project.queries.query import GetTodoDetails
from lato_project.domain.todo_read import TodoReadModel
from lato import ApplicationModule
from lato import TransactionContext
from datetime import datetime

notification = ApplicationModule("notification")

class NotificationService:
    def push(self, message):
        print(f"Receied at {datetime.now()} {message}")

@notification.handler(TodoWasCompleted)
def on_todo_completed(event:TodoWasCompleted, service:NotificationService, ctx:TransactionContext):
    details:TodoReadModel = ctx.execute(GetTodoDetails(todo_id=event.todo_id)) # the query is dispatched using TransactionContext
    message = f"A tdo {details.title} was completed"
    service.push(message=message)