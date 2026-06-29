import customtkinter as ctk

from app.constants import (
    APP_NAME,
    APP_VERSION,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    MIN_WIDTH,
    MIN_HEIGHT,
)

from app.logger import logger
from themes.theme import initialize_theme
from themes.manager import ThemeManager

from ui.login import LoginScreen
from ui.splash import SplashScreen
from ui.dashboard.dashboard import DashboardScreen


class ConnectHub(ctk.CTk):
    """
    Main ConnectHub application.
    """

    def __init__(self):
        super().__init__()

        initialize_theme()

        self.title(f"{APP_NAME} {APP_VERSION}")

        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        self.minsize(
            MIN_WIDTH,
            MIN_HEIGHT,
        )

        theme = ThemeManager.get()

        self.configure(
            fg_color=theme["background"]
        )

        self.current_screen = None

        self.show_splash()

        logger.info("Application Started")

    # --------------------------------------------------
    # Screen Manager
    # --------------------------------------------------

    def clear_screen(self):
        """
        Destroy the current screen.
        """

        for widget in self.winfo_children():
            widget.destroy()

    # --------------------------------------------------

    def show_splash(self):
        """
        Display splash screen.
        """

        self.clear_screen()

        SplashScreen(
            self,
            self.show_login,
        )

    # --------------------------------------------------

    def show_login(self):
        """
        Display login screen.
        """

        self.clear_screen()

        self.login_screen = LoginScreen(self)

        self.bind(
            "<Return>",
            self.login_screen.on_enter,
        )

    # --------------------------------------------------

    def show_dashboard(self):
        """
        Display dashboard.
        """

        self.clear_screen()

        self.dashboard = DashboardScreen(self)

        logger.info("Dashboard Opened")