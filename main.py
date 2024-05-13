from tkinter import *
import string
import random

string.ascii_letters

root = Tk()
root.title("Password generator")

Arial = ("Arial", 15) 
ArialSmall = ("Arial", 10) 

title = Label(root, text="PASSWORD GENERATOR")
title.configure(font=Arial)

text = Entry(root)

def generatePassword():
    password = ""

    i = 0
    
    while i <= 10:
        password += random.choice(string.ascii_letters)
        i += 1

    text.delete(0,"end")

    text.insert(0, password)

generateButton = Button(root, text="generate", command=generatePassword)
generateButton.configure(font=ArialSmall)

title.pack()
text.pack()
generateButton.pack()

root.mainloop()