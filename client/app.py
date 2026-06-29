import customtkinter as ctk

from config import *

from themes.theme import load_theme


class ConnectHub(ctk.CTk):

    def __init__(self):
        super().__init__()

        load_theme()

        self.title(f"{APP_NAME} {VERSION}")

        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        self.minsize(MIN_WIDTH, MIN_HEIGHT)

        self.configure(fg_color=BACKGROUND)