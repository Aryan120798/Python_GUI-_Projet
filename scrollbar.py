from tkinter import *
import sqlite3

root = Tk()
root.geometry("500x500")
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT,expand=FALSE)


mylist = Listbox(root, yscrollcommand = scrollbar.set )



mylist.pack( side = LEFT,expand=FALSE )
scrollbar.config( command = mylist.yview )
window_width = 1000
window_height = 600

screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)
mylist.config(width=90)

root.mainloop()