from tkinter import *
from tkinter import ttk 	


app = Tk()
app.title("RadioDial")
app.geometry("300x300")

# Function get the StringVar

def radio():
	tfield.delete(0.0, END)
	tfield.insert(INSERT, dials.get())
	
dials = StringVar()
r1 = ttk.Radiobutton(app, text="1", value="One", var=dials)
r1.pack()

r2 = ttk.Radiobutton(app, text="2", value="Two", var=dials)
r2.pack()

r3 = ttk.Radiobutton(app, text="3", value="Tree", var=dials)
r3.pack()

r4 = ttk.Radiobutton(app, text="4", value="Four", var=dials)
r4.pack()

r5 = ttk.Radiobutton(app, text="5", value="Five", var=dials)
r5.pack()


b1 = Button(app, text="Submit", command=radio)
b1.pack()

tfield = Text(app, width=10, height=5, font="Arial 20 bold")
tfield.pack()

app.mainloop()
