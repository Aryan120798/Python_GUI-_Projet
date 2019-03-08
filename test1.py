from tkinter import *
from test3 import *
class MyApp1:
    def __init__(self, root1):
        self.myParent = root1
        self.myContainer1 = Frame(root1)
        self.myContainer1.pack()
        self.myParent.geometry("500x500")

        self.button1 = Button(self.myContainer1,text="test1",command=self.button1Click)
        self.button1.pack(side=LEFT)
        #self.button1.focus_force()

        self.button2 = Button(self.myContainer1,text="Cancel",command=self.button2Click)
        self.button2.pack(side=RIGHT)

    def button1Click(self):
        self.myParent.destroy()
        MyApp(root)


    def button2Click(self):
        print
        "button2Click event handler"
        self.myParent.destroy()


root1 = Tk()
MyApp1(root1)
root.mainloop()