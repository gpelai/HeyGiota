import tkinter as tk

def read_all_bills(parent=None):
    root = tk.Toplevel(parent) if parent is not None else tk.Tk()
    root.title('List Bills')
    root.resizable(False, False)

    container = tk.Frame(root, padx=24, pady=24)
    container.pack(fill='both', expand=True)

    
    
    root.mainloop()
