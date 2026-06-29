from ui.dashboard.layout import DashboardLayout
from ui.dashboard.sidebar import Sidebar


class DashboardScreen(DashboardLayout):
    """
    Main application dashboard.
    """

    def __init__(self, master):

        super().__init__(master)

        self.build()

    def build(self):

        self.sidebar = Sidebar(self)

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns",
        )