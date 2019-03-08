from tkinter import *
from tkinter import messagebox

root = Tk()
root.withdraw()

# message box display
messagebox.showerror("Error", "Error message")
messagebox.showwarning("Warning", "Warning message")
messagebox.showinfo("Information", "Informative message")

root.mainloop()