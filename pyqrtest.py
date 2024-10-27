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

import tomlkit
import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, ttk
from PIL import ImageTk, Image
import qrcode
import shortuuid
from icecream import ic


def create_qr(qr_data, qr_size=250):
    img = qrcode.make(qr_data, version=1)
    return img.resize((qr_size, qr_size))


def test_dialog(dialog_text):
    messagebox.showinfo("Example", dialog_text)


def save_qr(qr_image):
    files = [("Image File", "*.png"), ("All Files", "*.*")]
    file_path = filedialog.asksaveasfilename(filetypes=files, defaultextension=files)
    if file_path:
        qr_image.save(file_path)

def generate_qr(qr_data, config_data):
    qr_data_formulate = (
        f"UserID:{config_data["Required"]["UserID"]};"
        f"PVer:{config_data["Required"]["PVer"]};"
        f"SharedSecret:{config_ini["Required"]["SharedSecret"]};"
        f"UUID:{config_ini["Required"]["UUID"]};"
        f"EquipmentType:repeater;"
        f"Make:Motorola;"
        f"Model:GTR8000;"
        f"SystemName:EAC;"
        f"P1:1.1;"
        f"P2:2.2;"
        f"P3:3.3;"
        f"P4:4.4;"
        f"P5:5.5;"
        f"P6:6.6;"
        f"P7:7.7;"
        f"P8:8.8;"
        f"P9:9.9;"
        f"P10:10.10;"
        )
    qr = create_qr(qr_data)
    tkqr = ImageTk.PhotoImage(qr)
    qr_panel.configure(image=tkqr)
    qr_panel.image = tkqr

def initialize_ini():

    settings_file = "./settings.toml"
    ini_exists = os.path.isfile(settings_file)
    # TODO: add read interface TOML

    if ini_exists:
        with open(settings_file, "r") as configfile:
            toml_settings = tomlkit.load(configfile)
    else:
        username = simpledialog.askstring("Username", "Please enter your username:")
        shared_secret = simpledialog.askstring("Shared Secret", "Please enter the shared secret:")
        toml_settings = tomlkit.document()
        toml_settings.add(tomlkit.comment("Settings TOML Document"))
        toml_required = tomlkit.table()
        toml_required["UserID"] = username
        toml_required["PVer"] = "1"
        toml_required["SharedSecret"] = shared_secret
        toml_required["UUID"] = shortuuid.uuid()
        toml_settings.add("Required", toml_required)

        try:
            with open(settings_file, 'w') as configfile:
                configfile.write(tomlkit.dumps(toml_settings))
            # end open file
        except FileNotFoundError:
            pass


    return toml_settings


if __name__ == "__main__":
    data = "UserID:LevinBG;PVer:1;SharedSecret:104ab42f11;UUID:vytxeTZskVKR7C7WgdSP3d;EquipmentType:repeater;Make:Motorola;Model:GTR8000;SystemName:EAC;P1:1.1;P2:2.2;P3:3.3;P4:4.4;P5:5.5;P6:6.6;P7:7.7;P8:8.8;P9:9.9;P10:10.10"

    config_ini = initialize_ini()
    ic(config_ini["Required"]["UserID"])

    # Create and name window instance
    window = tk.Tk()
    window.title("QR Code Display")

    frame = tk.Frame(window)
    frame.pack(padx=20, pady=20)

    # Create the menu bar
    menubar = tk.Menu(window)

    # Create a File menu
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Save QR", command=lambda: save_qr(qr))
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
    qr_frame = tk.Frame(frame)
    image = Image.open("RFHSign.png").resize((250, 250))
    tkqr = ImageTk.PhotoImage(image)
    qr_panel = tk.Label(qr_frame, image=tkqr)
    qr_panel.pack()
    qr_frame.pack(side=tk.RIGHT, padx=(20,0))

    input_frame = tk.Frame(frame)

    make = ["Motorola", "Tait"]
    model = ["GTR8000", "Quantar", "9100", "9400"]
    system = ["E&E", "EAC", "Admin",]

    label_make = tk.Label(input_frame, text="Make", height=1).grid(column=0, row=0)
    combo_make = ttk.Combobox(input_frame, state="readonly", values=make, width=10).grid(column=1, row=0)

    label_model = tk.Label(input_frame, text="Model", height=1).grid(column=0, row=2)
    combo_model = ttk.Combobox(input_frame, state="readonly", values=model, width=10).grid(column=1, row=2)

    label_system = tk.Label(input_frame, text="System", height=1).grid(column=0, row=3)
    combo_system = ttk.Combobox(input_frame, state="readonly", values=system, width=10).grid(column=1, row=3)

    label_P1 = tk.Label(input_frame, text="P1", height=1).grid(column=0, row=4)
    input_P1 = tk.Text(input_frame, width=15, height=1).grid(column=1, row=4)

    label_P2 = tk.Label(input_frame, text="P2", height=1).grid(column=0, row=5)
    input_P2 = tk.Text(input_frame, width=15, height=1).grid(column=1, row=5)

    label_P3 = tk.Label(input_frame, text="P3", height=1).grid(column=0, row=6)
    input_P3 = tk.Text(input_frame, width=15, height=1).grid(column=1, row=6)

    label_P4 = tk.Label(input_frame, text="P4", height=1).grid(column=0, row=7)
    input_P4 = tk.Text(input_frame, width=15, height=1).grid(column=1, row=7)

    label_P5 = tk.Label(input_frame, text="P5", height=1).grid(column=0, row=8)
    input_P5 = tk.Text(input_frame, width=15, height=1).grid(column=1, row=8)

    button_generate = tk.Button(input_frame, text="Generate!", width=15, height=1, command=lambda:generate_qr(data, config_ini)).grid(column=1,row=9)

    input_frame.pack(side=tk.LEFT, anchor="ne")



    # Start the GUI
    window.mainloop()

# end main
