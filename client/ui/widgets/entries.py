import customtkinter as ctk

from app.ui_constants import ENTRY_HEIGHT
from themes.manager import ThemeManager


class TextEntry(ctk.CTkEntry):
    """
    Standard text entry used throughout ConnectHub.
    """

    def __init__(
        self,
        master,
        placeholder="",
        width=300,
    ):

        theme = ThemeManager.get()

        super().__init__(
            master=master,

            width=width,
            height=ENTRY_HEIGHT,

            placeholder_text=placeholder,

            corner_radius=14,

            fg_color=theme["input"],

            border_color=theme["input_border"],
            border_width=1,

            text_color=theme["text"],
            placeholder_text_color=theme["placeholder"],

            font=("Segoe UI", 14),
        )


class SearchEntry(TextEntry):
    """
    Entry used for searching users/chats.
    """

    def __init__(
        self,
        master,
        placeholder="Search...",
        width=300,
    ):

        super().__init__(
            master,
            placeholder=placeholder,
            width=width,
        )


class MessageEntry(TextEntry):
    """
    Entry used for sending chat messages.
    """

    def __init__(
        self,
        master,
        width=500,
    ):

        super().__init__(
            master,
            placeholder="Type a message...",
            width=width,
        )