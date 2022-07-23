from ast import Not
from tkinter import *
from tkinter import messagebox
import os
import email
from itertools import count
import yagmail
import openpyxl

root = Tk()
root.title("Create New Project")
root.geometry("500x750")
root.configure(bg='dark grey')


e = Entry(root, width=50, bg="gray",fg="white")
e.pack()
def submit():
    path = "C:/Users/smyli/Desktop/pyproj/"
    os.mkdir(path + e.get())
    myLabel = Label(root, text = "New project" + e.get() + " created, the path is: " + path + "\n Setting up the enviornment with the following folders: ").pack()
    
    if var0.get() !="":
        print(var0.get())
        Label(root, text = var0.get()).pack()
        with open(path + e.get() + '/main.py', 'w') as fp:
            fp.write('#This is the main file for the WIP project ' + e.get())
            pass
    if var1.get() !="":
        print(var1.get())
        Label(root, text = var1.get()).pack()
        with open(path + e.get() + '/readme.txt', 'w') as fp:
            fp.write('README for ' + e.get() + "\n")
            pass

    
   


var0 = StringVar()
var1= StringVar()

# Function to use when button is clicked displaying info from checkbox

# Check widget used to display a number of toggle buttons/boxes for different options                       
c1 = Checkbutton(root, text = "Main", variable=var0, onvalue="Main", offvalue="")
c1.deselect
c1.pack()
c2 = Checkbutton(root, text = "Readme", variable=var1, onvalue="Readme", offvalue="")
c2.deselect
c2.pack()
# Create External root using function show info from selected checkbox                       
Button(root, text="Ok", command=submit).pack()

root.mainloop()

