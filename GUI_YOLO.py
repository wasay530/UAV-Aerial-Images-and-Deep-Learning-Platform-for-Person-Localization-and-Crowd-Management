import tkinter as tk
from tkinter import ttk
#from PIL import Image, ImageTk
import sys
win = tk.Tk()
win.title("Python GUI")
#ttk.Label(win,text="A Label").grid(column=0, row=0)
a_label = ttk.Label(win, text="A Label")
a_label.grid(column=0, row=0)
# Button Click Event Function
def click_me():
    action.configure(text="**I have been clicked!**")
    a_label.configure(foreground='red')
    a_label.configure(text='A Red Label')
# Adding a Button
action = ttk.Button(win, text="click Me!", command=click_me)
action.grid(column=1, row=0)
path = "wasay.jpg"
#image adding
img = ImageTk.PhotoImage(Image.open('wasay.jpg'))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

win.mainloop()
