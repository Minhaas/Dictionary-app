from tkinter import *
import backend

window = Tk()
window.title("Library Database Application")
#window.geometry("1000x750") TO set size of the tkinter window

#Wrapper functions to access functions in backend.py, this helps so that parameters can be passes appropriately to each function in the backend.
def view_command():
    list1.delete(0, END)
    for row in backend.viewAll():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in backend.search(title.get(), author.get(), year.get(), isbn.get()):
        list1.insert(END, row)

def insert_command():
    list1.delete(0, END)
    backend.addEntry(title.get(), author.get(), year.get(), isbn.get())
    list1.insert(END, (title.get(), author.get(), year.get(), isbn.get()))

def update_command():
    list1.delete(0, END)
    backend.update(select[0], title.get(), author.get(), year.get(), isbn.get())
    list1.insert(END, (title.get(), author.get(), year.get(), isbn.get()))
def getRow(event):
    try: #Try and pass used to handle exceptions and errors in the program, in particular, the IndexError showing up in the program
        global select
        index = list1.curselection()[0] #Used to get the index of the selected tuple
        select = list1.get(index)
        #Code to add the values of the selected tuple in the listbox to its relevant columns
        e1.delete(0, END)
        e1.insert(END, select[1])
        e2.delete(0, END)
        e2.insert(END, select[2])
        e3.delete(0, END)
        e3.insert(END, select[3])
        e4.delete(0, END)
        e4.insert(END, select[4])
    except :
        pass

def delete_command():
    backend.delete(select[0]) #This will help pass ID as parameter to the backend.delete() function
    
def closeWindow():
    window.destroy() #This closes the tkinter window once you click a button

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

#Listbox
list1 = Listbox(window, height = 8, width = 35)
list1.grid(row= 2, column= 0, columnspan=2, rowspan= 8)

#Buttons
b1 = Button(window, text="View all", command=view_command, height=1, width= 30, highlightbackground = "Black")
b1.grid(row=2, column=3)
b2 = Button(window, text="Search entry", command=search_command, height=1, width= 30, highlightbackground = "Black")
b2.grid(row=3, column=3)
b3 = Button(window, text="Add entry", command=insert_command, height=1, width= 30, highlightbackground = "Black")
b3.grid(row=4, column=3)
b4 = Button(window, text="Update Selected", command=update_command, height=1, width= 30, highlightbackground = "Black")
b4.grid(row=5, column=3)
b5 = Button(window, text="Delete Selected", command=delete_command, height=1, width= 30, highlightbackground = "Black")
b5.grid(row=6, column=3)
b6 = Button(window, text="Close", command=closeWindow, height=1, width= 30, highlightbackground = "Black")
b6.grid(row=7, column=3)

#Scrollwheel
sb1=Scrollbar(window, background= "Red", highlightbackground="White")
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand= sb1.set)
sb1.configure(command= list1.yview)

list1.bind('<<ListboxSelect>>', getRow)

window.mainloop()