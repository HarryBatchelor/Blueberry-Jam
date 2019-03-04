from tkinter import *
import tkinter.messagebox

q = [
    "What is Tkinter?",
    "What is Turtle?",
    "What does the 'Print' command do?",
    "What Type of language is python?"
    "Submit The test"

]

options = [
    ["A Guided User Interface", "A Variable", "A Function", "None of the above"],
    ["A module", "A boolean Value", "A Guided User Interface", "None of the abovve"],
    ["Create a window", "Show a message in the Python shell", "Print to the printer", "None of above"],
    ["A low level language", "An object orientated language", "A high level language", "None of the above"],
    ["Submit"]


]
a = [1, 1, 2, 3]


class Quiz:
    def __init__(self, master):
        self.opt_selected = IntVar()
        self.qn = 0
        self.correct = 0
        self.ques = self.create_q(master, self.qn)
        self.opts = self.create_options(master, 4)
        self.display_q(self.qn)
        self.status_bar = self.create_status_bar(master)
        self.create_nav(master)
        # self.storeResponse()

    def create_status_bar(self, master):
        status_bar = Label(master, text='Please choose the right answer')
        status_bar.pack(side=BOTTOM, fill=X)
        return status_bar

    def create_nav(self, master):
        button = Button(master, text="Back", command=self.back_btn)
        button.pack(side=BOTTOM)
        button = Button(master, text="Next", command=self.next_btn)
        button.pack(side=BOTTOM)
        button = Button(master, text="Submit", command=self.sub_btn)
        button.pack(side=BOTTOM)

    def create_q(self, master, qn):
        w = Label(master, text=q[qn])
        w.pack(side=TOP)
        return w

    def create_options(self, master, n):
        b_val = 0
        b = []
        while b_val < n:
            btn = Radiobutton(master, text="Please choose the right answer", variable=self.opt_selected, value=b_val + 1)
            b.append(btn)
            btn.pack(side=TOP, anchor="w")
            b_val = b_val + 1
        return b

    def display_q(self, qn):
        b_val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        for op in options[qn]:
            self.opts[b_val]['text'] = op
            b_val = b_val + 1

    def check_q(self, qn):
        if self.opt_selected.get() == a[qn]:
            return True
        return False

    def print_results(self):
        result = "Score: " + str(self.correct) + "/" + str(len(q))
        tkinter.messagebox.showinfo("Final Result", result)
        print("Score: " + str(self.correct) + "/" + str(len(q)))

    def back_btn(self):
        print("go back")

    def next_btn(self):
        if self.check_q(self.qn):
            self.status_bar['text'] = "Correct"
            self.correct += 1
        else:
            self.status_bar['text'] = "Wrong"
        self.qn = self.qn + 1
        if self.qn >= len(q):
            self.print_results()
        else:
            self.display_q(self.qn)
    def sub_btn(self):
        sub_btn["command"] = self.storeResponse
    def storeResponse(self):
        import shelve
        db = shelve.open('responsedb')




root = Tk()
root.title("Welcome to the Python test")
root.geometry("400x300")
app = Quiz(root)
root.mainloop()
