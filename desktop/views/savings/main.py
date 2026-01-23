import tkinter as tk
from .create import create_saving


def menu_savings(parent=None):
    root = tk.Toplevel(parent) if parent is not None else tk.Tk()
    root.title('Savings')
    root.resizable(False, False)

    container = tk.Frame(root, padx=24, pady=24)
    container.pack(fill='both', expand=True)

    def on_create():
        create_saving(root)

    create_button = tk.Button(container, text="Create", command=on_create, width=20)
    create_button.pack(pady=12)
    
    root.mainloop()
