from tkinter import *
from tkinter import simpledialog
import tkinter.messagebox
import tkinter
import datetime

top = Tk()
username = StringVar()
password = StringVar()
filnamn = StringVar()

framecanvas = Frame(top, bd=10, bg="black")
framecanvas.pack(side=TOP)

menubar = Menu(framecanvas)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=top.destroy)
menubar.add_cascade(label="File", menu=filemenu)

bild = PhotoImage(file='bild2.gif').subsample(2)
label = Label(framecanvas, image=bild)
label.pack(side=TOP)

L1 = Label(framecanvas, text="User Name", fg="white", bg="black")
L1.pack(side=TOP)
E2 = Entry(framecanvas, bd=5, text=username, bg="black", fg="white")
E2.pack(side=TOP)
L2 = Label(framecanvas, text="Password", bg="black", fg="white")
L2.pack(side=TOP)
E1 = Entry(framecanvas, bd=5, show="*", text=password, bg="black", fg="white")
E1.pack(side=TOP)


def Filename():
    if username.get() == "admin" and password.get() == "123":
        IN = Label(framecanvas, text="input filename", fg="white", bg="black")
        IN.pack()
        IN2 = Entry(framecanvas, bd=5, text=filnamn, bg="black", fg="white")
        IN2.pack()
        A = tkinter.Button(framecanvas, text="Open file", command=textfil, bg="black", fg="white")
        A.pack()
        B = tkinter.Button(framecanvas, text="New file", command=Newfileopen, bg="black", fg="white")
        B.pack()
    else:
        tkinter.messagebox.showinfo("Wrong", "wrong password or username")


B = tkinter.Button(framecanvas, text="Login", command=Filename, bg="black", fg="white")
B.pack()


def textfil():
    global filnamn1
    filnamn1 = filnamn.get() + ".txt"
    try:
        with open(filnamn1, "r") as x:
            global text
            root = Tk()
            text = Text(root)
            text.insert(INSERT, x.read())
            menubar2 = Menu(root)
            filemenu2 = Menu(menubar2, tearoff=0)
            filemenu2.add_command(label="New", command=Newfilename)
            filemenu2.add_command(label="Save", command=save)
            filemenu2.add_separator()
            filemenu2.add_command(label="Exit", command=root.destroy)
            menubar2.add_cascade(label="File", menu=filemenu2)
            root.title(filnamn.get())

            text.pack()
            root.config(menu=menubar2)
            root.mainloop()
    except:
        tkinter.messagebox.showinfo("Wrong", "File does not exist")

def Newfilename():
    global s
    s = simpledialog.askstring("New file name", "Enter file name:")
    Newfileopen2()

def Newfileopen():
    root2 = Tk()
    global nyfil1
    nyfil1 = filnamn.get() + ".txt"
    with open(nyfil1, "w") as x:
        x.close()

    with open(nyfil1, "r")as y:
        global text
        text = Text(root2)
        text.insert(INSERT, y.read())
        menubar3 = Menu(root2)
        filemenu3 = Menu(menubar3, tearoff=0)
        filemenu3.add_command(label="New", command=Newfilename)
        filemenu3.add_command(label="Save", command=save2)
        filemenu3.add_separator()
        filemenu3.add_command(label="Exit", command=root2.destroy)
        menubar3.add_cascade(label="File", menu=filemenu3)

        root2.title(filnamn.get())
        text.pack()
        root2.config(menu=menubar3)
        root2.mainloop()

def Newfileopen2():
    root3 = Tk()
    global newname
    newname = s + ".txt"
    with open(newname, "w") as x:
        x.close()

    with open(newname, "r")as y:
        global text
        text = Text(root3)
        text.insert(INSERT, y.read())
        menubar3 = Menu(root3)
        filemenu3 = Menu(menubar3, tearoff=0)
        filemenu3.add_command(label="New", command=Newfilename)
        filemenu3.add_command(label="Save", command=save3)
        filemenu3.add_separator()
        filemenu3.add_command(label="Exit", command=root3.destroy)
        menubar3.add_cascade(label="File", menu=filemenu3)

        root3.title(s)
        text.pack()
        root3.config(menu=menubar3)
        root3.mainloop()


def save():
    with open(filnamn1, "w") as x:
        input = text.get("1.0", END)
        x.write(input)


def save2():
    with open(nyfil1, "w")as x:
        input2 = text.get("1.0", END)
        x.write((input2))


def save3():
    with open(newname, "w")as x:
        input3 = text.get("1.0", END)
        x.write((input3))


now = datetime.datetime.now()
date = (now.year,"-", now.month,"-", now.day)
statusframe = Frame(top, bd=1, bg="black")
statursbar = Label(statusframe, bd=4, relief=RAISED, anchor=W, text=date, bg="black", fg="white")
statusframe.pack(side=BOTTOM, fill=X)
statursbar.pack(side=BOTTOM, fill=X)

top.config(menu=menubar)
top.mainloop()
