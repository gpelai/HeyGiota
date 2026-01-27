import tkinter as tk

from .bills.menu_bills import menu_bills
from .savings.menu_savings import menu_savings


def menu():
    root = tk.Tk()
    root.title('Menu')
    root.geometry('300x150')
    root.resizable(False, False)

    container = tk.Frame(root, padx=24, pady=24)
    container.pack(fill='both', expand=True)

    # bills
    def on_bills():
        menu_bills(root)

    bills_button = tk.Button(
        container, text='Bills', command=on_bills, width=10
    )
    bills_button.pack(pady=12)

    # savings
    def on_savings():
        menu_savings(root)

    savings_button = tk.Button(
        container, text='Savings', command=on_savings, width=10
    )
    savings_button.pack(pady=12)

    root.mainloop()
