from tkinter import *

root = Tk()
root.title("Password generator")

Arial = ("Arial", 15) 
ArialSmall = ("Arial", 10) 

title = Label(root, text="PASSWORD GENERATOR")
title.configure(font=Arial)

generateButton = Button(root, text="generate")
generateButton.configure(font=ArialSmall)

title.pack()
generateButton.pack()

root.mainloop()