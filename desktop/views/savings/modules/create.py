import tkinter as tk

def create_saving(parent=None):
    is_standalone = parent is None
    root = tk.Toplevel(parent)
    root.title("Create Saving")
    root.resizable(False, False)

    container = tk.Frame(root, padx=24, pady=24)
    container.pack(fill="both", expand=True)

    fields = [
        ("Title", tk.StringVar(master=root)),
        ("Amount", tk.StringVar(master=root)),
        ("Local", tk.StringVar(master=root)),
    ]

    for index, (label_text, var) in enumerate(fields):
        label = tk.Label(container, text=label_text)
        entry = tk.Entry(container, textvariable=var)
        label.grid(row=index, column=0, sticky="w", pady=8)
        entry.grid(row=index, column=1, sticky="ew", pady=8, padx=(12, 0))

    container.columnconfigure(1, weight=1)

    def on_submit():
        values = [var.get() for _, var in fields]
        print("New saving:", values)

    submit_button = tk.Button(container, text="Submit", command=on_submit)
    submit_button.grid(row=len(fields), column=0, columnspan=2, pady=16)
    if is_standalone:
        root.mainloop()
