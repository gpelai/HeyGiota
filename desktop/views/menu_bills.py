import tkinter as tk

from services.bills.create import create_bill
from services.bills.delete import delete_bill
from services.bills.list import list_bills
from services.bills.read_one import read_bill
from services.bills.update import update_bill


def menu_bills(parent=None):
    try:
        root = tk.Toplevel(parent) if parent is not None else tk.Tk()
        root.title('Bills')
        root.resizable(False, False)

        container = tk.Frame(root, padx=24, pady=24)
        container.pack(fill='both', expand=True)

        def on_create():
            create_bill(root)

        create_button = tk.Button(
            container, text='Create', command=on_create, width=20
        )
        create_button.pack(pady=12)

        def on_list():
            list_bills(root)

        get_button = tk.Button(
            container, text='List', command=on_list, width=20
        )
        get_button.pack(pady=12)

        def on_read():
            read_bill(root)

        list_button = tk.Button(
            container, text='Search', command=on_read, width=20
        )
        list_button.pack(pady=12)

        def on_update():
            update_bill(root)

        update_button = tk.Button(
            container, text='Update', command=on_update, width=20
        )
        update_button.pack(pady=12)

        def on_delete():
            delete_bill(root)

        delete_button = tk.Button(
            container, text='Delete', command=on_delete, width=20
        )
        delete_button.pack(pady=12)

        root.mainloop()

    except Exception as e:
        print(f'Error - {e}')
