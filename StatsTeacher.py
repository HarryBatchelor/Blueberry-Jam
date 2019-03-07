from tkinter import *
#from Results import *

class Stats(Frame):

    def __init__(self,master):
        super().__init__(master)
        self.pack()
        self.retrieveResults()
  
    def retrieveResults(self):
        students = 100

        sumM1T1 = 0
        sumM1T2 = 0

        sumM2T1 = 0
        sumM2T2 = 0

        sumM3T1 = 0
        sumM3T2 = 0

        self.txtDisplay = Text(self,height=14,width=85)
        self.txtDisplay.tag_configure('boldfont', font = ('MS', 8, 'bold'))
        self.txtDisplay.tag_configure('normfont', font = ('MS',8))

        tabResults = ""
        tabResults += ("\t"+"\t"+"\t"+"\t"+"\t")
        self.txtDisplay.insert(END, "TEST NUMBER: " + tabResults + "TEST 1" + "\t"
                                    + "TEST 2" + "\t" + "Total Avg." + "\n", 'boldfont')

        
        avgM1T1 = sumM1T1/students
        avgM1T2 = sumM1T2/students
        
        avgM2T1 = sumM2T1/students
        avgM2T2 = sumM2T2/students

        avgM3T1 = sumM3T1/students
        avgM3T2 = sumM3T2/students

        avgM1 = (avgM1T1 + avgM1T2) / 2
        avgM2 = (avgM2T1 + avgM2T2) / 2
        avgM3 = (avgM3T1 + avgM3T2) / 2


        self.txtDisplay.insert(END, "Module 1" + tabResults + "%.2f" %avgM1T1 + "\t" + "%.2f" %avgM1T2 + "\t" + "%.2f" %avgM1 + "\n", 'normfont')

        self.txtDisplay.insert(END, "Module 2" + tabResults + "%.2f" %avgM2T1 + "\t" + "%.2f" %avgM2T2 + "\t" + "%.2f" %avgM2+ "\n", 'normfont')

        self.txtDisplay.insert(END, "Module 3" + tabResults + "%.2f" %avgM3T1 + "\t" + "%.2f" %avgM3T2 + "\t" + "%.2f" %avgM3+ "\n", 'normfont')

        self.txtDisplay.pack()
