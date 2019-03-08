class Order():
    def order(self):
        #This frame has order menu

        root4 = Tk()
        print("start of order")
        root4.title("Order")

        window_width = 1360
        window_height = 760

        screen_height = root4.winfo_screenheight()
        screen_width = root4.winfo_screenwidth()

        x_coordinate = (screen_width/2) - (window_width/2)
        y_coordinate = (screen_height/2) - (window_height/2)

        root4.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coordinate, y_coordinate))

        frame2 = Frame(root4, height=1360, width=760)
        frame2.pack(fill=BOTH)

        coffee = PhotoImage(file="coffee.png")
        burrito = PhotoImage(file="burrito.png")
        frenchfries = PhotoImage(file="french-fries.png")
        hamburger = PhotoImage(file="hamburger.png")
        icecream = PhotoImage(file="ice-cream.png")
        ketchup = PhotoImage(file="ketchup.png")
        pizza = PhotoImage(file="pizza.png")
        sandwich = PhotoImage(file="sandwich.png")
        back = PhotoImage(file="back.png")

        coffeelabel = Label(frame2, image=coffee)
        burritolabel = Label(frame2, image=burrito)
        frenchfrieslabel = Label(frame2, image=frenchfries)
        hamburgerlabel = Label(frame2, image=hamburger)
        icecreamlabel = Label(frame2, image=icecream)
        ketchuplabel = Label(frame2, image=ketchup)
        pizzalabel = Label(frame2, image=pizza)
        sandwichlabel = Label(frame2, image=sandwich)


        backbutton = Button(frame2, image=back, relief=FLAT)

        coffeelabel.grid(row=0, column=0, padx=30, pady=10)
        burritolabel.grid(row=1, column=0, padx=30, pady=7)
        frenchfrieslabel.grid(row=2, column=0, padx=10, pady=7)
        hamburgerlabel.grid(row=3, column=0, padx=10, pady=7)
        icecreamlabel.grid(row=4, column=0, padx=10, pady=7)
        ketchuplabel.grid(row=5, column=0, padx=10, pady=7)
        pizzalabel.grid(row=6, column=0, padx=10, pady=7)
        sandwichlabel.grid(row=7, column=0, padx=10, pady=4)
        backbutton.grid(row=8, column=0, padx=10, pady=7)

        coffeelabel2 = Label(frame2, text='COFFEE', font=("Poiret One", 14), fg='#000000')
        burritolabel2 = Label(frame2, text='FRANKIE', font=("Poiret One", 14), fg='#000000')
        frenchfrieslabel2 = Label(frame2, text='FRENCH-FRIES', font=("Poiret One", 14), fg='#000000')
        hamburgerlabel2 = Label(frame2, text='BURGER', font=("Poiret One", 14), fg='#000000')
        icecreamlabel2 = Label(frame2, text='ICE-CREAM', font=("Poiret One", 14), fg='#000000')
        ketchuplabel2 = Label(frame2, text='KETCHUP', font=("Poiret One", 14), fg='#000000')
        pizzalabel2 = Label(frame2, text='PIZZA', font=("Poiret One", 14), fg='#000000')
        sandwichlabel2 = Label(frame2, text='SANDWICH', font=("Poiret One", 14), fg='#000000')

        coffeelabel2.grid(row=0, column=1, padx=100, pady=10, sticky=EW)
        burritolabel2.grid(row=1, column=1, padx=100, pady=7, sticky=EW)
        frenchfrieslabel2.grid(row=2, column=1, padx=100, pady=7, sticky=EW)
        hamburgerlabel2.grid(row=3, column=1, padx=100, pady=7, sticky=EW)
        icecreamlabel2.grid(row=4, column=1, padx=100, pady=7, sticky=EW)
        ketchuplabel2.grid(row=5, column=1, padx=100, pady=7, sticky=EW)
        pizzalabel2.grid(row=6, column=1, padx=100, pady=7, sticky=EW)
        sandwichlabel2.grid(row=7, column=1, padx=100, pady=4, sticky=EW)

        coffeelabelprice = Label(frame2, text='40₹', font=("Poiret One", 14), fg='#000000')
        burritolabelprice = Label(frame2, text='50₹', font=("Poiret One", 14), fg='#000000')
        frenchfrieslabelprice = Label(frame2, text='50₹', font=("Poiret One", 14), fg='#000000')
        hamburgerlabelprice = Label(frame2, text='100₹', font=("Poiret One", 14), fg='#000000')
        icecreamlabelprice = Label(frame2, text='30₹', font=("Poiret One", 14), fg='#000000')
        ketchuplabelprice = Label(frame2, text='5₹', font=("Poiret One", 14), fg='#000000')
        pizzalabelprice = Label(frame2, text='250₹', font=("Poiret One", 14), fg='#000000')
        sandwichlabelprice = Label(frame2, text='50₹', font=("Poiret One", 14), fg='#000000')


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

        tadd_to_cart = add_to_cart.subsample(2, 2 )
        tremove_to_cart = remove_to_cart.subsample(2, 2)

        add_to_cart1 = Button(frame2, image=tadd_to_cart, relief=FLAT)
        add_to_cart2 = Button(frame2, image=tadd_to_cart, relief=FLAT)
        add_to_cart3 = Button(frame2, image=tadd_to_cart, relief=FLAT)
        add_to_cart4 = Button(frame2, image=tadd_to_cart, relief=FLAT)
        add_to_cart5 = Button(frame2, image=tadd_to_cart, relief=FLAT)
        add_to_cart6 = Button(frame2, image=tadd_to_cart, relief=FLAT)
        add_to_cart7 = Button(frame2, image=tadd_to_cart, relief=FLAT)
        add_to_cart8 = Button(frame2, image=tadd_to_cart, relief=FLAT)
        #TODO link add to cart buttons to database

        remove_to_cart1 = Button(frame2, image=tremove_to_cart, relief=FLAT)
        remove_to_cart2 = Button(frame2, image=tremove_to_cart, relief=FLAT)
        remove_to_cart3 = Button(frame2, image=tremove_to_cart, relief=FLAT)
        remove_to_cart4 = Button(frame2, image=tremove_to_cart, relief=FLAT)
        remove_to_cart5 = Button(frame2, image=tremove_to_cart, relief=FLAT)
        remove_to_cart6 = Button(frame2, image=tremove_to_cart, relief=FLAT)
        remove_to_cart7 = Button(frame2, image=tremove_to_cart, relief=FLAT)
        remove_to_cart8 = Button(frame2, image=tremove_to_cart, relief=FLAT)
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

        coffeelabelpricetotal = Label(frame2, text='EDIT', font=("Poiret One", 14), fg='#000000')
        burritolabelpricetotal = Label(frame2, text='EDIT', font=("Poiret One", 14), fg='#000000')
        frenchfrieslabelpricetotal = Label(frame2, text='EDIT', font=("Poiret One", 14), fg='#000000')
        hamburgerlabelpricetotal = Label(frame2, text='EDIT', font=("Poiret One", 14), fg='#000000')
        icecreamlabelpricetotal = Label(frame2, text='EDIT', font=("Poiret One", 14), fg='#000000')
        ketchuplabelpricetotal = Label(frame2, text='EDIT', font=("Poiret One", 14), fg='#000000')
        pizzalabelpricetotal = Label(frame2, text='EDIT', font=("Poiret One", 14), fg='#000000')
        sandwichlabelpricetotal = Label(frame2, text='EDIT', font=("Poiret One", 14), fg='#000000')

        coffeelabelpricetotal.grid(row=0, column=5, padx=100, pady=10, sticky=EW)
        burritolabelpricetotal.grid(row=1, column=5, padx=100, pady=7, sticky=EW)
        frenchfrieslabelpricetotal.grid(row=2, column=5, padx=100, pady=7, sticky=EW)
        hamburgerlabelpricetotal.grid(row=3, column=5, padx=100, pady=7, sticky=EW)
        icecreamlabelpricetotal.grid(row=4, column=5, padx=100, pady=7, sticky=EW)
        ketchuplabelpricetotal.grid(row=5, column=5, padx=100, pady=7, sticky=EW)
        pizzalabelpricetotal.grid(row=6, column=5, padx=100, pady=7, sticky=EW)
        sandwichlabelpricetotal.grid(row=7, column=5, padx=100, pady=4, sticky=EW)

        next1 = PhotoImage(file="next.png")

        forwadbutton = Button(frame2, image=next1, relief=FLAT)
        forwadbutton.place(x=1250, y=660)
        # TODO link next button to billing window

        print("end of order")
        mainloop()

