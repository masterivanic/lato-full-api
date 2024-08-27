from dataclasses import dataclass
from uuid import UUID
from typing import Optional
from datetime import datetime

@dataclass
class User:
    user_id:UUID
    username:str
    email:str

@dataclass
class Account:
    id: UUID
    user: UUID
    amount:float
    created_date:Optional[datetime] = None
    due_at:Optional[datetime] = None

    @property
    def is_account_negative(self) -> bool:
        return self.amount < 0
    
    def add_cash(self, new_amount:float) -> None:
        self.amount = self.amount + new_amount

    def redraw_cash(self, amount:float) -> None:
        self.amount = self.amount - amount

    
