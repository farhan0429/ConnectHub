import customtkinter as ctk


class BaseWindow(ctk.CTkFrame):
    """
    Base layout used by all screens.
    """

    def __init__(self, master):
        super().__init__(master)

        self.pack(fill="both", expand=True)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)

        self.left_panel = ctk.CTkFrame(
            self,
            corner_radius=0
        )

        self.left_panel.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.right_panel = ctk.CTkFrame(
            self,
            corner_radius=0
        )

        self.right_panel.grid(
            row=0,
            column=1,
            sticky="nsew"
        )