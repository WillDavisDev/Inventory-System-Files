
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent / "assets/frame0"
ASSETS_PATH = OUTPUT_PATH # / Path(r"C:\Users\wld0015\OneDrive - Auburn University\Documents\GitHub\Inventory-System-Files\mainGUI.V.0.2\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("865x558")
window.configure(bg = "#242424")


canvas = Canvas(
    window,
    bg = "#242424",
    height = 558,
    width = 865,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    320.0,
    42.0,
    anchor="nw",
    text="ACES/AG IMS",
    fill="#FFFFFF",
    font=("Inter", 35 * -1)
)

canvas.create_text(
    6.0,
    5.0,
    anchor="nw",
    text="V. 0.2",
    fill="#FF2D00",
    font=("Inter", 10 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=290.0,
    y=294.0,
    width=285.3363342285156,
    height=48.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=290.0,
    y=215.0,
    width=285.3363342285156,
    height=48.0
)

canvas.create_text(
    5.0,
    542.0,
    anchor="nw",
    text="Developed by Garrett Flowers, William Davis, Seth Deloney",
    fill="#FFFFFF",
    font=("Inter Bold", 10 * -1)
)
window.resizable(False, False)
window.mainloop()
