# client/services/auth_service.py

from typing import Tuple, Optional
from models.user import User
import time

class AuthService:
    def __init__(self):
        self.current_user: Optional[User] = None

    def authenticate(self, username: str, password: str) -> Tuple[bool, str]:
        """
        Validates credentials. 
        Returns (success_boolean, message_string).
        """
        # TODO: Phase 8 - Replace with real network request to server
        
        # Simulating network delay
        time.sleep(0.5) 

        if not username or not password:
            return False, "Username and password are required."

        # MOCK LOGIN: Accept 'admin' / 'password' for testing UI transitions
        if username == "admin" and password == "password":
            self.current_user = User(
                user_id=1,
                username="admin",
                email="admin@connecthub.local",
                display_name="Administrator",
                auth_token="mock_token_12345"
            )
            return True, "Login successful."
            
        return False, "Invalid username or password."

    def logout(self) -> None:
        """Clears the current session."""
        self.current_user = None
        # TODO: Notify server of logout