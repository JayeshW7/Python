import webbrowser as wb

from tkinter import *
obj = Tk(className="Search Engine")

e = Entry(obj, font=("Helvetica",25))
e.grid()

def Navigate():
    query = e.get()
    wb.open("https://www.youtube.com/results?search_query="+query)

b = Button(obj, text="search", command= Navigate, font=("Helvetica",25))
b.grid()

b1 = Button(obj, text="close", command= obj.destroy, font=("Helvetica",25))
b1.grid()

obj.mainloop()