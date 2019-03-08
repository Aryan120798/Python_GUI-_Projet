from tkinter import *
import sqlite3

root = Tk()
root.geometry("500x500")
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)


mylist = Listbox(root, yscrollcommand = scrollbar.set )

'''def t9():
    print("Creating table")
    conn = sqlite3.connect('Main.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS CUSTOMER(Order_id INTEGER,
	Name TEXT,
	Address TEXT,
	Phone_no INTEGER)')
    mylist.delete(0, END)
    for row in c.fetchall():
        z=str(row)
        y=z[1:6]+' '+z[9:-2]
        mylist.insert(END,y)
    conn.commit()
    c.close()
    conn.close()'''

def t1():
    print("Display fun running")
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('SELECT * from INFO1')
    mylist.delete(0, END)
    for row in c.fetchall():
        mylist.insert(END,row)
    conn.commit()
    c.close()
    conn.close()

def entry():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("INSERT INTO INFO1 VALUES(124,'qwenbbhhiujnink')")
    conn.commit()
    c.close()
    conn.close()

def delete1():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('DELETE from INFO1')
    #mylist.destroy(0,END)
    conn.commit()
    c.close()
    conn.close()

button =Button(width=6,height=3,text="Dispaly",command=t1)
button.place(x=1,y=3)
button.pack()

button1 =Button(width=6,height=3,text="Insert",command=entry)
button1.place(x=3,y=3)
button1.pack()

button2 =Button(width=6,height=3,text="Delete",command=delete1)
button2.place(x=3,y=3)
button2.pack()

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )
window_width = 1000
window_height = 600

screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)
mylist.config(width=90)

root.mainloop()