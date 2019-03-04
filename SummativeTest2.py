from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from SummativeResponses import SummativeResponses

def main():

    notebook.add(frame1, text="One")
    notebook.add(frame2, text="Two")
    notebook.add(frame3, text="Three")
    notebook.add(frame4, text="Four")
    notebook.add(frame5, text="Five")
    notebook.add(frameSub, text="Submit")

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

    Label(frame4, text="What is Sublime Text?").grid(row=2, column=2)
    Button(frame4, text="A text editor", command=correct4).grid(row=3, column=1)
    Button(frame4, text="A music player", command=incorrect4).grid(row=3, column=2)
    Button(frame4, text="A word processor", command=incorrect4).grid(row=3, column=3)

    Label(frame5, text="What type of language is python?").grid(row=2, column=2)
    Button(frame5, text="A low level language", command=incorrect5).grid(row=3, column=1)
    Button(frame5, text="An object orientated language", command=incorrect5).grid(row=3, column=2)
    Button(frame5, text="A high level language", command=correct5).grid(row=3, column=3)

    Button(frameSub, text="Submit", font=('MS','8','bold'),command=submit).grid(row=2, column=4, columnspan=2)

    notebook.pack()

    # Label(root, text="Total:").pack()
    # Label(root, textvariable=total).pack()

def correct1():
    Label(frame1, text="Answer Submitted").grid(row=1, column=2)
    # counter()

def incorrect1():
    Label(frame1, text="Answer Submitted").grid(row=1, column=2)

def correct2():
    Label(frame2, text="Answer Submitted").grid(row=1, column=2)
    # counter()

def incorrect2():
    Label(frame2, text="Answer Submitted").grid(row=1, column=2)

def correct3():
    Label(frame3, text="Answer Submitted").grid(row=1, column=2)
    # counter()

def incorrect3():
    Label(frame3, text="Answer Submitted").grid(row=1, column=2)

def correct4():
    Label(frame4, text="Answer Submitted").grid(row=1, column=2)
    # counter()

def incorrect4():
    Label(frame4, text="Answer Submitted").grid(row=1, column=2)

def correct5():
    Label(frame5, text="Answer Submitted").grid(row=1, column=2)
    # counter()

def incorrect5():
    Label(frame5, text="Answer Submitted").grid(row=1, column=2)

# def counter():
#     total.set(total.get() + 1)

# Submitting the answers to SummativeResponses.py
def submit():
    Label(frameSub, text="Test Submitted").grid(row=1,column=2)
    storeResponse()

# Storing the responses in a database within SummativeResponses.py
def storeResponse():
        import shelve
        db = shelve.open('responsedb')

        responseCount = len(db)
        Ans = Response(str(responseCount+1), strProg, correct1.get(), correct2.get(), correct3.get(), correct4.get(), correct5.get())
        db[Ans.respNo] = Ans
        db.close



root = Tk()

total = IntVar()  # defaults to 0

notebook = ttk.Notebook(root)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
frame4 = ttk.Frame(notebook)
frame5 = ttk.Frame(notebook)
frameSub = ttk.Frame(notebook)

main()

root.mainloop()
