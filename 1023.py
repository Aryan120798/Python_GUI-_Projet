from tkinter import *

#This frame has two buttons and two labels - Customers and Staff Members
class B:
    def __init__(self, parent):
        self.myParent = parent
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()

        def button2Click(self):
            print
            "button2Click event handler"
            self.myParent.destroy()

        window_width = 1000
        window_height = 600

        screen_height = parent.winfo_screenheight()
        screen_width = parent.winfo_screenwidth()

        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)

        parent.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coordinate, y_coordinate))

        frame1 = Frame(parent, height=1000, width=600)
        frame1.pack(fill=BOTH)
        customerPhoto = PhotoImage(file="boy.png")
        staffPhoto = PhotoImage(file="boss.png")
        self.customerButton = Button(self.myContainer1, image=customerPhoto, command=button2Click)
        self.customerButton.focus_force()
        self.customerButton.place(x=152, y=125)
        staffButton = Button(frame1, image=staffPhoto)
        staffButton.place(x=550, y=125)

        customerLabel = Label(frame1, text="   CUSTOMER", font=("Poiret One", 24), fg='#34495E')
        staffLabel = Label(frame1, text="         STAFF", font=("Poiret One", 24), fg='#34495E')

        customerLabel.place(x=152, y=405)
        staffLabel.place(x=550, y=405)




root = Tk()
b=B(root)
root.mainloop()

