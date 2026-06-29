import customtkinter as ctk

from ui.base_window import BaseWindow

from ui.widgets.buttons import PrimaryButton
from ui.widgets.entries import TextEntry
from ui.widgets.password_entry import PasswordEntry
from ui.widgets.cards import GlassCard
from ui.widgets.labels import (
    TitleLabel,
    HeadingLabel,
    BodyLabel,
    CaptionLabel,
)


class LoginScreen(BaseWindow):
    """
    Login screen for ConnectHub.
    """

    def __init__(self, master):
        super().__init__(master)

        self.build_ui()
        self.master.bind("<Return>", self.on_enter)

    def on_enter(self, event=None):
        self.login()

    def build_ui(self):
        """Build the complete login screen."""
        self.build_left_panel()
        self.build_right_panel()

    def build_left_panel(self):
        """Create the branding panel."""

        container = ctk.CTkFrame(
            self.left_panel,
            fg_color="transparent"
        )

        container.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        TitleLabel(
            container,
            "ConnectHub",
        ).pack(
            pady=(0, 15)
        )

        BodyLabel(
            container,
            "Secure Desktop\nCommunication Platform",
        ).pack(
            pady=(0, 25)
        )

        CaptionLabel(
            container,
            "Version 0.1.0",
        ).pack()

    def build_right_panel(self):
        """Create the login form."""

        card = GlassCard(
            self.right_panel,
            width=420,
            height=520,
        )

        card.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
        )

        HeadingLabel(
            card,
            "Welcome Back",
        ).pack(
            pady=(35, 25),
        )

        self.username = TextEntry(
            card,
            placeholder="Username",
        )

        self.username.pack(
            padx=40,
            fill="x",
            pady=10,
        )

        self.password = PasswordEntry(card)

        self.password.pack(
            padx=40,
            fill="x",
            pady=10,
        )

        remember = ctk.CTkCheckBox(
            card,
            text="Remember Me",
        )

        remember.pack(
            padx=40,
            anchor="w",
            pady=10,
        )

        PrimaryButton(
            card,
            text="Login",
            command=self.login,
        ).pack(
            padx=40,
            fill="x",
            pady=20,
        )

        ctk.CTkButton(
            card,
            text="Create Account",
            fg_color="transparent",
        ).pack()

        ctk.CTkButton(
            card,
            text="Forgot Password",
            fg_color="transparent",
        ).pack(
            pady=(5, 15)
        )

        BodyLabel(
            card,
            "● Server Offline",
            text_color="orange"
        ).pack()

        CaptionLabel(
            card,
            "v0.1.0",
        ).pack(
            pady=(15, 0)
        )

        self.username.focus()

    def login(self):
        """
        Temporary login handler.
        """

        username = self.username.get()
        password = self.password.get()

        print(username)
        print(password)

        self.master.show_dashboard()