from tkinter import *

#This frame has two buttons and two labels - Customers and Staff Members

print("aa")
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

customerButton = Button(frame1, image=customerPhoto)
customerButton.place(x=152, y=125)
staffButton = Button(frame1, image=staffPhoto)
staffButton.place(x=550, y=125)

customerLabel = Label(frame1, text="   CUSTOMER", font=("Poiret One", 24), fg='#34495E')
staffLabel = Label(frame1, text="         STAFF", font=("Poiret One", 24), fg='#34495E')

customerLabel.place(x=152, y=405)
staffLabel.place(x=550, y=405)

mainloop()


print("SS")


