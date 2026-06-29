import customtkinter as ctk

from themes.manager import ThemeManager
from ui.widgets.sidebar_button import SidebarButton


class Sidebar(ctk.CTkFrame):
    """
    Left navigation panel.
    """

    WIDTH = 220

    def __init__(self, master):

        theme = ThemeManager.get()

        super().__init__(
            master,

            width=self.WIDTH,

            fg_color=theme["sidebar"],

            corner_radius=0,
        )

        self.pack_propagate(False)

        self.build()

    def build(self):

        title = ctk.CTkLabel(
            self,
            text="ConnectHub",
            font=("Segoe UI", 22, "bold"),
        )

        title.pack(
            pady=(30, 40)
        )

        SidebarButton(
            self,
            "💬 Chats",
            selected=True,
        ).pack(
            fill="x",
            padx=15,
            pady=5,
        )

        SidebarButton(
            self,
            "👥 Contacts",
        ).pack(
            fill="x",
            padx=15,
            pady=5,
        )

        SidebarButton(
            self,
            "📁 Files",
        ).pack(
            fill="x",
            padx=15,
            pady=5,
        )

        SidebarButton(
            self,
            "⚙ Settings",
        ).pack(
            fill="x",
            padx=15,
            pady=5,
        )

        ctk.CTkFrame(
            self,
            fg_color="transparent",
        ).pack(
            expand=True,
            fill="both",
        )

        SidebarButton(
            self,
            "🚪 Logout",
        ).pack(
            fill="x",
            padx=15,
            pady=20,
        )