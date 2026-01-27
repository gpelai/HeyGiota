import tkinter as tk

from .modules.create import create_saving
from .modules.read_all import read_all_savings
from .modules.read_one import read_saving
from .modules.update import update_saving


def menu_savings(parent=None):
    try:
        root = tk.Toplevel(parent)
        root.title('Savings')
        root.resizable(False, False)

        container = tk.Frame(root, padx=24, pady=24)
        container.pack(fill='both', expand=True)

        def on_create():
            create_saving(root)

        create_button = tk.Button(
            container, text='Create saving', command=on_create, width=20
        )
        create_button.pack(pady=12)

        def on_readAll():
            read_all_savings(root)

        get_button = tk.Button(
            container, text='List savings', command=on_readAll, width=20
        )
        get_button.pack(pady=12)

        def on_read():
            read_saving(root)

        list_button = tk.Button(
            container, text='Saving by id', command=on_read, width=20
        )
        list_button.pack(pady=12)

        def on_update():
            update_saving(root)

        update_button = tk.Button(
            container, text='Update saving', command=on_update, width=20
        )
        update_button.pack(pady=20)

    except Exception as e:
        print(f'Error - {e}')
