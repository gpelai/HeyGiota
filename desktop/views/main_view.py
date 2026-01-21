import tkinter as tk


class MainView(tk.Frame):
    def __init__(self, master, on_navigate):
        super().__init__(master)
        master.title('Main')
        self.pack(fill='both', expand=True)

        pages = [('Bills', 'bills'), ('Savings', 'savings')]

        for label, name in pages:
            tk.Button(
                self, text=label, command=lambda n=name: on_navigate(n)
            ).pack()
