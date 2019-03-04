from tkinter import *
import tkinter.messagebox as tm
import sys
from FormativeTest import *

data_students = {"": ""}
data_lecturers = {"kirill": "123"}

class Software(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.logbtnlecturer = Button(self, text="Login Lecturer", command=self._login_btn_clicked_lecturer)
        self.logbtnlecturer.grid(columnspan=2)

        self.logbtnstudent = Button(self, text="Login Student", command=self._login_btn_clicked_student)
        self.logbtnstudent.grid(columnspan=2)

        self.regbtn = Button(self, text="Register (only for students)", command=self._register_btn_clicked)
        self.regbtn.grid(columnspan=2)

        self.leave_software = Button(self, text='Press Me to quit', command=self.quit)
        self.leave_software.grid(columnspan=2)

        self.pack()

    def _login_btn_clicked_student(self):

        username = self.entry_username.get()
        password = self.entry_password.get()

        if username in data_students and password == data_students[username]:
            tm.showinfo("Login Box", "Welcome " + username.capitalize())
            self.student_page()
        else:
            tm.showerror("Login error", "Incorrect username or password")

    def _login_btn_clicked_lecturer(self):

        username = self.entry_username.get()
        password = self.entry_password.get()

        if username in data_lecturers and password == data_lecturers[username]:
            tm.showinfo("Login Box", "Welcome " + username.capitalize())
            self.lecturer_page()
        else:
            tm.showerror("Login error", "Incorrect username or password")

    def _register_btn_clicked(self):

        username = self.entry_username.get()
        password = self.entry_password.get()

        if username in data_students:
            tm.showinfo("Register Box", "Username already taken")
        else:
            data_students[username]=password
            tm.showinfo("Register Box", "Your username was successfully added, log in")

    def quit(self):
        sys.exit()


    def student_page(self):
        window = Toplevel(root)
        self.take_summative = Button(window, text="Take Summative Test", command= self.summative_page)
        self.take_summative.grid(columnspan=2)

        self.take_formative = Button(window, text="Take Formative Test", command= self.formative_page)
        self.take_formative.grid(columnspan=2)

        self.results = Button(window, text="Results", command= self.results_page)
        self.results.grid(columnspan=2)

        self.leave = Button(window, text="Exit", command= self.quit)
        self.leave.grid(columnspan=2)



    def summative_page(self):
        window2 = Toplevel(root)
        self.leave = Button(window2, text="Exit", command= self.quit)
        self.leave.grid(columnspan=2)


    def formative_page(self):
        window3 = Toplevel(root)
        app = Quiz(window3)


    def results_page(self):
        window4 = Toplevel(root)
        self.leave = Button(window4, text="Exit", command= self.quit)
        self.leave.grid(columnspan=2)



    def lecturer_page(self):
        windowL = Toplevel(root)
        self.create_summative = Button(windowL, text = "Create Summative Test", command= self.create_summative)
        self.create_summative.grid(columnspan = 2)

        self.create_formative = Button(windowL, text = "Create Formative Test", command= self.create_formative)
        self.create_formative.grid(columnspan = 2)

        self.modify_summative = Button(windowL, text = "Modify a Summative Test", command= self.modify_summative)
        self.modify_summative.grid(columnspan = 2)

        self.modify_formative = Button(windowL, text = "Modify a Formative Test", command= self.modify_formative)
        self.modify_formative.grid(columnspan = 2)

        self.view_sum_stats = Button(windowL, text = "View Sumative Test Statistics", command= self.view_sum_stats)
        self.view_sum_stats.grid(columnspan = 2)

        self.view_form_stats = Button(windowL, text = "View Formative Test Statistics", command= self.view_form_stats)
        self.view_form_stats.grid(columnspan = 2)

        self.leave = Button(windowL, text="Exit", command= self.quit)
        self.leave.grid(columnspan=2)



    def create_summative(self):
        windowL2 = Toplevel(root)
        self.leave = Button(windowL2, text="Exit", command= self.quit)
        self.leave.grid(columnspan=2)
        #will put a view summative tests in this page if you'd like?


    def create_formative(self):
        windowL3 = Toplevel(root)
        self.leave = Button(windowL3, text="Exit", command= self.quit)
        self.leave.grid(columnspan=2)
        #will put a view formative tests in this page if you'd like?

    def modify_summative(self):
        windowL4 = Toplevel(root)
        self.leave = Button(windowL4, text="Exit", command= self.quit)
        self.leave.grid(columnspan=2)

    def modify_formative(self):
        windowL5 = Toplevel(root)
        self.leave = Button(windowL5, text="Exit", command= self.quit)
        self.leave.grid(columnspan=2)

    def view_sum_stats(self):
        windowL6 = Toplevel(root)
        self.leave = Button(windowL6, text="Exit", command= self.quit)
        self.leave.grid(columnspan=2)

    def view_form_stats(self):
        windowL7 = Toplevel(root)
        self.leave = Button(windowL7, text="Exit", command= self.quit)
        self.leave.grid(columnspan=2)



root = Tk()
lf = Software(root)
root.mainloop()
