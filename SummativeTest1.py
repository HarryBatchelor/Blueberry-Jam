from tkinter import *
import tkinter.messagebox

class SummativeTest1(Frame):
    def __init__(self, master ):
        Frame.__init__(self,master)
        self.grid()
        self.questionOne()
        self.questionTwo()

    def questionOne(self):
        lblOneA = Label (self, text='1) ', font=('MS', 8, 'bold'))
        lblOneA.grid(row=4, column=0)

        lblOneB = Label(self, text='What is 10+5?')
        lblOneB.grid(row=4, column=1, columnspan=2, sticky=W)

        lblWrongQ1A = Label(self, text = '7')
        lblWrongQ1A.grid(row=4, column=4)

        lblWrongQ1B = Label(self,text='13')
        lblWrongQ1B.grid(row=4, column=5)

        lblCorrectQ1 = Label(self, text='15')
        lblCorrectQ1.grid(row=4, column=6)

        lblWrongQ1C = Label(self,text='16')
        lblWrongQ1C.grid(row=4, column=7)


        self.varQ1 = IntVar()

        R1Q1 = Radiobutton(self, variable=self.varQ1, value=0)
        R1Q1.grid(row=5, column=4)

        R2Q1 = Radiobutton(self,variable=self.varQ1, value=2)
        R2Q1.grid(row=5, column=5)

        R3Q1 = Radiobutton(self,variable=self.varQ1, value=1)
        R3Q1.grid(row=5, column=6)
        #Value of 1 is the right answer
        R4Q1 = Radiobutton(self,variable=self.varQ1, value=3)
        R4Q1.grid(row=5, column=7)

    def questionTwo(self):
        lblTwoA = Label (self, text='2)', font=('MS', 8, 'bold'))
        lblTwoA.grid(row=6, column=0)

        lblTwoB = Label(self, text='What is 10x10?')
        lblTwoB.grid(row=6, column=1, columnspan=2, sticky=W)
        
        lblWrongQ2a = Label(self, text = '70')
        lblWrongQ2a.grid(row = 7, column = 4)

        lblWrongQ2b = Label(self, text = "1000")
        lblWrongQ2b.grid(row = 7, column = 5)

        lblWrongQ2c = Label(self,text = "10")
        lblWrongQ2c.grid(row = 7, column = 6)

        lblCorrectQ2 = Label(self, text = "100")
        lblCorrectQ2.grid(row = 7, column = 7)

        self.varQ2 = IntVar()

        R1Q2 = Radiobutton(self, variable=self.varQ2, value = 0)
        R1Q2.grid(row=8, column=4)

        R2Q2 = Radiobutton(self, variable=self.varQ2, value=2)
        R2Q2.grid(row=8, column=5)

        R3Q2 = Radiobutton(self, variable=self.varQ2, value = 3)
        R3Q2.grid(row=8, column=6)

        R4Q2 = Radiobutton(self, variable=self.varQ2, value=1)
        R4Q2.grid(row=8, column=7)
#Main
root = Tk()
root.title("Summative Test")
app = SummativeTest1(root)
root.mainloop()
