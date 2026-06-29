import customtkinter as ctk

from app.constants import APP_NAME, APP_VERSION


class SplashScreen(ctk.CTkFrame):
    """
    Splash screen displayed during application startup.
    """

    def __init__(self, master, on_complete):
        super().__init__(master)

        self.on_complete = on_complete

        self.pack(fill="both", expand=True)

        self.build_ui()

        self.after(2500, self.finish)

    def build_ui(self):

        container = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        container.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        ctk.CTkLabel(
            container,
            text=APP_NAME,
            font=("Segoe UI", 36, "bold")
        ).pack(pady=(0, 15))

        ctk.CTkLabel(
            container,
            text="Secure Desktop Communication Platform",
            font=("Segoe UI", 16)
        ).pack(pady=(0, 30))

        self.progress = ctk.CTkProgressBar(
            container,
            width=300
        )

        self.progress.pack()

        self.progress.set(0)

        self.animate_progress()

        ctk.CTkLabel(
            container,
            text=f"Version {APP_VERSION}",
            font=("Segoe UI", 12)
        ).pack(pady=(25, 0))

    def animate_progress(self):

        value = self.progress.get()

        if value < 1:
            self.progress.set(value + 0.02)
            self.after(50, self.animate_progress)

    def finish(self):

        self.destroy()

        self.on_complete()