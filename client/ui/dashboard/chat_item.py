import customtkinter as ctk

from themes.manager import ThemeManager


class ChatItem(ctk.CTkFrame):
    """
    Single conversation item.
    """

    def __init__(
        self,
        master,
        username,
        last_message,
        time,
        online=False,
    ):

        theme = ThemeManager.get()

        super().__init__(
            master,
            fg_color="transparent",
            corner_radius=10,
            height=72,
        )

        self.pack_propagate(False)

        # Avatar
        avatar = ctk.CTkLabel(
            self,
            text="👤",
            font=("Segoe UI Emoji", 24),
            width=40,
        )

        avatar.pack(
            side="left",
            padx=(10, 8),
        )

        # Text area
        text_frame = ctk.CTkFrame(
            self,
            fg_color="transparent",
        )

        text_frame.pack(
            side="left",
            fill="both",
            expand=True,
        )

        ctk.CTkLabel(
            text_frame,
            text=username,
            font=("Segoe UI", 15, "bold"),
            anchor="w",
        ).pack(anchor="w")

        ctk.CTkLabel(
            text_frame,
            text=last_message,
            font=("Segoe UI", 12),
            text_color=theme["secondary_text"],
            anchor="w",
        ).pack(anchor="w")

        right = ctk.CTkFrame(
            self,
            fg_color="transparent",
        )

        right.pack(
            side="right",
            padx=10,
        )

        ctk.CTkLabel(
            right,
            text=time,
            font=("Segoe UI", 11),
        ).pack()

        status = "🟢" if online else "⚫"

        ctk.CTkLabel(
            right,
            text=status,
            font=("Segoe UI Emoji", 14),
        ).pack(pady=3)