#from main import font
from tkinter import *

x = Tk()
x.geometry("800x600")
x.title("Preferences")
bg = "#282828"
x.config(bg=bg)

#Main font for the interface
font = ("Cascadia Code", 14)
font2 = ("Cascadia Code", 16)

#Heading
head_font = Label(x, text="Change your font : ", font=font2, bg=bg, fg="white")
head_color = Label(x, text="Change your colors : ", font=font2, fg="white", bg=bg)
#Font 
font_name_label = Label(x, text="Font Name : ", font=font, fg="white", bg=bg)
font_name = Entry(x, width=20, font=font)
font_size_label = Label(x, text="Font Size : ", bg=bg, fg="white", font=font)
font_size = Entry(x, width=20, font=font)

font_style_label = Label(x, text="Font Style :", bg=bg, font=font, fg="white")
#font_style = Entry(x, width=10)
#this has to be a dropdown menu

#Colors 
custom_color_label = Label(x, text="Your custom colors:", font=font, bg=bg, fg="white")
bg_color_label = Label(x, text="Enter Bg Color: ", font=font, bg=bg, fg="white")
fg_color_label = Label(x, text="Enter Fg Color: ", font=font, bg=bg, fg="white")
fg_color = Entry(x, width=20, font=font)
bg_color = Entry(x, width=20, font=font)
#dropdown menu
options = [
	"Gruvbox",
	"Dracula", 
        "Solarized Dark"
]
clicked = StringVar(x)
clicked.set( "Gruvbox" )
color_drop_label = Label(x, text="Pre-configured Themes: ", font=font, fg="white", bg=bg)
color_drop = OptionMenu( x , clicked , *options )
color_drop.config(font=font)
#Positions
#Heading
head_font.grid(row=0, column=1)
head_color.grid(row=3, column=1)
#Fonts
font_name_label.grid(row=1, column=1, pady=10)
font_name.grid(row=1, column=2, pady=10)
font_size_label.grid(row=2, column=1, pady=10)
font_size.grid(row=2, column=2, pady=10)
#Colors
custom_color_label.grid(row=4, column=1, pady=10)
bg_color_label.grid(row=5, column=1, pady=10)
fg_color_label.grid(row=6, column=1, pady=10)
bg_color.grid(row=5, column=2, pady=10)
fg_color.grid(row=6, column=2, pady=10)
color_drop.grid(row=7, column=2, pady=10)
color_drop_label.grid(row=7, column=1, padx=10)
x.mainloop()
