import tkinter as tk

def create_view(root):
    root.title("My Tkinter App")
    label = tk.Label(root, text="Hello, Tkinter!")
    label.pack()
    button = tk.Button(root, text="Click Me", command=lambda: print("Button clicked"))
    button.pack()
