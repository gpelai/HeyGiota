import tkinter as tk
from controllers.bills_REST_functions import create_bill as cb


def create_bill(parent=None):
    root = tk.Toplevel(parent)
    root.title('Create Bill')
    root.resizable(False, False)

    container = tk.Frame(root, padx=24, pady=24)
    container.pack(fill='both', expand=True)

    fields = [
        ("Title", tk.StringVar()),
        ("Amount", tk.StringVar()),
    ]

    for index, (label_text, var) in enumerate(fields):
        label = tk.Label(container, text=label_text)
        entry = tk.Entry(container, textvariable=var)
        label.grid(row=index, column=0, sticky='w', pady=8)
        entry.grid(row=index, column=1, sticky='w', pady=8, padx=(12, 0))

    regular_var = tk.BooleanVar()
    label = tk.Label(container, text="Regular")
    checkbox = tk.Checkbutton(container, variable=regular_var, onvalue=True, offvalue=False)
    label.grid(row=2, column=0, sticky='w', pady=8)
    checkbox.grid(row=2, column=1, sticky='w', pady=8, padx=(12, 0))
    
    container.columnconfigure(1, weight=1)

    def on_submit():
        values = [var.get() for _, var in fields]
        values.append(regular_var.get())
        cb(values[0], values[1], values[2])

    submit_button = tk.Button(container, text='Submit', command=on_submit)
    submit_button.grid(row=3, column=0, columnspan=2, pady=16)
    
    root.mainloop()
