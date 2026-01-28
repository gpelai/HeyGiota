import tkinter as tk

from services.rest.bills_REST_functions import read_all_bills as r_ab


def list_bills(parent=None):
    root = tk.Toplevel(parent)
    root.title('List Bills')
    root.resizable(True, True)

    container = tk.Frame(root, padx=24, pady=24)
    container.pack(fill='both', expand=True)

    items = r_ab()
    if items:
        listbox = tk.Listbox(container, width=50, height=min(10, len(items)))
        listbox.pack(fill='both', expand=True)

        for item in items:
            listbox.insert(tk.END, str(item))

    else:
        empty_label = tk.Label(container, text='No items available')
        empty_label.pack()

    root.mainloop()
