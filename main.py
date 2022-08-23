from ast import Not
import tkinter
from tkinter import messagebox
import os
import email
from itertools import count
import yagmail
import openpyxl

root = tkinter.Tk()
root.title("Create New Project")
root.geometry("500x750")
root.configure(bg='dark grey')


e = tkinter.Entry(root, width=50, bg="gray",fg="white")
e.pack()
def submit():
    path = "C:/Users/smyli/Desktop/pyproj/"
    os.mkdir(path + e.get())
    myLabel = tkinter.Label(root, text = "New project" + e.get() + " created, the path is: " + path + "\n Setting up the enviornment with the following folders: ").pack()
    
    if var0.get() !="":
        print(var0.get())
        tkinter.Label(root, text = var0.get()).pack()
        with open(path + e.get() + '/main.py', 'w') as fp:
            fp.write('#This is the main file for the WIP project ' + e.get())
    if var1.get() !="":
        print(var1.get())
        tkinter.Label(root, text = var1.get()).pack()
        with open(path + e.get() + '/readme.txt', 'w') as fp:
            fp.write('README for ' + e.get() + "\n")

    
   


var0 = tkinter.StringVar()
var1= tkinter.StringVar()

# Function to use when button is clicked displaying info from checkbox

# Check widget used to display a number of toggle buttons/boxes for different options                       
c1 = tkinter.Checkbutton(root, text = "Main", variable=var0, onvalue="Main", offvalue="")
c1.deselect
c1.pack()
c2 = tkinter.Checkbutton(root, text = "Readme", variable=var1, onvalue="Readme", offvalue="")
c2.deselect
c2.pack()
# Create External root using function show info from selected checkbox                       
tkinter.Button(root, text="Ok", command=submit).pack()

root.mainloop()

