from tkinter import *
from tkinter import ttk

def main():

    notebook.add(frame1, text="One")
    notebook.add(frame2, text="Two")
    notebook.add(frame3, text="Three")

    Label(frame1, text="What is Tkinter?").grid(row=2, column=2)
    Button(frame1, text="Guided User Interface", command=correct1).grid(row=3, column=1)
    Button(frame1, text="Variable", command=incorrect1).grid(row=3, column=2)
    Button(frame1, text="Function", command=incorrect1).grid(row=3, column=3)

    Label(frame2, text="What is Turtle?").grid(row=2, column=2)
    Button(frame2, text="Guided User Interface", command=incorrect2).grid(row=3, column=1)
    Button(frame2, text="Module", command=correct2).grid(row=3, column=2)
    Button(frame2, text="Boolean Value", command=incorrect2).grid(row=3, column=3)

    Label(frame3, text="What does the 'Print' command do?").grid(row=2, column=2)
    Button(frame3, text="Create a window", command=incorrect3).grid(row=3, column=1)
    Button(frame3, text="Show a message in the Python Shell", command=correct3).grid(row=3, column=2)
    Button(frame3, text="Print to the printer", command=incorrect3).grid(row=3, column=3)

    notebook.pack()

    Label(root, text="Total:").pack()
    Label(root, textvariable=total).pack()

def correct1():
    Label(frame1, text="Correct").grid(row=1, column=2)
    counter()

def incorrect1():
    Label(frame1, text="Incorrect").grid(row=1, column=2)

def correct2():
    Label(frame2, text="Correct").grid(row=1, column=2)
    counter()

def incorrect2():
    Label(frame2, text="Incorrect").grid(row=1, column=2)

def correct3():
    Label(frame3, text="Correct").grid(row=1, column=2)
    counter()

def incorrect3():
    Label(frame3, text="Incorrect").grid(row=1, column=2)

def counter():
    total.set(total.get() + 1)

root = Tk()

total = IntVar()  # defaults to 0

notebook = ttk.Notebook(root)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)

main()

root.mainloop()
