import tkinter as tk

from controllers.main_controller import MainController


def main():
    root = tk.Tk()
    app = MainController(root)
    app.start()
    root.mainloop()


if __name__ == '__main__':
    main()
