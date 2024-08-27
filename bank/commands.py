from datetime import datetime
from uuid import UUID
from lato import Command
from typing import Optional


class AddCash(Command):
    """ represent an intent to add money """
    account_id: UUID
    amount:float
    due_at:Optional[datetime] = None

class ReDrawCash(AddCash):
    """ represent an intent to redraw money """
    reason:str = "family assistance"
