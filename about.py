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
authors_label = Label(q, text="Authors: Haard Majmudar", font=font, fg="white", bg=bg)
#Version 0.0.1
version_label = Label(q, text="Version: 0.0.1", font=font, bg=bg, fg="white")


#positions
heading.grid(row=0, column=0, padx=230, pady=10)
authors_label.grid(row=1, column=0, pady=10)#, padx=230, pady=10)
version_label.grid(row=2, column=0, pady=10)#, padx=230, pady=10)

q.mainloop()
