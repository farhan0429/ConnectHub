import customtkinter as ctk

from app.ui_constants import BUTTON_HEIGHT
from themes.manager import ThemeManager


class PrimaryButton(ctk.CTkButton):
    """
    Primary ConnectHub button.
    """

    def __init__(
        self,
        master,
        text,
        command=None,
        width=180,
        state="normal",
    ):

        theme = ThemeManager.get()

        super().__init__(
            master=master,
            text=text,
            command=command,

            width=width,
            height=BUTTON_HEIGHT,

            corner_radius=14,

            fg_color=theme["primary"],
            hover_color=theme["primary_hover"],

            text_color=theme["button_text"],

            border_width=0,

            font=("Segoe UI", 15, "bold"),

            cursor="hand2",

            state=state,
        )


class SecondaryButton(ctk.CTkButton):
    """
    Secondary action button.
    """

    def __init__(
        self,
        master,
        text,
        command=None,
        width=180,
    ):

        theme = ThemeManager.get()

        super().__init__(
            master=master,
            text=text,
            command=command,

            width=width,
            height=BUTTON_HEIGHT,

            corner_radius=14,

            fg_color=theme["secondary"],
            hover_color=theme["secondary_hover"],

            text_color=theme["text"],

            border_width=1,
            border_color=theme["border"],

            font=("Segoe UI", 15),

            cursor="hand2",
        )


class DangerButton(ctk.CTkButton):
    """
    Delete / Logout / Remove button.
    """

    def __init__(
        self,
        master,
        text,
        command=None,
        width=180,
    ):

        theme = ThemeManager.get()

        super().__init__(
            master=master,
            text=text,
            command=command,

            width=width,
            height=BUTTON_HEIGHT,

            corner_radius=14,

            fg_color=theme["error"],
            hover_color="#DC2626",

            text_color="white",

            font=("Segoe UI", 15, "bold"),

            cursor="hand2",
        )