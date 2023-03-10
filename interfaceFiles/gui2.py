
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame2"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def makeWindow():
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
        303.0,
        32.0,
        anchor="nw",
        text="Inventory Editor",
        fill="#FFFFFF",
        font=("Inter", 35 * -1)
    )
    
    canvas.create_text(
        8.0,
        7.0,
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
        x=233.0,
        y=149.0,
        width=183.0,
        height=39.0
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
        x=490.0,
        y=149.0,
        width=142.0,
        height=39.0
    )
    
    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=362.0,
        y=486.0,
        width=141.0,
        height=29.0
    )
    
    canvas.create_text(
        5.0,
        542.0,
        anchor="nw",
        text="Developed by Garrett Flowers, William Davis, Seth Deloney",
        fill="#FFFFFF",
        font=("Inter Bold", 10 * -1)
    )
    
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        497.5,
        416.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=383.0,
        y=404.0,
        width=229.0,
        height=23.0
    )
    
    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        497.5,
        362.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=383.0,
        y=350.0,
        width=229.0,
        height=23.0
    )
    
    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        497.5,
        308.5,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=383.0,
        y=296.0,
        width=229.0,
        height=23.0
    )
    
    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        497.5,
        254.5,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=383.0,
        y=242.0,
        width=229.0,
        height=23.0
    )
    
    canvas.create_text(
        254.0,
        247.0,
        anchor="nw",
        text="Computer Name:",
        fill="#FFFFFF",
        font=("Inter Bold", 12 * -1)
    )
    
    canvas.create_text(
        254.0,
        301.0,
        anchor="nw",
        text="Username:",
        fill="#FFFFFF",
        font=("Inter Bold", 12 * -1)
    )
    
    canvas.create_text(
        254.0,
        360.0,
        anchor="nw",
        text="Serial Number:",
        fill="#FFFFFF",
        font=("Inter Bold", 12 * -1)
    )
    
    canvas.create_text(
        254.0,
        410.0,
        anchor="nw",
        text="Model Identifier:",
        fill="#FFFFFF",
        font=("Inter Bold", 12 * -1)
    )
    
    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=485.0,
        y=103.0,
        width=31.0,
        height=23.0
    )
    
    canvas.create_text(
        346.0,
        109.0,
        anchor="nw",
        text="Surplus Form Export Location",
        fill="#FFFFFF",
        font=("Inter Bold", 9 * -1)
    )
    
    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    button_5.place(
        x=61.0,
        y=41.0,
        width=64.0,
        height=25.0
    )
    window.resizable(False, False)
    window.mainloop()
    