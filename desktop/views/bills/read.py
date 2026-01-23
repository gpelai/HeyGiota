import tkinter as tk


def read_bill(parent=None):
    root = tk.Toplevel(parent) if parent is not None else tk.Tk()
    root.title('Read Bill')
    root.resizable(False, False)

    container = tk.Frame(root, padx=24, pady=24)
    container.pack(fill='both', expand=True)

    fields = [
        ("ID", tk.StringVar()),
    ]

    for index, (label_text, var) in enumerate(fields):
        label = tk.Label(container, text=label_text)
        entry = tk.Entry(container, textvariable=var)
        label.grid(row=index, column=0, sticky='w', pady=8)
        entry.grid(row=index, column=1, sticky='w', pady=8, padx=(12, 0))
    
    container.columnconfigure(1, weight=1)

    def on_submit():
        values = [var.get() for _, var in fields]
        print("Bill id", values)

    submit_button = tk.Button(container, text='Submit', command=on_submit)
    submit_button.grid(row=3, column=0, columnspan=2, pady=16)
    
    root.mainloop()
