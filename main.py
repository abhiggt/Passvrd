import random
import pyperclip
from tkinter import *
import tkinter as tk
from tkinter import messagebox
#------------------------------------------------------------------------------------------------------------------------------------   
# Function for calculation of password 
def low(): 
	entry.delete(0, END) 

	# Get the length of passowrd 
	length = var1.get() 

	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
	password = "" 

	# if strength selected is low 
	if var.get() == 1: 
		for i in range(0, length): 
			password = password + random.choice(lower) 
		return password 

	# if strength selected is medium 
	elif var.get() == 0: 
		for i in range(0, length): 
			password = password + random.choice(upper) 
		return password 

	# if strength selected is strong 
	elif var.get() == 3: 
		for i in range(0, length): 
			password = password + random.choice(digits) 
		return password 

# Function for generation of password 
def generate(): 
	password1 = low() 
	entry.insert(10, password1)

#----------------------------------------------------------------------------#
#GUI
root = Tk()
root.title("Passvrd-Password Generator")
root.configure(background='#111111')
var = IntVar() 
var1 = IntVar()
#LOGO
title=Label(root,text="PassVrd",font=("product sans",42),compound = TOP,background='#111111',foreground="#baf7f0")
title.grid(row=0,column =2,padx=5, pady=5)
itle=Label(root,text="Choose your Password Mode",font=("consolas",12),compound = TOP,background='#111111',foreground="white")
itle.grid(row=1,column =2,padx=1, pady=1)
# Radio Buttons for deciding the strength of password (Default strength is Medium) 
radio_low = Radiobutton(root,text="Low",fg="#42f5bf",variable=var,bg='#111111', value=1)
radio_low.grid(row=2,padx=5, pady=5)
radio_middle = Radiobutton(root,text="Medium",fg="#42ffa1",variable=var,bg='#111111',value=0)
radio_middle.grid(row=2,column=2,padx=5, pady=5)
radio_strong = Radiobutton(root, text="Strong",fg="#2edb31",variable=var,bg='#111111',value=3) 
radio_strong.grid(row=2,column=3,padx=5, pady=5)

#slider for password length
slih = tk.Scale(root, from_=8, to=16, orient=HORIZONTAL,variable=var1,background='#111111',foreground="#baf7f0",highlightcolor="#baf7f0")
slih.grid(row=3,column=2,sticky="s",padx=1, pady=7)
slih.config(font="Avenir",length=253,sliderlength=17)

# create Button Generate which will generate the password
generate_button = Button(root,fg="#baf7f0",bg='#111111',text="Generate",font=("Product Sans",13),command=generate,compound = TOP)
generate_button.grid(row=4,column=2,padx=5, pady=7)

#Password text
entry = Entry(root,bg="#070d0c",font=("Product Sans",17),fg="white")
entry.grid(row=5,column=2,sticky="E",padx=3, pady=7)

# Function for copying password to clipboard and appending it to a file
def copy():
        passw=entry.get()
        pyperclip.copy(passw)
#------------------------------------------------------------------------------------------------------------------------------#

#Function for saving password
def savetov():
        copy()
        messagebox.showinfo('Saved', 'Successfully copied Password, Use it anywhere you like...\n')

        
save_button=Button(root, text="Copy",fg="#5ced9b",bg='#111111',font=("Product Sans",13),command=savetov,compound = LEFT) 
save_button.grid(row=6,column=2,padx=5, pady=7)

# start the GUI
root.mainloop()


