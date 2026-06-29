# client/controllers/login_controller.py

class LoginController:
    def __init__(self, login_view, auth_service, on_login_success):
        """
        :param login_view: The instance of your Login UI class
        :param auth_service: The instance of AuthService
        :param on_login_success: Callback function to trigger when login succeeds (e.g., to load dashboard)
        """
        self.view = login_view
        self.auth_service = auth_service
        self.on_login_success = on_login_success

        self._bind_events()

    def _bind_events(self):
        """Connect UI triggers to controller logic."""
        # Assuming your login view has these widgets accessible
        self.view.login_button.configure(command=self.handle_login)
        
        # Bind the Enter key to submit the form
        self.view.password_entry.bind("<Return>", lambda e: self.handle_login())
        self.view.username_entry.bind("<Return>", lambda e: self.handle_login())

    def handle_login(self):
        """Processes the login attempt."""
        # 1. Disable UI during processing to prevent double-clicks
        self._set_ui_state("disabled")
        
        # 2. Get data from UI
        username = self.view.username_entry.get().strip()
        password = self.view.password_entry.get().strip()
        
        # 3. Call Service
        success, message = self.auth_service.authenticate(username, password)
        
        # 4. Handle Result
        if success:
            # Login worked! Trigger the callback to change screens
            self.on_login_success(self.auth_service.current_user)
        else:
            # Login failed. Show error in UI
            self._set_ui_state("normal")
            self.view.show_error(message) # Assumes your view has a show_error method

    def _set_ui_state(self, state: str):
        """Helper to freeze/unfreeze the UI."""
        self.view.login_button.configure(state=state)
        self.view.username_entry.configure(state=state)
        self.view.password_entry.configure(state=state)