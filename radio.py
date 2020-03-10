from tkinter import *
from tkinter import ttk 	


app = Tk()
app.title("RadioDial")
app.geometry("150x300")

# Function get the StringVar

def radio():
	tfield.delete(0.0, END)
	tfield.insert(INSERT, dials.get())
	
dials = StringVar()
r1 = ttk.Radiobutton(app, text="1", value="One", var=dials)
r1.grid(row=0, column=0)

r2 = ttk.Radiobutton(app, text="2", value="Two", var=dials)
r2.grid(row=1, column=0)

r3 = ttk.Radiobutton(app, text="3", value="Tree", var=dials)
r3.grid(row=2, column=0)

r4 = ttk.Radiobutton(app, text="4", value="Four", var=dials)
r4.grid(row=3, column=0)

r5 = ttk.Radiobutton(app, text="5", value="Five", var=dials)
r5.grid(row=4, column=0)


b1 = Button(app, text="Submit", command=radio)
b1.grid(row=5, column=0)

tfield = Text(app, width=10, height=5, font="Arial 20 bold")
tfield.grid(row=6, column=0)

app.mainloop()
