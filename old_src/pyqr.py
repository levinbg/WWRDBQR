#!/usr/bin/env python

"""Python application to create QR code for PM's in the radio database.

This is a single application that generates a QR code based on

__author__ = "Brian Levin"
__copyright__ = "Copyright 2024, Brian Levin"
__credits__ = ["Brian Levin", "Allan Richards"]
__license__ = "BSDv3"
__version__ = "0.0.1"
__maintainer__ = "Brian Levin"
__email__ = "levinbg@fan.gov"
__status__ = "Alpha"
"""

import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, ttk
from tkinterweb import HtmlFrame

import qrcode
import markdown
import shortuuid
import tomlkit
from icecream import ic
from PIL import Image, ImageTk


def create_qr(qr_data):
    ic(qr_data)
    img = qrcode.make(qr_data, version=1)
    return img.resize((config_ini["Interface"]["qr_size"], config_ini["Interface"]["qr_size"]))


def test_dialog(dialog_text):
    messagebox.showinfo("Example", dialog_text)


def save_qr(qr):
    files = [("Image File", "*.png"), ("All Files", "*.*")]
    file_path = filedialog.asksaveasfilename(filetypes=files, defaultextension=files)
    if file_path:
        qr.save(file_path)


def generate_docs():

    md_content = [os.path.join(root, file) for root, dirs, files in os.walk("docs") for file in files if file.endswith(".md")]


def get_doc():
    user_input = get_user_input()
    pmi_doc_path = f"docs/{user_input["model"]}/index.md" if user_input["model"] else f"docs/default/index.md"

    with open(pmi_doc_path, "r", encoding="utf-8") as md_file:
        md_contents = md_file.read()

    html_doc = markdown.markdown(md_contents)
    doc_frame = HtmlFrame(window)
    doc_frame.set_fontscale(2)
    doc_frame.load_html(html_doc)
    doc_frame.grid(row=0, column=2, sticky="NSEW", rowspan=2)
    doc_frame.grid_rowconfigure(0, weight=1)
    doc_frame.grid_columnconfigure(2, weight=1)


def on_resize(event):
    pass


def reset_app():
    if os.path.exists("settings.toml"):
        answer = messagebox.askokcancel(
            "Reseet TOML", "Do you really want to delete settings.toml?"
        )
        if answer:
            os.remove("settings.toml")
            python = sys.executable
            os.execl(python, python, *sys.argv)


def get_user_input():
    user_input = {
        "equipment_type": "repeater",
        "make": combo_make.get(),
        "model": combo_model.get(),
        "network": combo_network.get(),
        "P1": input_P1.get("1.0", "end-1c"),
        "P2": input_P2.get("1.0", "end-1c"),
        "P3": input_P3.get("1.0", "end-1c"),
        "P4": input_P4.get("1.0", "end-1c"),
        "P5": input_P5.get("1.0", "end-1c"),
    }

    user_input = {
        key: (None if not value else value) for key, value in user_input.items()
    }

    return user_input


def generate_qr(config_data):
    user_input = get_user_input()

    qr_data_formulate = (
        f"UserID:{config_data["Required"]["UserID"]};"
        f"PVer:{config_data["Required"]["PVer"]};"
        f"SharedSecret:{config_data["Required"]["SharedSecret"]};"
        f"UUID:{config_data["Required"]["UUID"]};"
        f"EquipmentType:{user_input["equipment_type"]};"
        f"Make:{user_input["make"]};"
        f"Model:{user_input["model"]};"
        f"Network:{user_input["network"]};"
        f"P1:{user_input["P1"]};"
        f"P2:{user_input["P2"]};"
        f"P3:{user_input["P3"]};"
        f"P4:{user_input["P4"]};"
        f"P5:{user_input["P5"]};"
    )

    ic(qr_data_formulate)
    return create_qr(qr_data_formulate)


def display_qr(qr):
    tkqr = ImageTk.PhotoImage(qr)
    qr_panel.configure(image=tkqr)
    qr_panel.image = tkqr


def initialize_ini():
    settings_file = "./settings.toml"
    ini_exists = os.path.isfile(settings_file)

    generate_docs()

    if ini_exists:
        with open(settings_file, "r", encoding="utf-8") as configfile:
            toml_settings = tomlkit.load(configfile)
    else:
        username = simpledialog.askstring("Username", "Please enter your username:")
        shared_secret = simpledialog.askstring(
            "Shared Secret", "Please enter the shared secret:"
        )
        toml_settings = tomlkit.document()
        toml_settings.add(tomlkit.comment("Settings TOML Document"))
        toml_required = tomlkit.table()
        toml_required["UserID"] = username
        toml_required["PVer"] = "1"
        toml_required["SharedSecret"] = shared_secret
        toml_required["UUID"] = shortuuid.uuid()
        toml_settings.add("Required", toml_required)

        toml_interface = tomlkit.table()
        toml_interface["window_title"] = "PMI Buddy"
        toml_interface["qr_size"] = 250
        toml_interface["window_size_x"] = 800
        toml_interface["window_size_y"] = 500
        toml_interface["window_padding"] = 20
        toml_interface["Question_1"] = "Question 1: "
        toml_interface["Question_2"] = "Question 2: "
        toml_interface["Question_3"] = "Question 3: "
        toml_interface["Question_4"] = "Question 4: "
        toml_interface["Question_5"] = "Question 5: "

        toml_settings.add("Interface", toml_interface)

        try:
            with open(settings_file, "w", encoding="utf-8") as configfile:
                configfile.write(tomlkit.dumps(toml_settings))
            # end open file
        except FileNotFoundError:
            pass

    return toml_settings


def set_menus():
    pass


if __name__ == "__main__":
    config_ini = initialize_ini()
    ic(config_ini)

    # Create and name window instance
    window = tk.Tk()
    window.title(config_ini["Interface"]["window_title"])
    window.geometry("+%d+%d" % (window.winfo_width(), window.winfo_height()))
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    # Create the menu bar
    menubar = tk.Menu(window)

    # Create a File menu
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(
        label="Save QR", command=lambda: save_qr(generate_qr(config_ini))
    )
    filemenu.add_command(label="Reset App", command=lambda: reset_app())
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=window.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    # Create an Edit menu
    editmenu = tk.Menu(menubar, tearoff=0)
    editmenu.add_command(label="Cut", command=lambda: test_dialog("Cut!"))
    editmenu.add_command(label="Copy", command=lambda: test_dialog("Copy!"))
    editmenu.add_command(label="Paste", command=lambda: test_dialog("Paste!"))
    menubar.add_cascade(label="Edit", menu=editmenu)

    # Configure the window to use the menu bar
    window.config(menu=menubar)

    # Display QR Code Frame
    input_frame = tk.Frame(window)
    image = Image.open("RFHSign.png").resize((config_ini["Interface"]["qr_size"], config_ini["Interface"]["qr_size"]))
    base = ImageTk.PhotoImage(image)
    qr_panel = tk.Label(input_frame, image=base)
    qr_panel.grid(row=0, column=0)



    make = ["Motorola", "Tait"]
    model = ["GTR8000", "Quantar", "9100", "9400"]
    network = [
        "E&E",
        "EAC",
        "Admin",
    ]

    tk.Label(input_frame, text="Make", height=1).grid(column=0, row=1)
    combo_make = ttk.Combobox(input_frame, state="readonly", values=make, width=10)
    combo_make.grid(column=1, row=1)

    tk.Label(input_frame, text="Model", height=1).grid(column=0, row=2)
    combo_model = ttk.Combobox(input_frame, state="readonly", values=model, width=10)
    combo_model.grid(column=1, row=2)

    tk.Label(input_frame, text="Network", height=1).grid(column=0, row=3)
    combo_network = ttk.Combobox(
        input_frame, state="readonly", values=network, width=10
    )
    combo_network.grid(column=1, row=3)

    tk.Label(
        input_frame, text=config_ini["Interface"]["Question_1"][:15], height=1
    ).grid(column=0, row=4)
    input_P1 = tk.Text(input_frame, width=15, height=1)
    input_P1.grid(column=1, row=4)

    tk.Label(
        input_frame, text=config_ini["Interface"]["Question_2"][:15], height=1
    ).grid(column=0, row=5)
    input_P2 = tk.Text(input_frame, width=15, height=1)
    input_P2.grid(column=1, row=5)

    tk.Label(
        input_frame, text=config_ini["Interface"]["Question_3"][:15], height=1
    ).grid(column=0, row=6)
    input_P3 = tk.Text(input_frame, width=15, height=1)
    input_P3.grid(column=1, row=6)

    tk.Label(
        input_frame, text=config_ini["Interface"]["Question_4"][:15], height=1
    ).grid(column=0, row=7)
    input_P4 = tk.Text(input_frame, width=15, height=1)
    input_P4.grid(column=1, row=7)

    tk.Label(
        input_frame, text=config_ini["Interface"]["Question_5"][:15], height=1
    ).grid(column=0, row=8)
    input_P5 = tk.Text(input_frame, width=15, height=1)
    input_P5.grid(column=1, row=8)

    button_generate = tk.Button(
        input_frame,
        text="Generate!",
        width=10,
        height=1,
        command=lambda: display_qr(generate_qr(config_ini)),
    ).grid(column=1, row=9, sticky="E")

    input_frame.grid(column=0, row=1, padx=20, pady=20, sticky="N")

    get_doc()

    window.bind("<Configure>", on_resize)
    # Start the GUI
    window.mainloop()

# end main
