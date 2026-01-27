import tkinter as tk


def read_all_savings(parent=None):
    root = tk.Toplevel(parent)
    root.title('List Savings')
    root.resizable(False, False)

    container = tk.Frame(root, padx=24, pady=24)
    container.pack(fill='both', expand=True)

    items = []
    if items:
        listbox = tk.Listbox(container, width=50, height=min(10, len(items)))
        listbox.pack(fill='both', expand=True)

        for item in items:
            listbox.insert(tk.END, str(item))

    else:
        empty_label = tk.Label(container, text='No items available')
        empty_label.pack()

    root.mainloop()
