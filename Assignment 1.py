# Name:         Jonathan Tarrant
# Assignment:   01
# Section:      01
# Due Date:     09/16/2022

# Library imports
import tkinter as tk
from tkinter import CENTER, ttk

# Create Root Window
root = tk.Tk() 

# Set Window Attributes
root.title("Assignment 1")
root.geometry("500x360")
root.resizable(width=True, height=True)
root.configure(bg="#3f3f3f")

# Config Grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)




# Call Mainloop
root.mainloop()