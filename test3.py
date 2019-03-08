from tkinter import *
from test1 import *
class MyApp:
    def __init__(self, root):
        self.myParent = root
        self.myContainer1 = Frame(root)
        self.myContainer1.pack()
        self.myParent.geometry("500x500")

        self.button1 = Button(self.myContainer1,text="test3",command=self.button1Click)
        self.button1.pack(side=LEFT)
        #self.button1.focus_force()

        self.button2 = Button(self.myContainer1,text="Cancel",command=self.button2Click)
        self.button2.pack(side=RIGHT)

    def button1Click(self):
        self.myParent.destroy()
        MyApp1()



    def button2Click(self):
        print
        "button2Click event handler"
        self.myParent.destroy()


root = Tk()
MyApp(root)
root.mainloop()