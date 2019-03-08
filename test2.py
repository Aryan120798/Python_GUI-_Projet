from tkinter import *


class cancelfood():
    def canfood(self):
        root3 = Tk()
        root3.title("Staff")
        window_width = 1000
        window_height = 600

        screen_height = root3.winfo_screenheight()
        screen_width = root3.winfo_screenwidth()

        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)

        root3.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coordinate, y_coordinate))

        frame4 = Frame(root3, width=1000, height=1000)
        frame4.pack(fill=BOTH)

        label_1 = Label(frame4, text="Username", font=("Poiret One", 24), fg='#34495E')
        label_2 = Label(frame4, text="Password", font=("Poiret One", 24), fg='#34495E')

        entry_1 = Entry(frame4)
        entry_2 = Entry(frame4)

        label_1.place(x=10,y=60)
        label_2.grid(row=1, sticky=E)
        entry_1.grid(row=2, column=4)
        entry_2.grid(row=1, column=1)

        checkbox = Checkbutton(frame4, text="Keep me logged in")
        checkbox.grid(columnspan=2)

        def t2():
            root.destroy()
            B.welcomeWindow(self)

        root3.mainloop()

class Stafflogin():
    def Staffwin(self):
        root2 = Tk()
        root2.title("Staff")
        window_width = 1000
        window_height = 600

        screen_height = root2.winfo_screenheight()
        screen_width = root2.winfo_screenwidth()

        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)

        root2.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coordinate, y_coordinate))

        frame3 = Frame(root2, width=1000, height=1000)
        frame3.pack(fill=BOTH)

        label_1 = Label(frame3, text="Username", font=("Poiret One", 24), fg='#34495E')
        label_2 = Label(frame3, text="Password", font=("Poiret One", 24), fg='#34495E')

        entry_1 = Entry(frame3)
        entry_2 = Entry(frame3)

        label_1.place(x=10,y=60)
        label_2.grid(row=1, sticky=E)
        entry_1.grid(row=2, column=4)
        entry_2.grid(row=1, column=1)

        checkbox = Checkbutton(frame3, text="Keep me logged in")
        checkbox.grid(columnspan=2)

        def t2():
            root2.destroy()
            B.welcomeWindow(self)

        root2.mainloop()

class A():
    def customerwindow(self):
        root1 = Tk()
        root1.title("Customer Choice")



        window_width = 1000
        window_height = 600

        screen_height = root1.winfo_screenheight()
        screen_width = root1.winfo_screenwidth()

        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)

        root1.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coordinate, y_coordinate))

        frame2 = Frame(root1, height=600, width=600)
        frame2.pack(fill=BOTH)

        Order = PhotoImage(file="fast-food.png")
        Cancel = PhotoImage(file="delete.png")

        def t2():
            root1.destroy()
            B.welcomeWindow(self)

        OrderButton = Button(frame2, image=Order)
        OrderButton.place(x=152, y=125)
        button3 = Button(frame2,text="BAck",command=t2,width=10, height=5)
        button3.place(x=430, y=400)

        def t3():
            root1.destroy()
            cancelfood.canfood(self)

        CancelButton = Button(frame2, image=Cancel,command=t3)
        CancelButton.place(x=550, y=125)

        OrderLabel = Label(frame2, text="       ORDER", font=("Poiret One", 24), fg='#34495E')
        CancelLabel = Label(frame2, text=" CANCEL ORDER", font=("Poiret One", 24), fg='#34495E')

        OrderLabel.place(x=152, y=405)
        CancelLabel.place(x=550, y=405)

        root1.mainloop()



class B():
    def welcomeWindow(self):
        root = Tk()
        root.title("Welcome")

        window_width = 1000
        window_height = 600

        screen_height = root.winfo_screenheight()
        screen_width = root.winfo_screenwidth()

        x_coordinate = (screen_width/2) - (window_width/2)
        y_coordinate = (screen_height/2) - (window_height/2)

        root.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coordinate, y_coordinate))

        frame1 = Frame(root, height=1000, width=600)
        frame1.pack(fill=BOTH)

        customerPhoto = PhotoImage(file="boy.png")
        staffPhoto = PhotoImage(file="boss.png")
        def t1():
            root.destroy()
            A.customerwindow(self)



        customerButton = Button(frame1, image=customerPhoto, command=t1)

        customerButton.place(x=152, y=125)

        def ToStaff():
            root.destroy()
            Stafflogin.Staffwin(self)
        staffButton = Button(frame1, image=staffPhoto,command=ToStaff)
        staffButton.place(x=550, y=125)


        customerLabel = Label(frame1, text="   CUSTOMER", font=("Poiret One", 24), fg='#34495E')
        staffLabel = Label(frame1, text="         STAFF", font=("Poiret One", 24), fg='#34495E')

        customerLabel.place(x=152, y=405)
        staffLabel.place(x=550, y=405)


        root.mainloop()



b=B()
b.welcomeWindow()





