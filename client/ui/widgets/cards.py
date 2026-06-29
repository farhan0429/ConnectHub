import customtkinter as ctk

from themes.manager import ThemeManager


class GlassCard(ctk.CTkFrame):
    """
    Reusable glass-style card for ConnectHub.

    Used in:
        • Login
        • Register
        • Settings
        • Profile
        • Dialogs
    """

    def __init__(
        self,
        master,
        width=420,
        height=500,
        corner_radius=20,
    ):

        theme = ThemeManager.get()

        super().__init__(
            master=master,

            width=width,
            height=height,

            fg_color=theme["card"],

            corner_radius=corner_radius,

            border_width=1,
            border_color=theme["card_border"],
        )

        # Prevent the frame from shrinking to fit its children.
        self.pack_propagate(False)