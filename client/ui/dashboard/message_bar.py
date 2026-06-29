# client/ui/dashboard/message_bar.py

import tkinter as tk
# Adjust these imports based on your actual framework (e.g., customtkinter)
# from ui.widgets.entries import PrimaryEntry
# from ui.widgets.buttons import IconButton

class MessageBar(tk.Frame):
    def __init__(self, master, theme_manager, on_send_callback, on_attach_callback, **kwargs):
        super().__init__(master, **kwargs)
        self.theme_manager = theme_manager
        self.on_send_callback = on_send_callback
        self.on_attach_callback = on_attach_callback
        
        # Apply theme colors
        self.theme = self.theme_manager.get_current_theme()
        self.configure(bg=self.theme['background_secondary'], pady=10, padx=15)
        
        self._setup_ui()
        
    def _setup_ui(self):
        # Attachment Button (Left)
        # Replace tk.Button with your custom IconButton if available
        self.attach_btn = tk.Button(
            self, 
            text="📎", # Or use your assets/icons/attachment.png
            command=self.on_attach_callback,
            bg=self.theme['background_secondary'],
            fg=self.theme['text_primary'],
            bd=0,
            cursor="hand2"
        )
        self.attach_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Message Entry (Center, expands to fill space)
        # Replace tk.Entry with your custom PrimaryEntry from widgets/entries.py
        self.message_entry = tk.Entry(
            self,
            bg=self.theme['background_primary'],
            fg=self.theme['text_primary'],
            insertbackground=self.theme['text_primary'], # Cursor color
            font=("Segoe UI", 12),
            bd=0,
            highlightthickness=1,
            highlightbackground=self.theme['border_color']
        )
        self.message_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, ipady=5)
        
        # Bind the Enter key to the send action
        self.message_entry.bind("<Return>", lambda event: self._handle_send())
        
        # Send Button (Right)
        # Replace tk.Button with your custom IconButton
        self.send_btn = tk.Button(
            self,
            text="➤", # Or use your assets/icons/send.png
            command=self._handle_send,
            bg=self.theme['accent_color'],
            fg="white",
            bd=0,
            padx=15,
            cursor="hand2"
        )
        self.send_btn.pack(side=tk.RIGHT, padx=(10, 0))
        
    def _handle_send(self):
        message_text = self.message_entry.get().strip()
        if message_text:
            self.on_send_callback(message_text)
            self.message_entry.delete(0, tk.END) # Clear after sending