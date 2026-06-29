# client/ui/dashboard/empty_state.py

import tkinter as tk

class EmptyState(tk.Frame):
    def __init__(self, master, theme_manager, **kwargs):
        super().__init__(master, **kwargs)
        self.theme_manager = theme_manager
        self.theme = self.theme_manager.get_current_theme()
        
        self.configure(bg=self.theme['background_primary'])
        
        self._setup_ui()
        
    def _setup_ui(self):
        # Centering container
        self.container = tk.Frame(self, bg=self.theme['background_primary'])
        self.container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Logo/Icon Placeholder
        # You can load assets/logo/connecthub_logo.png here via PhotoImage
        self.icon_label = tk.Label(
            self.container,
            text="💬", # Placeholder for the logo
            font=("Segoe UI", 48),
            bg=self.theme['background_primary'],
            fg=self.theme['text_secondary']
        )
        self.icon_label.pack(pady=(0, 20))
        
        # Main heading
        self.title_label = tk.Label(
            self.container,
            text="ConnectHub",
            font=("Segoe UI", 24, "bold"),
            bg=self.theme['background_primary'],
            fg=self.theme['text_primary']
        )
        self.title_label.pack(pady=(0, 10))
        
        # Subtitle instructions
        self.subtitle_label = tk.Label(
            self.container,
            text="Select a chat from the sidebar to start messaging,\nor create a new conversation.",
            font=("Segoe UI", 12),
            bg=self.theme['background_primary'],
            fg=self.theme['text_secondary'],
            justify=tk.CENTER
        )
        self.subtitle_label.pack()