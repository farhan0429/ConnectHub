import customtkinter as ctk

from app.ui_constants import ENTRY_HEIGHT


class PasswordEntry(ctk.CTkFrame):
    """
    Password entry with show/hide functionality.
    """

    def __init__(self, master, placeholder="Password"):

        super().__init__(master, fg_color="transparent")

        self._visible = False

        self.grid_columnconfigure(0, weight=1)

        self.entry = ctk.CTkEntry(
            self,
            placeholder_text=placeholder,
            show="*",
            height=ENTRY_HEIGHT,
            corner_radius=12,
            font=("Segoe UI", 14),
        )

        self.entry.grid(
            row=0,
            column=0,
            sticky="ew",
        )

        self.toggle_button = ctk.CTkButton(
            self,
            text="👁",
            width=45,
            command=self.toggle_password,
        )

        self.toggle_button.grid(
            row=0,
            column=1,
            padx=(8, 0),
        )

    def toggle_password(self):
        self._visible = not self._visible

        self.entry.configure(
            show="" if self._visible else "*"
        )

    def get(self):
        return self.entry.get()

    def clear(self):
        self.entry.delete(0, "end")

    def focus(self):
        self.entry.focus()