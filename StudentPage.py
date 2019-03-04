from tkinter import *

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):

        self.master.title("Student Page")

        self.pack(fill=BOTH, expand=1)

        sumButton = Button(self, text="Summative Assessment")

        sumButton.place(x=10, y=10)

        formButton = Button(self, text="Formative Assessment")

        formButton.place(x=10, y=40)

        resButton = Button(self, text="Results")

        resButton.place(x=10, y=70)

        gobackButton = Button(self, text="Go Back")

        gobackButton.place(x=167, y=240)

        

        


root = Tk()#Tk is part of Tkinter, calls the root the main window
root.geometry("400x300")

app = Window(root)

root.mainloop