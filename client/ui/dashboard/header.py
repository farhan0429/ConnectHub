import customtkinter as ctk

from themes.manager import ThemeManager


class Header(ctk.CTkFrame):

    HEIGHT = 70

    def __init__(self, master):

        theme = ThemeManager.get()

        super().__init__(
            master,
            height=self.HEIGHT,
            fg_color=theme["surface"],
            corner_radius=0,
        )

        self.pack_propagate(False)

        self.build()

    def build(self):

        left = ctk.CTkFrame(self, fg_color="transparent")
        left.pack(side="left", padx=20)

        ctk.CTkLabel(
            left,
            text="👤 Alice",
            font=("Segoe UI", 18, "bold"),
        ).pack(anchor="w")

        ctk.CTkLabel(
            left,
            text="🟢 Online",
            font=("Segoe UI", 12),
        ).pack(anchor="w")

        right = ctk.CTkFrame(self, fg_color="transparent")
        right.pack(side="right", padx=20)

        ctk.CTkButton(
            right,
            text="📞",
            width=40,
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            right,
            text="⋮",
            width=40,
        ).pack(side="left")