import tkinter as tk
from .modules.create import create_bill
from .modules.read_all import read_all_bills
from .modules.read_one import read_bill
from .modules.update import update_bill


def menu_bills(parent=None):
    try:
        root = tk.Toplevel(parent) if parent is not None else tk.Tk()
        root.title('Bills')
        root.resizable(False, False)

        container = tk.Frame(root, padx=24, pady=24)
        container.pack(fill='both', expand=True)

        def on_create():
            create_bill(root)
        create_button = tk.Button(container, text="Create", command=on_create, width=20)
        create_button.pack(pady=12)

        def on_readAll():
            read_all_bills(root)
        get_button = tk.Button(container, text="List bills", command=on_readAll, width=20)
        get_button.pack(pady=12)

        def on_read():
            read_bill(root)
        list_button = tk.Button(container, text="Bill by id", command=on_read, width=20)
        list_button.pack(pady=12)

        def on_update():
            update_bill(root)
        update_button = tk.Button(container, text="Update bill", command=on_update, width=20)
        update_button.pack(pady=20)


        
        root.mainloop()

    except Exception as e:
        print(f"Error - {e}")
