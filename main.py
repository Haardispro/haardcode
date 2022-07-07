#!/usr/bin/env python
from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
import tkinter.font
import os
import platform
import theme

# Colors
GLOBAL_THEME = theme.get_theme_from_dict(theme.DEFAULT_THEME_DICT)


w = Tk()
w.title("Haardcode")
w.geometry("800x600")
scroll_bar=Scrollbar(w)


def save_as_file():
    save_as_file.name = None
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
    try:
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
    except AttributeError:
        save_as_file()


def exit():
    w.destroy()


def new():
    main_text.delete(0.0, END)
    w.title("Haardcode")


# Shitty code 
"""
def preferences():
    os.system("python preferences.py")
"""
def about():
    os.system("python about.py")


def print_file():
    """Printing"""
    a = Tk()
    a.title("Print")
    a.configure(bg=GLOBAL_THEME.background)
    a.resizable(width=False, height=False)
    font=("Cascadia Code", 14)
    operating_system = platform.system()
    def normal_print():
        #lpr file.text
        if operating_system == 'Linux':
            try:
                if save_as_file.name is not None:
                    os.system("lp {}".format(save_as_file.name))
                    a.destroy()
            except AttributeError:
                if open_file.filename is not None:
                    os.system("lp {}".format(open_file.filename.name))
                    a.destroy()
        elif operating_system == 'Windows':
            try:
                if save_as_file.name is not None:
                    os.system("notepad /p {}".format(save_as_file.name))

            except AttributeError:
                if open_file.filename is not None:
                    os.system("notepad /p {}".format(open_file.filename.name))
    # Before printing set default printer
    heading = Label(a, text="Printing options", font=font, fg="white", bg=GLOBAL_THEME.background)
    note = Label(a, text="Note: Before you print, please set your default printer", font=font, fg="white", bg=GLOBAL_THEME.background)
    # normal button
    normal = Button(a, text="Normal Print", font=font, command=normal_print)
    # positions
    heading.grid(row=0, column=0, padx=10, pady=10)
    note.grid(row=1, column=0, padx=10, pady=10)
    normal.grid(row=2, column=0, padx=10, pady=10)
    a.mainloop()

# Font
font = tkinter.font.Font(family=GLOBAL_THEME.font, size=GLOBAL_THEME.font_size)

# Menubar
menubar=Menu(w, font=font, bg=GLOBAL_THEME.background, fg=GLOBAL_THEME.foreground, relief=FLAT)

# Files tab
files = Menu(menubar, tearoff=0, font=font, bg=GLOBAL_THEME.background, fg=GLOBAL_THEME.foreground, relief=FLAT)
files.add_command(label="New", command=new)
files.add_command(label="Open", command=open_file)
files.add_command(label="Save", command=save)
files.add_command(label="Save as..", command=lambda: save_as_file())
files.add_command(label="Print", command=print_file)
files.add_separator()
files.add_command(label="Exit", command=exit)
menubar.add_cascade(label="File", menu=files)

main_text = Text(w, width=800, height=600, wrap=WORD, font=font, bg=GLOBAL_THEME.background, fg=GLOBAL_THEME.foreground, insertbackground='white', highlightthickness=0, relief=SOLID)

# TODO: Continue here:
#   - Theme loader function
#   - Implement themes.py in here
def pick_theme():
    from tkinter import ttk
    theme.initialize_themes_folder()

    def load_theme():
        theme_name = clicked.get()
        new_editor_theme = theme.load_theme(theme_name)
        # Change the global theme var
        global GLOBAL_THEME
        GLOBAL_THEME = new_editor_theme
        font = tkinter.font.Font(family=GLOBAL_THEME.font, size=GLOBAL_THEME.font_size)

        # Apply the changes
        menubar.configure(
                bg=GLOBAL_THEME.background,
                fg=GLOBAL_THEME.foreground,
                font=font)
        edit.configure(
                bg=GLOBAL_THEME.background,
                fg=GLOBAL_THEME.foreground,
                font=font)
        files.configure(
                bg=GLOBAL_THEME.background,
                fg=GLOBAL_THEME.foreground,
                font=font)
        main_text.configure(
                bg=GLOBAL_THEME.background,
                fg=GLOBAL_THEME.foreground,
                font=font)

        print("Theme changed.")
        theme_window.destroy()

    # Available themes in themes folder
    themes = theme.list_themes()
    theme_window = Toplevel(w)
    #theme_window.configure(bg=GLOBAL_THEME.background, fg=GLOBAL_THEME.foreground)
    #theme_window.geometry("400x200")
    clicked = StringVar()
    clicked.set(themes[0])

    frame = Frame(theme_window)
    options = OptionMenu(frame, clicked, *themes)
    load_btn = Button(frame, text="Load theme", command=load_theme)
    load_btn.configure(bg=GLOBAL_THEME.background, fg=GLOBAL_THEME.foreground)
    options.pack()
    load_btn.pack()
    frame.grid(sticky="ne")
    theme_window.title("Theme selector")


# Edit
edit = Menu(menubar, tearoff=0, font=font, bg=GLOBAL_THEME.background, fg=GLOBAL_THEME.foreground, relief=FLAT)
#edit.add_command(label="Preferences", command=preferences)
edit.add_command(label="themes", command=pick_theme)
menubar.add_cascade(label="Edit", menu=edit)

#About
menubar.add_command(label="About", command=about)

#Help 
menubar.add_command(label="Help")

#Main Text Box

#positions
main_text.grid(row=1, column=0)
w.config(menu=menubar)
w.mainloop()
