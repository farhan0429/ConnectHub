import customtkinter as ctk

from themes.manager import ThemeManager


class TitleLabel(ctk.CTkLabel):
    """
    Large screen title.
    """

    def __init__(self, master, text):

        theme = ThemeManager.get()

        super().__init__(
            master=master,
            text=text,
            text_color=theme["text"],
            font=("Segoe UI", 30, "bold"),
        )


class HeadingLabel(ctk.CTkLabel):
    """
    Section heading.
    """

    def __init__(self, master, text):

        theme = ThemeManager.get()

        super().__init__(
            master=master,
            text=text,
            text_color=theme["text"],
            font=("Segoe UI", 24, "bold"),
        )


class BodyLabel(ctk.CTkLabel):
    """
    Standard application text.
    """

    def __init__(self, master, text, text_color=None,):

        theme = ThemeManager.get()

        super().__init__(
            master=master,
            text=text,
            text_color=text_color or theme["secondary_text"],
            font=("Segoe UI", 14),
        )


class CaptionLabel(ctk.CTkLabel):
    """
    Small helper text.
    """

    def __init__(self, master, text):

        theme = ThemeManager.get()

        super().__init__(
            master=master,
            text=text,
            text_color=theme["muted_text"],
            font=("Segoe UI", 11),
        )