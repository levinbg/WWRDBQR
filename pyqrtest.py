import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import qrcode
from icecream import ic


def create_qr(qr_data, qr_size=150):
    img = qrcode.make(qr_data, version=1)
    return img.resize((qr_size, qr_size))


def test_dialog(dialog_text):
    messagebox.showinfo("Example", dialog_text)


def save_qr(qr_image):
    files = [("Image File", "*.png"), ("All Files", "*.*")]
    file_path = filedialog.asksaveasfilename(filetypes=files, defaultextension=files)
    if file_path:
        qr_image.save(file_path)


if __name__ == "__main__":
    data = "UserID:LevinBG;PVer:1;SharedSecret:104ab42f11;UUID:vytxeTZskVKR7C7WgdSP3d;EquipmentType:repeater;Make:Motorola;Model:GTR8000;SystemName:EAC;P1:1.1;P2:2.2;P3:3.3;P4:4.4;P5:5.5;P6:6.6;P7:7.7;P8:8.8;P9:9.9;P10:10.10"

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
    
    input_frame = tk.Frame(frame)
    
    label_make = tk.Label(input_frame, text="Make", height=1)
    label_make.grid(column=0, row=0)
    input_make = tk.Text(input_frame, width=10, height=1)
    input_make.grid(column=1, row=0)
    
    label_model = tk.Label(input_frame, text="Model", height=1)
    label_model.grid(column=0, row=2)
    input_model = tk.Text(input_frame, width=10, height=1)
    input_model.grid(column=1, row=2)
    
    label_system = tk.Label(input_frame, text="System", height=1)
    label_system.grid(column=0, row=3)
    input_system = tk.Text(input_frame, width=10, height=1)
    input_system.grid(column=1, row=3)
    
    label_P1 = tk.Label(input_frame, text="P1", height=1)
    label_P1.grid(column=0, row=4)
    input_P1 = tk.Text(input_frame, width=10, height=1)
    input_P1.grid(column=1, row=4)
    
    label_P2 = tk.Label(input_frame, text="P2", height=1)
    label_P2.grid(column=0, row=5)
    input_P2 = tk.Text(input_frame, width=10, height=1)
    input_P2.grid(column=1, row=5)
    
    label_P3 = tk.Label(input_frame, text="P3", height=1)
    label_P3.grid(column=0, row=6)
    input_P3 = tk.Text(input_frame, width=10, height=1)
    input_P3.grid(column=1, row=6)
    
    label_P4 = tk.Label(input_frame, text="P4", height=1)
    label_P4.grid(column=0, row=7)
    input_P4 = tk.Text(input_frame, width=10, height=1)
    input_P4.grid(column=1, row=7)
    
    label_P5 = tk.Label(input_frame, text="P5", height=1)
    label_P5.grid(column=0, row=8)
    input_P5 = tk.Text(input_frame, width=10, height=1)
    input_P5.grid(column=1, row=8)
    
    input_frame.pack()
    # input_frame.grid(column=0, row=0)
    
    
     # Display QR Code
    qr_frame = tk.Frame(frame)
    qr = create_qr(data)
    tkqr = ImageTk.PhotoImage(qr)
    label = tk.Label(qr_frame, image=tkqr)
    label.image = tkqr
    qr_frame.pack()
    # qr_frame.grid(column=1, row=0)

    # Start the GUI
    window.mainloop()

# end main
