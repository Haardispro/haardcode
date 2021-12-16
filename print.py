from tkinter import *
import os #not yet used
import platform

a = Tk()
a.title("Print")

operating_system = platform.system()

def normal_print():
    if operating_system == 'Linux':
        print("sdf")
        #do lpr thing here 
    elif operating_system == 'Windows':
        print("sdf")
        #notepad /p file.txt
    else:
        print("Your os is not supported")


def landscape_print():
    if operating_system == 'Linux':
        print("sdf")
        #do lpr thing here with landscape 
    elif operating_system == 'Windows':
        print("sdf")
        #notepad /p file.txt
        #see how to print in landscape in windows
    else:
        print("Your os is not supported")
#Before printing set default printer
heading = Label(a, text="Printing options")
note = Label(a, text="Note: Before you print, please set your default printer")


#normal button
normal = Button(a, text="Normal Print")
#landscapes button
lanscape = Button(a, text="Landscape Print")

#positions
heading.grid(row=0, column=0, padx=10, pady=10)
note.grid(row=1, column=0, padx=10, pady=10)
normal.grid(row=2, column=0, padx=10, pady=10)
lanscape.grid(row=3, column=0, padx=10, pady=10)



a.mainloop()
