from collections.abc import Callable
from datetime import datetime
from typing import Any

from lato import Application
from lato import TransactionContext

from counter import analytics
from counter import TodoCounter
from notification import notification
from notification import NotificationService
from todo import app
from todo import TodoRepository


def create_application() -> Application:
    _app = Application(
        "Lato",
        todo_repository=TodoRepository(),
        notification_service=NotificationService(),
        todos_counter=TodoCounter(),
    )
    _app.include_submodule(app)
    _app.include_submodule(notification)
    _app.include_submodule(analytics)

    @_app.on_enter_transaction_context
    def on_enter_transaction_context(ctx: TransactionContext):
        print("starting transation...")
        ctx.set_dependencies(now=datetime.now())

    @_app.on_exit_transaction_context
    def on_exit_transation_context(ctx: TransactionContext, exception=None):
        print("ending transation...")

    @_app.transaction_middleware
    def logging_middleware(ctx: TransactionContext, call_next: Callable) -> Any:
        handler = ctx.current_handler
        message_name = ctx.get_dependency("message").__class__.__name__
        handler_name = f"{handler.source}.{handler.fn.__name__}"
        print(f"Executing {handler_name}({message_name})")
        result = call_next()
        print(f"Result from {handler_name}: {result}")
        return result

    @_app.transaction_middleware
    def analytics_middleware(ctx: TransactionContext, call_next: Callable) -> Any:
        result = call_next()
        todos_counter = ctx.get_dependency(TodoCounter)
        print(
            f" todos stats: {todos_counter.completed_todos}/{todos_counter.created_todos}"
        )
        return result

    return _app
