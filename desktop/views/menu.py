import tkinter as tk
from bills import bills
from investments import investments

def menu():
    root = tk.Tk()
    root.title("Menu")
    root.geometry("500x500")
    root.resizable(False, False)

    container = tk.Frame(root, padx=24, pady=24)
    container.pack(fill="both", expand=True)

    def on_bills():
        bills(root)

    def on_investments():
        investments(root)

    bills_button = tk.Button(container, text="Bills", command=on_bills, width=20)
    investments_button = tk.Button(container, text="Investments", command=on_investments, width=20)

    bills_button.pack(pady=12)
    investments_button.pack(pady=12)

    root.mainloop()


if __name__ == "__main__":
    menu()
