from tkinter import *
from tkinter.filedialog import asksaveasfile
import subprocess

w = Tk()
w.title("Haardcode")

def save_file():
    f=asksaveasfile(mode="w", defaultextension=".txt")
    if f is None:
        return 
    text2save=str(main_text.get(1.0, END))
    f.write(text2save)
    f.close()
def exit():
    w.destroy()

def preferences():
    import preferences.py


#Font
font = ("Cascadia Code", 14)

#Menubar
menubar=Menu(w, font=font, bg="#32333d", fg="#f8f8f2", relief=FLAT)

#Files tab
files = Menu(menubar, tearoff=0, font=font, bg="#32333d", fg="#f8f8f2", relief=FLAT)
files.add_command(label="New")
files.add_command(label="Save", command=lambda:save_file())
files.add_command(label="Edit")
files.add_separator()
files.add_command(label="Exit", command=exit)
menubar.add_cascade(label="File", menu=files)

#Edit
edit = Menu(menubar, tearoff=0, font=font, bg="#32333d", fg="#f8f8f2", relief=FLAT)
edit.add_command(label="Preferences")
menubar.add_cascade(label="Edit", menu=edit)

#About
menubar.add_command(label="About")

#Help 
menubar.add_command(label="Help")


#Main Text Box
main_text = Text(w, width=60, height=20, wrap=WORD, font=font, bg="#282a36", fg="#f8f8f2", insertbackground='white', highlightthickness=0, relief=SOLID)


#positions
main_text.grid(row=1, column=0)

w.config(menu=menubar)

w.mainloop()

