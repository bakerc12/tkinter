from tkinter import *


master = Tk()

#from tkinter import *
 
var1 = IntVar()
Checkbutton(master, text='male', variable=var1).pack()
var2 = IntVar()
Checkbutton(master, text='female', variable=var2).pack()
var3 = IntVar()
Checkbutton(master, text='other', variable=var3).pack()
var4 = IntVar()
Checkbutton(master, text='Nathan Leroy Savarese', variable=var4).pack()


 
Label(master, text='First Name').pack()
Label(master, text='Last Name').pack()
Label(master, text='Date Of Birth ').pack()
Label(master, text='Country').pack()
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e1.pack()
e2.pack()
e3.pack()
e4.pack()


 
w = Scale(master, from_=0, to=42)
w.pack()
w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.pack()
w = Scale(master, from_=0, to=500)
w.pack()
w = Scale(master, from_=0, to=100, orient=HORIZONTAL)
w.pack()

w = Label(master, text='Label 1')
w.pack()
w2 = Label(master, text='Label 2')
w2.pack()
w3 = Label(master, text='Label 3')
w3.pack()
w4 = Label(master, text='Label 4')
w4.pack()

master.title('These are buttons')
button = Button(master, text='Button 1', width=25, command=master.destroy)
button.pack()
button2 =Button(master, text='Button 2', width=25, command=master.destroy)
button2.pack()
button3 = Button(master, text='Button 3', width=25, command=master.destroy)
button3.pack()
button4 = Button(master, text='Button 4', width=25, command=master.destroy)
button4.pack()


mb = Menubutton (master, text = "This Is My Menu")
mb.pack()
mb.menu = Menu ( mb, tearoff = 0 )
mb["menu"] = mb.menu
cVar = IntVar()
aVar = IntVar()
mb.menu.add_checkbutton ( label ='Contact', variable = cVar )
mb.menu.add_checkbutton ( label = 'About', variable = aVar )
mb.pack()

ourMessage ='This is a message box!'
messageVar = Message(master, text = ourMessage)
messageVar.config(bg='white')
messageVar.pack( )

v = IntVar()
Radiobutton(master, text='Are you in Science', variable=v, value=1).pack(anchor=W)
Radiobutton(master, text='Are you in Math', variable=v, value=2).pack(anchor=W)
Radiobutton(master, text='Are you in Lang & Lit', variable=v, value=3).pack(anchor=W)
Radiobutton(master, text='Are you in Computer Science', variable=v, value=4).pack(anchor=W)
Radiobutton(master, text='Are you in ECON', variable=v, value=5).pack(anchor=W)

w = Spinbox(master, from_ = 0, to = 10)
w.pack()
mainloop()





mainloop()

