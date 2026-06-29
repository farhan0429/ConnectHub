import customtkinter as ctk

from themes.manager import ThemeManager


class MessageBubble(ctk.CTkFrame):
    """
    Single chat message.
    """

    def __init__(
        self,
        master,
        message,
        sender="other",
    ):

        theme = ThemeManager.get()

        bubble_color = (
            theme["primary"]
            if sender == "me"
            else theme["card"]
        )

        anchor = "e" if sender == "me" else "w"

        super().__init__(
            master,
            fg_color="transparent",
        )

        container = ctk.CTkFrame(
            self,
            fg_color=bubble_color,
            corner_radius=16,
        )

        container.pack(
            anchor=anchor,
            padx=15,
            pady=6,
        )

        ctk.CTkLabel(
            container,
            text=message,
            wraplength=400,
            justify="left",
            font=("Segoe UI", 14),
        ).pack(
            padx=14,
            pady=10,
        )