import tkinter as tk


class BaseView(tk.Frame):
    def __init__(self, master, on_navigate, title, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.on_navigate = on_navigate
        self.pack(fill='both', expand=True)

        master.title(title)
        tk.Button(
            self,
            text='Back to Home',
            command=lambda: self.on_navigate('main'),
        ).pack()


class EntryFormView(BaseView):
    def __init__(self, master, on_navigate, title):
        super().__init__(master, on_navigate, title)
        master.geometry('500x500')

        form = self._build_form_section()
        form.pack(pady=16)

    def _build_form_section(self):
        section = tk.Frame(self)

        tk.Label(section, text='Title').grid(
            row=0, column=0, sticky='w', padx=8, pady=6
        )
        self.title_entry = tk.Entry(section, width=30)
        self.title_entry.grid(row=0, column=1, padx=8, pady=6)

        tk.Label(section, text='Value').grid(
            row=1, column=0, sticky='w', padx=8, pady=6
        )
        self.value_entry = tk.Entry(section, width=30)
        self.value_entry.grid(row=1, column=1, padx=8, pady=6)

        tk.Button(section, text='Submit', command=self._on_submit).grid(
            row=2,
            column=0,
            columnspan=2,
            pady=10,
        )

        return section

    def _on_submit(self):
        title = self.title_entry.get().strip()
        value = self.value_entry.get().strip()
        self.on_submit(title, value)

    def on_submit(self, title, value):
        raise NotImplementedError
