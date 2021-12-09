from tkinter import *

q = Tk()
q.title("About")
bg="#282828"
q.config(bg=bg)
q.geometry("600x400")

#What is Haardcode 
#haardcode is a text editor made in python 
font = ("Cascadia Code", 20, "underline")

heading = Label(q, text="Haardcode", fg="white", bg=bg, font=font)



#Authors: Haard Majmudar
#Version 0.0.1
#Made on [insert date of finish]

#positions
heading.grid(row=0, column=0, padx=230, pady=10)

q.mainloop()
