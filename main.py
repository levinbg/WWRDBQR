import tkinter as tk
from src.view import create_view


def main():
    root = tk.Tk()
    create_view(root)
    root.mainloop()


if __name__ == "__main__":
    main()
