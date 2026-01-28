import tkinter as tk

from .bills.menu_bills import menu_bills


def menu():
    root = tk.Tk()
    root.title('Menu')
    root.geometry('300x100')
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

    root.mainloop()
