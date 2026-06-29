from ui.dashboard.layout import DashboardLayout
from ui.dashboard.sidebar import Sidebar
from ui.dashboard.chat_list import ChatList
from ui.dashboard.conversation import Conversation


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

        self.chat_list = ChatList(self)

        self.chat_list.grid(
            row=0,
            column=1,
            sticky="ns",
        )

        self.conversation = Conversation(self)

        self.conversation.grid(
            row=0,
            column=2,
            sticky="nsew"
        )