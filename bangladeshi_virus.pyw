import tkinter as tk
import webbrowser
from tkinter import messagebox

root = tk.Tk()
root.wm_attributes("-topmost", 1)
root.withdraw()
while True:
    name = messagebox.askyesnocancel(icon= "error", title = "Virus Alert!", message = "Hi, I am an Bangladeshi Virus but because of poor technology in my country unfortunately I am not able to harm your computer. Please be so kind to delete one of your important files yourself and then forward me to other ones, Many thanks for your cooperation! Best regards, Bangladeshi virus")
    if name:
        for _ in range(100):
            webbrowser.open("https://www.youtube.com/watch?v=1TO48Cnl66w")
    else:
        while True:
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

root.destroy()