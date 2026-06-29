import customtkinter as ctk

from themes.manager import ThemeManager


class SidebarButton(ctk.CTkButton):
    """
    Navigation button used in the dashboard sidebar.
    """

    def __init__(
        self,
        master,
        text,
        command=None,
        selected=False,
    ):

        theme = ThemeManager.get()

        fg = theme["sidebar_selected"] if selected else "transparent"

        super().__init__(
            master=master,

            text=text,

            command=command,

            fg_color=fg,

            hover_color=theme["sidebar_hover"],

            text_color=theme["text"],

            anchor="w",

            corner_radius=12,

            height=48,

            font=("Segoe UI", 15, "bold"),
        )