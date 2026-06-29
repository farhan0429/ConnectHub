import customtkinter as ctk

from themes.manager import ThemeManager
from ui.dashboard.header import Header
from ui.dashboard.message_bubble import MessageBubble


class Conversation(ctk.CTkFrame):

    def __init__(self, master):

        theme = ThemeManager.get()

        super().__init__(
            master,
            fg_color=theme["background"],
        )

        self.build()

    def build(self):

        header = Header(self)
        header.pack(fill="x")

        messages = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent",
        )

        messages.pack(
            fill="both",
            expand=True,
        )

        MessageBubble(
            messages,
            "Hello!",
            sender="other",
        ).pack(fill="x")

        MessageBubble(
            messages,
            "Hi Alice 👋",
            sender="me",
        ).pack(fill="x")

        MessageBubble(
            messages,
            "Welcome to ConnectHub!",
            sender="other",
        ).pack(fill="x")