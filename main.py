#!/usr/bin/env python
from tkinter import *
from tkinter.filedialog import *
import tkinter.font
import os
#import keyboard
#import subprocess

w = Tk()
w.title("Haardcode")
w.geometry("800x600")

def save_as_file():
    
    f=asksaveasfile(mode="w", defaultextension=".txt")
    if f is None:
        return 
    else:
        save_as_file.name = f.name
        base = os.path.basename(save_as_file.name)
        w.title("Haardcode - {}".format(base))
    text2save=str(main_text.get(1.0, END))
    f.write(text2save)
    f.close()

def open_file():
    open_file.filename = askopenfile(mode = "r")
    if open_file.filename is not None:
        content = open_file.filename.read()
        main_text.delete(0.0, END)
        main_text.insert(END, content)

def save():
    if save_as_file.name is not None:
        with open (save_as_file.name, 'r+') as myfile:
            data = myfile.read()
            myfile.seek(0)
            myfile.write(str(main_text.get(1.0, END)))
            myfile.truncate()
    elif save_as_file.name is None and open_file.filename is not None:
        with open (open_file.filename, 'r+') as myfile:
            data = myfile.read()
            myfile.seek(0)
            myfile.write(str(main_text.get(1.0, END)))
            myfile.truncate()
    elif save_as_file.name is None and open_file.filename is None:
        save_as_file()

def exit():
    w.destroy()

def new():
    main_text.delete(0.0, END)
    w.title("Haardcode")


def preferences():
    import preferences

def about():
    import about
#Font
n=14
font = tkinter.font.Font(family='Cascadia Code', size=n)

#Menubar
menubar=Menu(w, font=font, bg="#282828", fg="#f8f8f2", relief=FLAT)

#Files tab
files = Menu(menubar, tearoff=0, font=font, bg="#282828", fg="#f8f8f2", relief=FLAT)
files.add_command(label="New", command=new)
files.add_command(label="Open", command=open_file)
files.add_command(label="Save", command=save)
files.add_command(label="Save as..", command=lambda:save_as_file())
files.add_command(label="Print")
files.add_separator()
files.add_command(label="Exit", command=exit)
menubar.add_cascade(label="File", menu=files)

#Edit
edit = Menu(menubar, tearoff=0, font=font, bg="#282828", fg="#f8f8f2", relief=FLAT)
edit.add_command(label="Preferences", command=preferences)
menubar.add_cascade(label="Edit", menu=edit)

#About
menubar.add_command(label="About", command=about)

#Help 
menubar.add_command(label="Help")

#Main Text Box
main_text = Text(w, width=800, height=600, wrap=WORD, font=font, bg="#282828", fg="#f8f8f2", insertbackground='white', highlightthickness=0, relief=SOLID)

#positions
main_text.grid(row=1, column=0)

w.winfo_geometry()

w.config(menu=menubar)
w.mainloop()

