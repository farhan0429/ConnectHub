# client/models/user.py

from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    """Represents the currently authenticated user."""
    user_id: int
    username: str
    email: str
    display_name: str
    status: str = "online"
    auth_token: Optional[str] = None
    
    def to_dict(self) -> dict:
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "display_name": self.display_name,
            "status": self.status
        }