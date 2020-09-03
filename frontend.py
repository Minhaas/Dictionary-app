from tkinter import *

window = Tk()
window.title("Library App")

def dict():
    return 0

#Labels
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)
l2 = Label(window, text="Author")
l2.grid(row=0, column=2)
l3 = Label(window, text="Year")
l3.grid(row=1, column=0)
l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

#Entries
title = StringVar()
year = StringVar()
isbn = StringVar()
author = StringVar()
e1 = Entry(window, textvariable=title, width=30)
e1.grid(row=0, column=1)
e2 = Entry(window, textvariable=author, width=30)
e2.grid(row=0, column=3)
e3 = Entry(window, textvariable=year, width=30)
e3.grid(row=1, column=1)
e4 = Entry(window, textvariable=isbn, width=30)
e4.grid(row=1, column=3)

#Buttons
b1 = Button(window, text="View all", command=dict, height=1, width= 30, highlightbackground = "Black")
b1.grid(row=2, column=3)
b2 = Button(window, text="Search entry", command=dict, height=1, width= 30, highlightbackground = "Black")
b2.grid(row=3, column=3)
b3 = Button(window, text="Add entry", command=dict, height=1, width= 30, highlightbackground = "Black")
b3.grid(row=4, column=3)
b4 = Button(window, text="Update", command=dict, height=1, width= 30, highlightbackground = "Black")
b4.grid(row=5, column=3)
b5 = Button(window, text="Delete", command=dict, height=1, width= 30, highlightbackground = "Black")
b5.grid(row=6, column=3)
b6 = Button(window, text="Close", command=dict, height=1, width= 30, highlightbackground = "Black")
b6.grid(row=7, column=3)























window.mainloop()