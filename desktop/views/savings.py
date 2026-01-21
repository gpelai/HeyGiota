from views.base_view import EntryFormView


class SavingsView(EntryFormView):
    def __init__(self, master, on_navigate):
        super().__init__(master, on_navigate, 'Savings')

    def on_submit(self, title, value):
        print(f'Title: {title}\nValue: R${value}')
