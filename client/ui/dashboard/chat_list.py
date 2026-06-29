import customtkinter as ctk

from themes.manager import ThemeManager
from ui.dashboard.chat_item import ChatItem


class ChatList(ctk.CTkFrame):

    WIDTH = 380

    def __init__(self, master):

        theme = ThemeManager.get()

        super().__init__(
            master,
            width=self.WIDTH,
            fg_color=theme["surface"],
            corner_radius=0,
        )

        self.pack_propagate(False)

        self.build()

    def build(self):

        title = ctk.CTkLabel(
            self,
            text="Chats",
            font=("Segoe UI", 22, "bold"),
        )

        title.pack(
            anchor="w",
            padx=20,
            pady=(25, 15),
        )

        search = ctk.CTkEntry(
            self,
            placeholder_text="Search chats...",
        )

        search.pack(
            fill="x",
            padx=15,
            pady=(0, 15),
        )

        scroll = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent",
        )

        scroll.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=5,
        )

        ChatItem(
            scroll,
            "Alice",
            "See you tomorrow!",
            "10:30",
            True,
        ).pack(fill="x", pady=4)

        ChatItem(
            scroll,
            "Bob",
            "Let's meet.",
            "Yesterday",
            False,
        ).pack(fill="x", pady=4)

        ChatItem(
            scroll,
            "Charlie",
            "Project completed.",
            "Mon",
            True,
        ).pack(fill="x", pady=4)