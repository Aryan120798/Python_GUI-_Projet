from tkinter import *

#This frame has two buttons and two labels - Order and Cancel

root1 = Tk()
root1.title("Customer Choice")

window_width = 1000
window_height = 600

screen_height = root1.winfo_screenheight()
screen_width = root1.winfo_screenwidth()

x_coordinate = (screen_width/2) - (window_width/2)
y_coordinate = (screen_height/2) - (window_height/2)

root1.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coordinate, y_coordinate))

frame1 = Frame(root1, height=1000, width=600)
frame1.pack(fill=BOTH)

Order = PhotoImage(file="fast-food.png")
Cancel = PhotoImage(file="shopping-cart.png")

OrderButton = Button(frame1, image=Order)
OrderButton.place(x=152, y=125)
CancelButton = Button(frame1, image=Cancel)
CancelButton.place(x=550, y=125)

OrderLabel = Label(frame1, text="       ORDER", font=("Poiret One", 24), fg='#34495E')
CancelLabel = Label(frame1, text=" CANCEL ORDER", font=("Poiret One", 24), fg='#34495E')

OrderLabel.place(x=152, y=405)
CancelLabel.place(x=550, y=405)

mainloop()


