from tkinter import *
from tkinter import messagebox
import random
import sqlite3

print("start")
class testframe:
    global orderid
    global tcoffee, tfrankie, tfrenchfries, tburger, ticecream, tketchup, tpizza, tsandwich, grandtotal
    def testframefun(self):
        root22 = Tk()
        root22.title("Billing")
        root22.geometry("400x300")
        f1 = Frame(root22, height='900', width='400')

        orderidl= Label(f1, text='Order id :', font=("Poiret One", 16), fg='#000000')
        orderidl.place(x=10, y=27)

        orderidno = Label(f1, font=("Poiret One", 16), fg='#000000')
        orderidno.place(x=124, y=27)
        l1 = Label(f1, text='Name :', font=("Poiret One", 16), fg='#000000')
        l1.place(x=10, y=60)
        l2 = Label(f1, text='Phone No :', font=("Poiret One", 16), fg='#000000')
        l2.place(x=10, y=100)
        l3 = Label(f1, text='Address :', font=("Poiret One", 16), fg='#000000')
        l3.place(x=10, y=140)
        l4 = Label(f1, text='Payment Type :', font=("Poiret One", 16), fg='#000000')
        l4.place(x=10, y=180)
        name = StringVar()
        e1 = Entry(f1, width=40,textvariable=name)
        e1.place(x=130, y=67)
        pno=StringVar()
        e2 = Entry(f1, width=40,textvariable=pno)
        e2.place(x=130, y=107)
        addrs=StringVar()
        e3 = Entry(f1, width=40,textvariable=addrs)
        e3.place(x=130, y=145)
        v0 = IntVar()
        l5 = Label(f1, font=("Poiret One", 10), fg='#000000')
        l5.place(x=240, y=186)
        orderidno.config(text=orderid)

        def on_enter(self):
            l5.configure(text="only cod available")

        def on_leave(self):
            l5.configure(text="")

        r1 = Radiobutton(f1, text='COD', variable=v0, value=0)
        r1.bind("<Enter>", on_enter)
        r1.bind("<Leave>", on_leave)
        def t0():
            root22.destroy()
            Orderclass.ordermethod(self)

        def nextwin():
            x1=name.get()
            x2=pno.get()
            x3=addrs.get()
            if (x1=='' or x2=='' or x3==''):
                messagebox.showerror("Error", "Enter complete details!")
            else:
                conn = sqlite3.connect('Main.db')
                c = conn.cursor()
                x4=int(x2)
                print("b4customer part")
                str1=("INSERT INTO CUSTOMER(Order_id, Name, Phone_no, Address) VALUES('%d', '%s', '%d', '%s')"%(orderid,x1,x4,x3))
                c.execute(str1)
                conn.commit()
                conn.close()
                print("a4 customer part")
                if counters.pizzacount!=0:

                    conn = sqlite3.connect('Main.db')
                    c = conn.cursor()
                    str2 = ("INSERT INTO ORDER_DETAILS(Order_id, Item_name, Cost, Count, T_cost) VALUES('%d', '%s', '%d', '%d','%d')" % (orderid,'Pizza',250,counters.pizzacount,tpizza))
                    c.execute(str2)
                    conn.commit()
                    conn.close()

                if counters.coffeecount!=0:

                    conn = sqlite3.connect('Main.db')
                    c = conn.cursor()
                    str2 = ("INSERT INTO ORDER_DETAILS(Order_id, Item_name, Cost, Count, T_cost) VALUES('%d', '%s', '%d', '%d','%d')" % (orderid,'Coffee',40,counters.coffeecount,tcoffee))
                    c.execute(str2)
                    conn.commit()
                    conn.close()

                if counters.frenchfriescount!=0:

                    conn = sqlite3.connect('Main.db')
                    c = conn.cursor()
                    str2 = ("INSERT INTO ORDER_DETAILS(Order_id, Item_name, Cost, Count, T_cost) VALUES('%d', '%s', '%d', '%d','%d')" % (orderid,'French-Fries',50,counters.frenchfriescount,tfrenchfries))
                    c.execute(str2)
                    conn.commit()
                    conn.close()

                if counters.frankiecount!=0:

                    conn = sqlite3.connect('Main.db')
                    c = conn.cursor()
                    str2 = ("INSERT INTO ORDER_DETAILS(Order_id, Item_name, Cost, Count, T_cost) VALUES('%d', '%s', '%d', '%d','%d')" % (orderid,'Frankie',50,counters.frankiecount,tfrankie))
                    c.execute(str2)
                    conn.commit()
                    conn.close()

                if counters.sandwichcount!=0:

                    conn = sqlite3.connect('Main.db')
                    c = conn.cursor()
                    str2 = ("INSERT INTO ORDER_DETAILS(Order_id, Item_name, Cost, Count, T_cost) VALUES('%d', '%s', '%d', '%d','%d')" % (orderid,'Sandwich',50,counters.sandwichcount,tsandwich))
                    c.execute(str2)
                    conn.commit()
                    conn.close()

                if counters.icecreamcount!=0:

                    conn = sqlite3.connect('Main.db')
                    c = conn.cursor()
                    str2 = ("INSERT INTO ORDER_DETAILS(Order_id, Item_name, Cost, Count, T_cost) VALUES('%d', '%s', '%d', '%d','%d')" % (orderid,'Ice-Cream',30,counters.icecreamcount,ticecream))
                    c.execute(str2)
                    conn.commit()
                    conn.close()

                if counters.ketchupcount!=0:

                    conn = sqlite3.connect('Main.db')
                    c = conn.cursor()
                    str2 = ("INSERT INTO ORDER_DETAILS(Order_id, Item_name, Cost, Count, T_cost) VALUES('%d', '%s', '%d', '%d','%d')" % (orderid,'Ketchup',5,counters.ketchupcount,tketchup))
                    c.execute(str2)
                    conn.commit()
                    conn.close()


                if counters.burgercount!=0:

                    conn = sqlite3.connect('Main.db')
                    c = conn.cursor()
                    str2 = ("INSERT INTO ORDER_DETAILS(Order_id, Item_name, Cost, Count, T_cost) VALUES('%d', '%s', '%d', '%d','%d')" % (orderid,'Burger',100,counters.burgercount,tburger))
                    c.execute(str2)



                    conn.commit()
                    conn.close()

        next1 = Button(f1, text='Next', font=("Poiret One", 16), fg='#000000',command=nextwin)
        next1.place(x=317, y=240)
        back = Button(f1, text='Back', font=("Poiret One", 16), fg='#000000',command=t0)
        back.place(x=10, y=240)

        r1.place(x=170, y=184)

        f1.pack()
        root22.mainloop()



class counters:

    pizzacount=0
    coffeecount=0
    frankiecount=0
    frenchfriescount=0
    burgercount=0
    icecreamcount=0
    ketchupcount=0
    sandwichcount=0


    @classmethod
    def pizzapluscounter(cls):
        cls.pizzacount+=1
        return cls.pizzacount

    @classmethod
    def pizzaminuscounter(cls):

        cls.pizzacount-=1
        if cls.pizzacount < 0:
            cls.pizzacount=0
        return cls.pizzacount

    @classmethod
    def coffeepluscounter(cls):
        cls.coffeecount+=1
        return cls.coffeecount

    @classmethod
    def coffeeminuscounter(cls):
        cls.coffeecount-=1
        if cls.coffeecount < 0:
            cls.coffeecount=0
        return cls.coffeecount

    @classmethod
    def frankiepluscounter(cls):
        cls.frankiecount+=1
        return cls.frankiecount

    @classmethod
    def frankieminuscounter(cls):
        cls.frankiecount-=1
        if cls.frankiecount < 0:
            cls.frankiecount=0
        return cls.frankiecount

    @classmethod
    def frenchfriespluscounter(cls):
        cls.frenchfriescount+=1
        return cls.frenchfriescount

    @classmethod
    def frenchfriesminuscounter(cls):
        cls.frenchfriescount-=1
        if cls.frenchfriescount < 0:
            cls.frenchfriescount=0
        return cls.frenchfriescount

    @classmethod
    def burgerpluscounter(cls):
        cls.burgercount+=1
        return cls.burgercount

    @classmethod
    def burgerminuscounter(cls):
        cls.burgercount-=1
        if cls.burgercount < 0:
            cls.burgercount=0
        return cls.burgercount

    @classmethod
    def icecreampluscounter(cls):
        cls.icecreamcount+=1
        return cls.icecreamcount

    @classmethod
    def icecreamminuscounter(cls):
        cls.icecreamcount-=1
        if cls.icecreamcount < 0:
            cls.icecreamcount=0
        return cls.icecreamcount

    @classmethod
    def ketchuppluscounter(cls):
        cls.ketchupcount+=1
        return cls.ketchupcount

    @classmethod
    def ketchupminuscounter(cls):
        cls.ketchupcount-=1
        if cls.ketchupcount < 0:
            cls.ketchupcount=0
        return cls.ketchupcount

    @classmethod
    def sandwichpluscounter(cls):
        cls.sandwichcount+=1
        return cls.sandwichcount

    @classmethod
    def sandwichminuscounter(cls):
        cls.sandwichcount-=1
        if cls.sandwichcount < 0:
            cls.sandwichcount=0
        return cls.sandwichcount

class Orderclass():
    global tcoffee
    tcoffee=0
    global tfrankie
    tfrankie=0
    global tfrenchfries
    tfrenchfries=0
    global tburger
    tburger=0
    global ticecream
    ticecream=0
    global tketchup
    tketchup=0
    global tpizza
    tpizza=0
    global tsandwich
    tsandwich=0

    global grandtotal
    grandtotal=0

    global orderid

    def ordermethod(self):
        global tcoffee, tfrankie, tfrenchfries, tburger, ticecream, tketchup, tpizza, tsandwich, grandtotal
        # This class has order menu
        root7 = Tk()
        print("start of order")
        root7.title("Order")
        root7.resizable(width=FALSE,height=FALSE)

        window_width = 1200
        window_height = 760

        screen_height = root7.winfo_screenheight()
        screen_width = root7.winfo_screenwidth()

        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)

        root7.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coordinate, y_coordinate))

        frame8 = Frame(root7, height=1200, width=760)
        frame8.pack(fill=BOTH)

        coffee = PhotoImage(file="coffee.png")
        burrito = PhotoImage(file="burrito.png")
        frenchfries = PhotoImage(file="french-fries.png")
        hamburger = PhotoImage(file="hamburger.png")
        icecream = PhotoImage(file="ice-cream.png")
        ketchup = PhotoImage(file="ketchup.png")
        pizza = PhotoImage(file="pizza.png")
        sandwich = PhotoImage(file="sandwich.png")
        back = PhotoImage(file="back.png")

        coffeelabel = Label(frame8, image=coffee)
        burritolabel = Label(frame8, image=burrito)
        frenchfrieslabel = Label(frame8, image=frenchfries)
        hamburgerlabel = Label(frame8, image=hamburger)
        icecreamlabel = Label(frame8, image=icecream)
        ketchuplabel = Label(frame8, image=ketchup)
        pizzalabel = Label(frame8, image=pizza)
        sandwichlabel = Label(frame8, image=sandwich)

        item = Label(frame8, text='Count',font=("Poiret One", 10), fg='#000000')
        item.place(x=889, y=0)

        bhaav = Label(frame8, text='Total', font=("Poiret One", 10), fg='#000000')
        bhaav.place(x=1087, y=0)

        grandtotal= Label(frame8,text="Grand Total =",font=("Poiret One", 29), fg='#000000')
        grandtotal.place(x=600,y=670)


        grandtotal1 = Label(frame8,font=("Poiret One", 29), fg='#000000')
        grandtotal1.place(x=880, y=670)
        grandtotal = tcoffee + tfrankie + tfrenchfries + tburger + ticecream + tketchup + tpizza + tsandwich
        print('GD',grandtotal)
        grandtotal1.config(text=grandtotal)

        orderid1 = Label(frame8,text="Order id:", font=("Poiret One", 29), fg='#000000')
        orderid1.place(x=130, y=670)
        orderidno = Label(frame8, font=("Poiret One", 29), fg='#000000')
        orderidno.place(x=290, y=670)
        global orderid
        a = 10000000
        b = 99999999
        orderid=random.randint(a, b)

        orderidno.config(text=orderid)

        def toCustomerChoice():
            root7.destroy()
            A.customerwindow(self)

        coffeel= Label(frame8,font=("Poiret One", 17), fg='#000000')
        coffeel.place(x=889, y=30)
        coffeel.config(text=counters.coffeecount)
        frankiel = Label(frame8, font=("Poiret One", 17), fg='#000000')
        frankiel.place(x=889, y=113)
        frankiel.config(text=counters.frankiecount)
        frenchl = Label(frame8, font=("Poiret One", 17), fg='#000000')
        frenchl.place(x=889, y=196)
        frenchl.config(text=counters.frenchfriescount)
        bugl = Label(frame8, font=("Poiret One", 17), fg='#000000')
        bugl.place(x=889, y=279)
        bugl.config(text=counters.burgercount)
        icecreaml = Label(frame8, font=("Poiret One", 17), fg='#000000')
        icecreaml.place(x=889, y=362)
        icecreaml.config(text=counters.icecreamcount)
        ketupl = Label(frame8, font=("Poiret One", 17), fg='#000000')
        ketupl.place(x=889, y=445)
        ketupl.config(text=counters.ketchupcount)
        pizzal = Label(frame8, font=("Poiret One", 17), fg='#000000')
        pizzal.place(x=889, y=528)
        pizzal.config(text=counters.pizzacount)
        sandwichl = Label(frame8, font=("Poiret One", 17), fg='#000000')
        sandwichl.place(x=889, y=611)
        sandwichl.config(text=counters.sandwichcount)
        coffeelabelpricetotal = Label(frame8, font=("Poiret One", 17), fg='#000000')
        coffeelabelpricetotal.config(text=tcoffee)
        burritolabelpricetotal = Label(frame8, font=("Poiret One", 17), fg='#000000')
        burritolabelpricetotal.config(text=tfrankie)
        frenchfrieslabelpricetotal = Label(frame8, font=("Poiret One", 17), fg='#000000')
        frenchfrieslabelpricetotal.config(text=tfrenchfries)
        hamburgerlabelpricetotal = Label(frame8, font=("Poiret One", 17), fg='#000000')
        hamburgerlabelpricetotal.config(text=tburger)
        icecreamlabelpricetotal = Label(frame8, font=("Poiret One", 17), fg='#000000')
        icecreamlabelpricetotal.config(text=ticecream)
        ketchuplabelpricetotal = Label(frame8, font=("Poiret One", 17), fg='#000000')
        ketchuplabelpricetotal.config(text=tketchup)
        pizzalabelpricetotal = Label(frame8, font=("Poiret One", 17), fg='#000000')
        pizzalabelpricetotal.config(text=tpizza)
        sandwichlabelpricetotal = Label(frame8, font=("Poiret One", 17), fg='#000000')
        sandwichlabelpricetotal.config(text=tsandwich)

        coffeelabelpricetotal.place(x=1087,y=30)
        burritolabelpricetotal.place(x=1087,y=113)
        frenchfrieslabelpricetotal.place(x=1087,y=196)
        hamburgerlabelpricetotal.place(x=1087,y=276)
        icecreamlabelpricetotal.place(x=1087,y=362)
        ketchuplabelpricetotal.place(x=1087,y=445)
        pizzalabelpricetotal.place(x=1087,y=528)
        sandwichlabelpricetotal.place(x=1087,y=611)


        def coffeeclickp():
            global tcoffee,tfrankie,tfrenchfries,tburger,ticecream,tketchup,tpizza,tsandwich,grandtotal
            clickcoffee=counters.coffeepluscounter()
            coffeel.config(text=clickcoffee)
            tcoffee=40*clickcoffee
            coffeelabelpricetotal.config(text=tcoffee)
            grandtotal=tcoffee+tfrankie+tfrenchfries+tburger+ticecream+tketchup+tpizza+tsandwich
            grandtotal1.config(text=grandtotal)

        def coffeeclickm():
            global tcoffee, tfrankie, tfrenchfries, tburger, ticecream, tketchup, tpizza, tsandwich, grandtotal
            clickcoffee=counters.coffeeminuscounter()
            tcoffee = 40 * clickcoffee
            coffeel.config(text=clickcoffee)
            coffeelabelpricetotal.config(text=tcoffee)
            grandtotal = tcoffee + tfrankie + tfrenchfries + tburger + ticecream + tketchup + tpizza + tsandwich
            grandtotal1.config(text=grandtotal)

        def frankieclickp():
            global tcoffee, tfrankie, tfrenchfries, tburger, ticecream, tketchup, tpizza, tsandwich, grandtotal
            clickfrankie = counters.frankiepluscounter()
            tfrankie = 50 * clickfrankie
            frankiel.config(text=clickfrankie)
            burritolabelpricetotal.config(text=tfrankie)
            grandtotal = tcoffee + tfrankie + tfrenchfries + tburger + ticecream + tketchup + tpizza + tsandwich
            grandtotal1.config(text=grandtotal)

        def frankieclickm():
            global tcoffee, tfrankie, tfrenchfries, tburger, ticecream, tketchup, tpizza, tsandwich, grandtotal
            clickfrankie = counters.frankieminuscounter()
            tfrankie = 50 * clickfrankie
            frankiel.config(text=clickfrankie)
            burritolabelpricetotal.config(text=tfrankie)
            grandtotal = tcoffee + tfrankie + tfrenchfries + tburger + ticecream + tketchup + tpizza + tsandwich
            grandtotal1.config(text=grandtotal)


        def frenchfriesp():
            global tcoffee, tfrankie, tfrenchfries, tburger, ticecream, tketchup, tpizza, tsandwich, grandtotal
            clickfrench = counters.frenchfriespluscounter()
            tfrenchfries = 50 * clickfrench
            frenchl.config(text=clickfrench)
            frenchfrieslabelpricetotal.config(text=tfrenchfries)
            grandtotal = tcoffee + tfrankie + tfrenchfries + tburger + ticecream + tketchup + tpizza + tsandwich
            grandtotal1.config(text=grandtotal)

        def frenchfriesm():
            global tcoffee, tfrankie, tfrenchfries, tburger, ticecream, tketchup, tpizza, tsandwich, grandtotal
            clickfrench = counters.frenchfriesminuscounter()
            tfrenchfries = 50 * clickfrench
            frenchl.config(text=clickfrench)
            frenchfrieslabelpricetotal.config(text=tfrenchfries)
            grandtotal = tcoffee + tfrankie + tfrenchfries + tburger + ticecream + tketchup + tpizza + tsandwich
            grandtotal1.config(text=grandtotal)


        def burgerp():
            global tcoffee, tfrankie, tfrenchfries, tburger, ticecream, tketchup, tpizza, tsandwich, grandtotal
            clickburger = counters.burgerpluscounter()
            tburger=100*clickburger
            bugl.config(text=clickburger)
            hamburgerlabelpricetotal.config(text=tburger)
            grandtotal = tcoffee + tfrankie + tfrenchfries + tburger + ticecream + tketchup + tpizza + tsandwich
            grandtotal1.config(text=grandtotal)

        def burgerm():
            global tcoffee, tfrankie, tfrenchfries, tburger, ticecream, tketchup, tpizza, tsandwich, grandtotal
            clickburger = counters.burgerminuscounter()
            tburger=100*clickburger
            bugl.config(text=clickburger)
            hamburgerlabelpricetotal.config(text=tburger)
            grandtotal = tcoffee + tfrankie + tfrenchfries + tburger + ticecream + tketchup + tpizza + tsandwich
            grandtotal1.config(text=grandtotal)


        def icecreamp():
            global tcoffee, tfrankie, tfrenchfries, tburger, ticecream, tketchup, tpizza, tsandwich, grandtotal
            clickicecream = counters.icecreampluscounter()
            ticecream=30*clickicecream
            icecreaml.config(text=clickicecream)
            icecreamlabelpricetotal.config(text=ticecream)
            grandtotal = tcoffee + tfrankie + tfrenchfries + tburger + ticecream + tketchup + tpizza + tsandwich
            grandtotal1.config(text=grandtotal)

        def icecreamm():
            global tcoffee, tfrankie, tfrenchfries, tburger, ticecream, tketchup, tpizza, tsandwich, grandtotal
            clickicream = counters.icecreamminuscounter()
            ticecream = 30 * clickicream
            icecreaml.config(text=clickicream)
            icecreamlabelpricetotal.config(text=ticecream)
            grandtotal = tcoffee + tfrankie + tfrenchfries + tburger + ticecream + tketchup + tpizza + tsandwich
            grandtotal1.config(text=grandtotal)

        def ketchupp():
            global tcoffee, tfrankie, tfrenchfries, tburger, ticecream, tketchup, tpizza, tsandwich, grandtotal
            clickketchup = counters.ketchuppluscounter()
            tketchup=5*clickketchup
            ketupl.config(text=clickketchup)
            ketchuplabelpricetotal.config(text=tketchup)
            grandtotal = tcoffee + tfrankie + tfrenchfries + tburger + ticecream + tketchup + tpizza + tsandwich
            grandtotal1.config(text=grandtotal)

        def ketchupm():
            global tcoffee, tfrankie, tfrenchfries, tburger, ticecream, tketchup, tpizza, tsandwich, grandtotal
            clickketchup = counters.ketchupminuscounter()
            tketchup = 5 * clickketchup
            ketupl.config(text=clickketchup)
            ketchuplabelpricetotal.config(text=tketchup)
            grandtotal = tcoffee + tfrankie + tfrenchfries + tburger + ticecream + tketchup + tpizza + tsandwich
            grandtotal1.config(text=grandtotal)

        def pizzap():
            global tcoffee, tfrankie, tfrenchfries, tburger, ticecream, tketchup, tpizza, tsandwich, grandtotal
            clickpizza = counters.pizzapluscounter()
            tpizza=250*clickpizza
            pizzal.config(text=clickpizza)
            pizzalabelpricetotal.config(text=tpizza)
            grandtotal = tcoffee + tfrankie + tfrenchfries + tburger + ticecream + tketchup + tpizza + tsandwich
            grandtotal1.config(text=grandtotal)

        def pizzam():
            global tcoffee, tfrankie, tfrenchfries, tburger, ticecream, tketchup, tpizza, tsandwich, grandtotal
            clickpizza = counters.pizzaminuscounter()
            tpizza = 250 * clickpizza
            pizzal.config(text=clickpizza)
            pizzalabelpricetotal.config(text=tpizza)
            grandtotal = tcoffee + tfrankie + tfrenchfries + tburger + ticecream + tketchup + tpizza + tsandwich
            grandtotal1.config(text=grandtotal)

        def sandwichp():
            global tcoffee, tfrankie, tfrenchfries, tburger, ticecream, tketchup, tpizza, tsandwich, grandtotal
            clicksand = counters.sandwichpluscounter()
            tsandwich=50*clicksand
            sandwichl.config(text=clicksand)
            sandwichlabelpricetotal.config(text=tsandwich)
            grandtotal = tcoffee + tfrankie + tfrenchfries + tburger + ticecream + tketchup + tpizza + tsandwich
            grandtotal1.config(text=grandtotal)


        def sandwichm():
            global tcoffee, tfrankie, tfrenchfries, tburger, ticecream, tketchup, tpizza, tsandwich, grandtotal
            clicksand = counters.sandwichminuscounter()
            tsandwich = 50 * clicksand
            sandwichl.config(text=clicksand)
            sandwichlabelpricetotal.config(text=tsandwich)
            grandtotal = tcoffee + tfrankie + tfrenchfries + tburger + ticecream + tketchup + tpizza + tsandwich
            grandtotal1.config(text=grandtotal)


        backbutton = Button(frame8, image=back, relief=FLAT, command=toCustomerChoice)





        coffeelabel.grid(row=0, column=0, padx=30, pady=10)
        burritolabel.grid(row=1, column=0, padx=30, pady=7)
        frenchfrieslabel.grid(row=2, column=0, padx=10, pady=7)
        hamburgerlabel.grid(row=3, column=0, padx=10, pady=7)
        icecreamlabel.grid(row=4, column=0, padx=10, pady=7)
        ketchuplabel.grid(row=5, column=0, padx=10, pady=7)
        pizzalabel.grid(row=6, column=0, padx=10, pady=7)
        sandwichlabel.grid(row=7, column=0, padx=10, pady=4)
        backbutton.grid(row=8, column=0, padx=10, pady=7)

        coffeelabel2 = Label(frame8, text='COFFEE', font=("Poiret One", 14), fg='#000000')
        burritolabel2 = Label(frame8, text='FRANKIE', font=("Poiret One", 14), fg='#000000')
        frenchfrieslabel2 = Label(frame8, text='FRENCH-FRIES', font=("Poiret One", 14), fg='#000000')
        hamburgerlabel2 = Label(frame8, text='BURGER', font=("Poiret One", 14), fg='#000000')
        icecreamlabel2 = Label(frame8, text='ICE-CREAM', font=("Poiret One", 14), fg='#000000')
        ketchuplabel2 = Label(frame8, text='KETCHUP', font=("Poiret One", 14), fg='#000000')
        pizzalabel2 = Label(frame8, text='PIZZA', font=("Poiret One", 14), fg='#000000')
        sandwichlabel2 = Label(frame8, text='SANDWICH', font=("Poiret One", 14), fg='#000000')

        coffeelabel2.grid(row=0, column=1, padx=100, pady=10, sticky=EW)
        burritolabel2.grid(row=1, column=1, padx=100, pady=7, sticky=EW)
        frenchfrieslabel2.grid(row=2, column=1, padx=100, pady=7, sticky=EW)
        hamburgerlabel2.grid(row=3, column=1, padx=100, pady=7, sticky=EW)
        icecreamlabel2.grid(row=4, column=1, padx=100, pady=7, sticky=EW)
        ketchuplabel2.grid(row=5, column=1, padx=100, pady=7, sticky=EW)
        pizzalabel2.grid(row=6, column=1, padx=100, pady=7, sticky=EW)
        sandwichlabel2.grid(row=7, column=1, padx=100, pady=4, sticky=EW)

        coffeelabelprice = Label(frame8, text='40₹', font=("Poiret One", 14), fg='#000000')
        burritolabelprice = Label(frame8, text='50₹', font=("Poiret One", 14), fg='#000000')
        frenchfrieslabelprice = Label(frame8, text='50₹', font=("Poiret One", 14), fg='#000000')
        hamburgerlabelprice = Label(frame8, text='100₹', font=("Poiret One", 14), fg='#000000')
        icecreamlabelprice = Label(frame8, text='30₹', font=("Poiret One", 14), fg='#000000')
        ketchuplabelprice = Label(frame8, text='5₹', font=("Poiret One", 14), fg='#000000')
        pizzalabelprice = Label(frame8, text='250₹', font=("Poiret One", 14), fg='#000000')
        sandwichlabelprice = Label(frame8, text='50₹', font=("Poiret One", 14), fg='#000000')

        coffeelabelprice.grid(row=0, column=2, padx=100, pady=10, sticky=EW)
        burritolabelprice.grid(row=1, column=2, padx=100, pady=7, sticky=EW)
        frenchfrieslabelprice.grid(row=2, column=2, padx=100, pady=7, sticky=EW)
        hamburgerlabelprice.grid(row=3, column=2, padx=100, pady=7, sticky=EW)
        icecreamlabelprice.grid(row=4, column=2, padx=100, pady=7, sticky=EW)
        ketchuplabelprice.grid(row=5, column=2, padx=100, pady=7, sticky=EW)
        pizzalabelprice.grid(row=6, column=2, padx=100, pady=7, sticky=EW)
        sandwichlabelprice.grid(row=7, column=2, padx=100, pady=4, sticky=EW)

        add_to_cart = PhotoImage(file="add_cart.png")
        remove_to_cart = PhotoImage(file="remove_cart.png")

        tadd_to_cart = add_to_cart.subsample(2, 2)
        tremove_to_cart = remove_to_cart.subsample(2, 2)

        add_to_cart1 = Button(frame8, image=tadd_to_cart, relief=FLAT,command=coffeeclickp)
        add_to_cart2 = Button(frame8, image=tadd_to_cart, relief=FLAT,command=frankieclickp)
        add_to_cart3 = Button(frame8, image=tadd_to_cart, relief=FLAT,command=frenchfriesp)
        add_to_cart4 = Button(frame8, image=tadd_to_cart, relief=FLAT,command=burgerp)
        add_to_cart5 = Button(frame8, image=tadd_to_cart, relief=FLAT,command=icecreamp)
        add_to_cart6 = Button(frame8, image=tadd_to_cart, relief=FLAT,command=ketchupp)
        add_to_cart7 = Button(frame8, image=tadd_to_cart, relief=FLAT,command=pizzap)
        add_to_cart8 = Button(frame8, image=tadd_to_cart, relief=FLAT,command=sandwichp)
        # TODO link add to cart buttons to database

        remove_to_cart1 = Button(frame8, image=tremove_to_cart, relief=FLAT,command=coffeeclickm)
        remove_to_cart2 = Button(frame8, image=tremove_to_cart, relief=FLAT,command=frankieclickm)
        remove_to_cart3 = Button(frame8, image=tremove_to_cart, relief=FLAT,command=frenchfriesm)
        remove_to_cart4 = Button(frame8, image=tremove_to_cart, relief=FLAT,command=burgerm)
        remove_to_cart5 = Button(frame8, image=tremove_to_cart, relief=FLAT,command=icecreamm)
        remove_to_cart6 = Button(frame8, image=tremove_to_cart, relief=FLAT,command=ketchupm)
        remove_to_cart7 = Button(frame8, image=tremove_to_cart, relief=FLAT,command=pizzam)
        remove_to_cart8 = Button(frame8, image=tremove_to_cart, relief=FLAT,command=sandwichm)
        # TODO link remove to cart buttons to database

        add_to_cart1.grid(row=0, column=3, padx=70, pady=10, sticky=EW)
        add_to_cart2.grid(row=1, column=3, padx=50, pady=10, sticky=EW)
        add_to_cart3.grid(row=2, column=3, padx=50, pady=10, sticky=EW)
        add_to_cart4.grid(row=3, column=3, padx=50, pady=10, sticky=EW)
        add_to_cart5.grid(row=4, column=3, padx=50, pady=10, sticky=EW)
        add_to_cart6.grid(row=5, column=3, padx=50, pady=10, sticky=EW)
        add_to_cart7.grid(row=6, column=3, padx=50, pady=10, sticky=EW)
        add_to_cart8.grid(row=7, column=3, padx=50, pady=10, sticky=EW)

        remove_to_cart1.grid(row=0, column=4, padx=70, pady=10, sticky=EW)
        remove_to_cart2.grid(row=1, column=4, padx=50, pady=10, sticky=EW)
        remove_to_cart3.grid(row=2, column=4, padx=50, pady=10, sticky=EW)
        remove_to_cart4.grid(row=3, column=4, padx=50, pady=10, sticky=EW)
        remove_to_cart5.grid(row=4, column=4, padx=50, pady=10, sticky=EW)
        remove_to_cart6.grid(row=5, column=4, padx=50, pady=10, sticky=EW)
        remove_to_cart7.grid(row=6, column=4, padx=50, pady=10, sticky=EW)
        remove_to_cart8.grid(row=7, column=4, padx=50, pady=10, sticky=EW)


        #sandwichlabelprice = Label(frame8, text='50₹', font=("Poiret One", 14), fg='#000000')




        next1 = PhotoImage(file="next.png")
        def forwardbutton():
            global  grandtotal
            if grandtotal!=0:
                root7.destroy()
                testframe.testframefun(self)

            else:
                messagebox.showerror("Error", "Select atleast one item")
        forwadbutton = Button(frame8, image=next1, relief=FLAT,command=forwardbutton)
        forwadbutton.place(x=1100, y=660)
        # TODO link next button to billing window




        print("end of order")
        root7.mainloop()

class Staffmain():
    def staffmain(self):
        root4 = Tk()
        root4.title("StaffMAin")
        window_width = 1000
        window_height = 400

        screen_height = root4.winfo_screenheight()
        screen_width = root4.winfo_screenwidth()

        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)

        root4.geometry("1000x350")

        frame5 = Frame(root4, width=1000, height=350)
        frame5.pack()
        scrollbar = Scrollbar(frame5)
        scrollbar.pack(side=RIGHT,padx=10,ipady=50,expand=TRUE)

        mylist = Listbox(frame5, yscrollcommand=scrollbar.set)
        mylist.pack(pady=110,expand=FALSE)
        mylist.insert(END, "ORDER ID         Phone no                  Name                   Address")
        mylist.config(font=('courier', 11, 'normal'))


        #mylist.delete(1, END)

        scrollbar.config(command=mylist.yview)
        mylist.config(width=150, height=20)

        label_1 = Label(frame5, text="Search Box:", font=("Poiret One", 16), fg='#34495E')
        label_1.place(x=5, y=35)
        user=StringVar()

        entry_1 = Entry(frame5, width=50,textvariable=user)
        entry_1.place(x=143, y=42)

        def searchngettext():
            x=user.get()
            conn = sqlite3.connect('Main.db')
            c = conn.cursor()
            c.execute("SELECT Order_id from CUSTOMER WHERE Order_id=?",(x,))
            x1=c.fetchall()
            c.execute("SELECT Phone_no from CUSTOMER WHERE Order_id=?", (x,))
            x2 = c.fetchall()
            c.execute("SELECT Name from CUSTOMER WHERE Order_id=?", (x,))
            x3 = c.fetchall()
            c.execute("SELECT Address from CUSTOMER WHERE Order_id=?", (x,))
            x4 = c.fetchall()


            def cal(b):
                c.execute("SELECT Order_id from CUSTOMER")
                x1 = c.fetchall()
                length = len(x1)
                d1 = ''.join(map(str, x1))
                a = d1.replace(',', '')
                a1 = a.replace('(', '')
                a2 = a1.replace(')', ' ')
                a3 = a2.split()
                for i in a3:
                    print(i)
               # print(a3)
                #b=0
                for i in a3:
                    if x==i:
                        print('RUNNING')
                        print(i)
                        return  1

            q=cal(0)

            if q is 1:
                q=1
            else:
                q=0

            if user.get()=='':
                messagebox.showerror("Error", "Enter data")
                mylist.config(state=NORMAL)
                mylist.delete(1, END)
                mylist.config(state=DISABLED)
            elif  q is 0:
                messagebox.showerror("Error", "NO data Found")
                user.set('')
                mylist.config(state=NORMAL)
                mylist.delete(1, END)
                mylist.config(state=DISABLED)

            if q is 1:
                mylist.config(state=NORMAL)
                mylist.delete(1, END)
                y1=str(x1)
                y2 = str(x2)
                y3 = str(x3)
                y4 = str(x4)
                z1=y1[2:-3]
                z2 = y2[2:-3]
                z3 = y3[2:-3]
                z4 = y4[2:-3]
                w=z1+"         "+z2+"               "+z3
                l3=21-len(z3)
                y=w+(' '*l3)+z4
                z=str(y)
                mylist.insert(END,y,)
                mylist.config(state=DISABLED)
            conn.commit()
            c.close()
            conn.close()

        def showalldata():
            user.set('')
            conn = sqlite3.connect('Main.db')
            c = conn.cursor()
            c.execute("SELECT Order_id from CUSTOMER")
            x1 = c.fetchall()
            length = len(x1)
            d1=''.join(map(str,x1))
            a=d1.replace(',','')
            a1 = a.replace('(', '')
            a2 = a1.replace(')', ' ')
            a3=a2.split()
            size=0
            mylist.config(state=NORMAL)
            mylist.delete(1, END)
            mylist.config(state=DISABLED)
            while(size<length):
                c.execute("SELECT Order_id from CUSTOMER WHERE Order_id=?",(a3[size],))
                x1 = c.fetchall()
                c.execute("SELECT Phone_no from CUSTOMER WHERE Order_id=?", (a3[size],))
                x2 = c.fetchall()
                c.execute("SELECT Name from CUSTOMER WHERE Order_id=?", (a3[size],))
                x3 = c.fetchall()
                c.execute("SELECT Address from CUSTOMER WHERE Order_id=?",(a3[size],))
                x4 = c.fetchall()

                y1 = str(x1)
                y2 = str(x2)
                y3 = str(x3)
                y4 = str(x4)
                z1 = y1[2:-3]
                z2 = y2[2:-3]
                z3 = y3[2:-3]
                z4 = y4[2:-3]
                print(len(z3))

                l3 = 24-len(z3)
                print(l3)
                w=z1+"         "+z2+"               "+z3
                y=w+' '*l3+z4
                mylist.config(state=NORMAL)
                mylist.insert(END,y,)
                mylist.config(font=('courier', 11, 'normal'))
                mylist.config(state=DISABLED)
                size=size+1


        def deletedata():
            x = user.get()
            conn = sqlite3.connect('Main.db')
            c = conn.cursor()
            #c.execute("SELECT Order_id from CUSTOMER WHERE Order_id=?",(x,))
            #x1 = c.fetchall()


            def cal(a):
                conn = sqlite3.connect('Main.db')
                c = conn.cursor()
                c.execute("SELECT Order_id from CUSTOMER")
                x1 = c.fetchall()
                #print(x1)
                length = len(x1)
                d1 = ''.join(map(str, x1))
                a = d1.replace(',', '')
                a1 = a.replace('(', '')
                a2 = a1.replace(')', ' ')
                a3 = a2.split()
                #print('hey',a3[1])
                q = 0
                if x in a3:
                    #if x==i:
                    return 1
                else:
                    return 0

            q = cal(0)

            if user.get() == '':
                messagebox.showerror("Error", "Enter data")
                mylist.config(state=NORMAL)
                mylist.delete(1, END)
                mylist.config(state=DISABLED)

            elif q is 0:
                messagebox.showerror("Error", "NO data Found")
                user.set('')
                mylist.config(state=NORMAL)
                mylist.delete(1, END)
                mylist.config(state=DISABLED)

            if q is 1:
               # y1 = str(x1)
                #z1 = y1[2:-3]
               # y = z1 + "                                                            " + z2 + "                                                                 " + z3 + "                                                                    " + z4
                #z = str(y)
                conn = sqlite3.connect('Main.db')
                c = conn.cursor()
                print("delete data q runiing")
                c.execute("DELETE from CUSTOMER WHERE Order_id=?",(x,))
                conn.commit()
                messagebox.showinfo("Information", "Data Deleted")
            showalldata()
            conn.commit()
            c.close()
            conn.close()


        Searchbtn = Button(frame5, text="Search", width=12,command=searchngettext)  #TODO link login button
        Searchbtn.place(x=470, y=38)

        showall = Button(frame5, text="Show all data", width=12, command=showalldata)  # TODO link login button
        showall.place(x=580, y=38)

        deletedata = Button(frame5, text="Delete", width=12, command=deletedata)  # TODO link login button
        deletedata.place(x=690, y=38)

        showorderdet = Button(frame5, text="Show Order Details", width=16)  # TODO link login button
        showorderdet.place(x=805, y=38)


        def t2():
            root4.destroy()
            Stafflogin.Staffwin(self)

        back = PhotoImage(file="back.png")
        tback = back.subsample(2, 2)

        backbutton = Button(frame5, image=tback, relief=FLAT, command=t2)

        backbutton.place(x=5, y=290)

        root4.resizable(width=FALSE, height=FALSE)
        root4.mainloop()

class cancelorder():
    def canorder(self):
        root3 = Tk()
        root3.title("Staff")


        window_width = 200
        window_height = 370

        screen_height = root3.winfo_screenheight()
        screen_width = root3.winfo_screenwidth()

        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)

        root3.geometry("700x400")

        frame4 = Frame(root3, width=900, height=450)
        frame4.pack()
        scrollbar = Scrollbar(frame4)
        scrollbar.pack(side=RIGHT, padx=10, ipady=50, expand=TRUE)

        mylist = Listbox(frame4, yscrollcommand=scrollbar.set)
        mylist.pack(pady=100, expand=FALSE)
        mylist.config(state='normal')
        mylist.insert(END,"Item               Cost              Count          Total Cost")
        mylist.config(font=('courier', 11, 'normal'))
        mylist.config(state='disabled')
        # mylist.delete(1, END)

        scrollbar.config(command=mylist.yview)
        mylist.config(width=80, height=20)

        label_1 = Label(frame4, text="Order No:", font=("Poiret One", 18), fg='#34495E')
        label_1.place(x=2, y=40)
        user=StringVar()
        label_2 = Label(frame4, text="ENTERED ORDER NUMBER:", font=("Poiret One", 10), fg='#34495E')
        label_2.place(x=1, y=79)
        label_3 = Label(frame4, font=("Poiret One", 10), fg='#34495E')

        label_3.place(x=180, y=79)
        entry_1 = Entry(frame4, width=30,textvariable=user)
        entry_1.place(x=120, y=47)
        def print1():
            x = user.get()
            if x=='':
                messagebox.showerror("Error", "Enter Order Id")
            else:
                x=user.get()
                conn = sqlite3.connect('Main.db')
                c = conn.cursor()
                c.execute("SELECT Order_id from ORDER_DETAILS WHERE Order_id=?",(x,))
                data = c.fetchall()
                #print(data)
                length=len(data)
                q=0
                for i in data:
                    k=str(i)
                    j=k[1:-2]
                    #print(j)
                    if x in j:
                        q=1
                    else:
                        q=0
                if q==1:
                    mylist.config(state='normal')
                    mylist.delete(1, END)
                    for j in range(len(data)):
                        c.execute("SELECT Item_name,Cost,Count,T_cost from ORDER_DETAILS WHERE Order_id=?", (x,))
                        x1 = c.fetchall()
                        print(x1)
                        x2 = str(x1).replace(',', '')
                        x4 = str(x2).replace(')', '')
                        x5 = str(x4).replace("'", '')
                        x6 = str(x5).replace("[", '')
                        x7 = str(x6).replace("]", '')
                        list1 = x7.split('(')
                        print('dfghj',list1)
                        for i in range(1, len(list1)):
                            list2 = str(list1[i]).split()
                            var1 = len(list2[0])
                            var2 = len(list2[1])
                            var3 = len(list2[2])

                            y = list2[0] + " " * (19 - var1) + list2[1] + " " * (18 - var2) + list2[2] + " " * (15 - var3) + list2[3]
                            #print(y)

                            mylist.insert(END, y, )
                        mylist.config(state='disabled')

                else:
                    messagebox.showerror("Error", "No order found with the given order id")
                    mylist.config(state='normal')
                    mylist.delete(1, END)
                    mylist.config(state='disabled')



        search = Button(frame4, text="Search", width=13,command=print1)  #TODO link login button
        search.place(x=313, y=42)


        def t2():
            root3.destroy()
            A.customerwindow(self)

        back = PhotoImage(file="back.png")
        tback = back.subsample(2, 2)

        backbutton = Button(frame4, image=tback, relief=FLAT, command=t2)
        backbutton.place(x=2, y=300)
        root3.resizable(width=FALSE, height=FALSE)
        root3.mainloop()

class Stafflogin():
    def Staffwin(self):
        root2 = Tk()
        root2.title("Staff")

        window_width = 500
        window_height = 300

        screen_height = root2.winfo_screenheight()
        screen_width = root2.winfo_screenwidth()

        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)

        root2.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coordinate, y_coordinate))

        frame3 = Frame(root2, width=500, height=300)
        frame3.pack()

        label_1 = Label(frame3, text="Username", font=("Poiret One", 24), fg='#34495E')
        label_1.place(x=10, y=60)

        label_2 = Label(frame3, text="Password", font=("Poiret One", 24), fg='#34495E')
        label_2.place(x=10, y=100)
        user=StringVar()
        password= StringVar()
        entry_1 = Entry(frame3, width=25,textvariable=user)
        entry_1.place(x=200, y=70)

        entry_2 = Entry(frame3, show="\u2022",textvariable=password)
        entry_2.place(x=200, y=115)
        def print1():
            x='Sharad'
            y='admin'
            if(x=='Sharad' or x=='Aryan' and y=='admin'):
                messagebox.showinfo("info", "Login Successfull")
                def t4():
                    root2.destroy()
                    Staffmain.staffmain(self)
                next1 = Button(frame3, text="CONTINUE", width=15,command=t4)  # TODO link login button
                next1.place(x=205, y=175)

            else:
                user.set('')
                password.set('')
                messagebox.showerror("Error", "Try again.!")


        checkbox = Checkbutton(frame3, text="Keep me logged in")
        checkbox.place(x=10, y=150)

        loginbutton = Button(frame3, text="LOGIN", width=15,command=print1)  #TODO link login button
        loginbutton.place(x=205, y=175)


        def t2():
            root2.destroy()
            B.welcomeWindow(self)

        back = PhotoImage(file="back.png")
        tback = back.subsample(2, 2)

        backbutton = Button(frame3, image=tback, relief=FLAT, command=t2)
        backbutton.place(x=10, y=250)

        root2.mainloop()

# A = Customer Window
class A():#customer window
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
        Cancel = PhotoImage(file="shopping-cart.png")
        back = PhotoImage(file="back.png")

        def t2():
            root1.destroy()
            B.welcomeWindow(self)

        def t0():
            root1.destroy()
            Orderclass.ordermethod(self)


        OrderButton = Button(frame2, image=Order,command=t0)
        OrderButton.place(x=152, y=125)
        button3 = Button(frame2, image=back, command=t2, relief=FLAT)
        button3.place(x=50, y=500)

        def t3():
            root1.destroy()
            cancelorder.canorder(self)
        CancelButton = Button(frame2, image=Cancel,command=t3)
        CancelButton.place(x=550, y=125)

        OrderLabel = Label(frame2, text="       ORDER", font=("Poiret One", 24), fg='#34495E')
        CancelLabel = Label(frame2, text=" CANCEL ORDER", font=("Poiret One", 24), fg='#34495E')

        OrderLabel.place(x=152, y=405)
        CancelLabel.place(x=550, y=405)

        root1.mainloop()

        print("mid")

# B = Welcome Window
class B():#welcome
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

        staffButton = Button(frame1, image=staffPhoto, command=ToStaff)
        staffButton.place(x=550, y=125)

        customerLabel = Label(frame1, text="   CUSTOMER", font=("Poiret One", 24), fg='#34495E')
        staffLabel = Label(frame1, text="         STAFF", font=("Poiret One", 24), fg='#34495E')

        customerLabel.place(x=152, y=405)
        staffLabel.place(x=550, y=405)

        root.mainloop()

b=B()
b.welcomeWindow()
print("end")

