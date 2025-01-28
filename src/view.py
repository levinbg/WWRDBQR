import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

import src.settings as settings

def test_dialog(dialog_text):
    messagebox.showinfo("Example", dialog_text)


def create_view(root):
    # Create and name window instance
    root.title("Test Application")
    root.geometry("600x600")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Create the menu bar
    menubar = tk.Menu(root)

    # Create a File menu
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(
        label="Save QR", command=lambda: test_dialog("Save_QR")
    )
    filemenu.add_command(label="Reset App", command=lambda: test_dialog("Reset_App"))
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    # Create an Edit menu
    editmenu = tk.Menu(menubar, tearoff=0)
    editmenu.add_command(label="Cut", command=lambda: test_dialog("Cut!"))
    editmenu.add_command(label="Copy", command=lambda: test_dialog("Copy!"))
    editmenu.add_command(label="Paste", command=lambda: test_dialog("Paste!"))
    menubar.add_cascade(label="Edit", menu=editmenu)

    # Configure the window to use the menu bar
    root.config(menu=menubar)

    # Display QR Code Frame
    input_frame = tk.Frame(root)
    image = Image.open("./assets/RFHSign.png").resize((200, 200))
    base = ImageTk.PhotoImage(image)
    qr_panel = tk.Label(input_frame, image=base)
    qr_panel.grid(row=0, column=0)


    tk.Label(input_frame, text="Make", height=1).grid(column=0, row=1)
    combo_make = ttk.Combobox(input_frame, state="readonly", values=settings.make, width=10)
    combo_make.grid(column=1, row=1)

    tk.Label(input_frame, text="Model", height=1).grid(column=0, row=2)
    combo_model = ttk.Combobox(input_frame, state="readonly", values=settings.model, width=10)
    combo_model.grid(column=1, row=2)

    tk.Label(input_frame, text="Network", height=1).grid(column=0, row=3)
    combo_network = ttk.Combobox(
        input_frame, state="readonly", values=settings.network, width=10
    )
    combo_network.grid(column=1, row=3)

    tk.Label(
        input_frame, text="Question_1", height=1
    ).grid(column=0, row=4)
    input_P1 = tk.Text(input_frame, width=15, height=1)
    input_P1.grid(column=1, row=4)

    tk.Label(
        input_frame, text="Question 2", height=1
    ).grid(column=0, row=5)
    input_P2 = tk.Text(input_frame, width=15, height=1)
    input_P2.grid(column=1, row=5)

    tk.Label(
        input_frame, text="Question_3", height=1
    ).grid(column=0, row=6)
    input_P3 = tk.Text(input_frame, width=15, height=1)
    input_P3.grid(column=1, row=6)

    tk.Label(
        input_frame, text="Question_4", height=1
    ).grid(column=0, row=7)
    input_P4 = tk.Text(input_frame, width=15, height=1)
    input_P4.grid(column=1, row=7)

    tk.Label(
        input_frame, text="Question_5", height=1
    ).grid(column=0, row=8)
    input_P5 = tk.Text(input_frame, width=15, height=1)
    input_P5.grid(column=1, row=8)

    button_generate = tk.Button(
        input_frame,
        text="Generate!",
        width=10,
        height=1,
        command=lambda: test_dialog("Generate!")).grid(column=1, row=9, sticky="E")

    input_frame.grid(column=0, row=1, padx=20, pady=20, sticky="N")

# end main
