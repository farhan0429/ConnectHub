import customtkinter as ctk

from themes.manager import ThemeManager


class NavigationButton(ctk.CTkButton):
    """
    Sidebar navigation button.
    """

    def __init__(
        self,
        master,
        text,
        command=None,
    ):

        theme = ThemeManager.get()

        super().__init__(
            master=master,
            text=text,
            command=command,

            fg_color="transparent",
            hover_color=theme["sidebar_hover"],

            text_color=theme["text"],

            anchor="w",

            height=44,

            corner_radius=10,

            font=("Segoe UI", 15),
        )