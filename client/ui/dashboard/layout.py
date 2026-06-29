import customtkinter as ctk

from themes.manager import ThemeManager


class DashboardLayout(ctk.CTkFrame):
    """
    Main dashboard layout.

    This frame contains:
        - Sidebar
        - Chat List
        - Conversation
        - Message Bar
    """

    def __init__(self, master):

        theme = ThemeManager.get()

        super().__init__(
            master,
            fg_color=theme["background"],
        )

        self.pack(fill="both", expand=True)

        # Configure grid
        self.grid_columnconfigure(0, weight=0)  # Sidebar
        self.grid_columnconfigure(1, weight=1)  # Chat List
        self.grid_columnconfigure(2, weight=3)  # Conversation

        self.grid_rowconfigure(0, weight=1)