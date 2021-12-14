#from main import font
from tkinter import *
import platform,os

from tkinter.filedialog import askopenfile

Operating_System = platform.system()
x = Tk()
x.geometry("1400x1600")
x.title("Preferences")
bg = "#282828"
x.config(bg=bg)

#Main font for the interface
font = ("Cascadia Code", 14)
font2 = ("Cascadia Code", 16)


    
        
printerName_label = Label(x, text="Enter Printer Name(must be accurate): ", font=font, fg="white", bg=bg)
printerEntry = Entry(x, width=20, font=font)



# font_size_label = Label(x, text="Font Size : ", bg=bg, fg="white", font=font)
# font_size = Entry(x, width=20, font=font)
def printDocumentCommand():
    fileName = askopenfile(title="Open File").name
    printerName = printerEntry.get()
    if Operating_System=="Linux":
        os.system(f"lpr -P {printerName} {fileName}")
    else:
        print("Switch to GNU/Linux bro...")

B =Button(x, text ="Print", command = printDocumentCommand)
B.grid(row=6,column=1)


#Fonts
printerName_label.grid(row=1, column=1, pady=10)
printerEntry.grid(row=1, column=2, pady=10)
# font_size_label.grid(row=2, column=1, pady=10)
# font_size.grid(row=2, column=2, pady=10)
#font_style = Entry(x, width=10)
#this has to be a dropdown menu

#Colors 

#Heading

x.mainloop()
