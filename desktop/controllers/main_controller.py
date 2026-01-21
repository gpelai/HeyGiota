from views.bills import BillsView
from views.main_view import MainView
from views.savings import SavingsView


class MainController:
    def __init__(self, root):
        self.root = root
        self.views = {}
        self.show_main()

    def show_main(self):
        self._switch(MainView(self.root, self.show_view))

    def show_view(self, view_name):
        if view_name == 'main':
            self.show_main()
        elif view_name == 'bills':
            self._switch(BillsView(self.root, self.show_view))
        elif view_name == 'savings':
            self._switch(SavingsView(self.root, self.show_view))

    def _switch(self, view):
        if hasattr(self, 'current_view'):
            self.current_view.destroy()
        self.current_view = view

    def start(self):
        pass
