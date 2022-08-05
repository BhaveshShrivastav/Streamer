from os import startfile
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Replace the path here to te file.
# example => path = r"C:\Users\path\to\file.mp4"
path = r"C:\Users\path\to\file.mp4"


# streamer func
def streamer():
    startfile(path)


# ui func
def ui():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Streamer App").grid(column=0, row=0)
    # image = Image.open(r"D:\Development\tt.png")
    # python_image = ImageTk.PhotoImage(image)
    # ttk.Button(frm, text="Play", image=python_image, command=streamer).grid(column=1, row=0)
    ttk.Button(frm, text="Play", command=streamer).grid(column=1, row=0)
    root.mainloop()


def main():
    ui()

# Initiate the Streamer App
if __name__ == '__main__':
    main()
