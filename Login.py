from tkinter import *
import tkinter.messagebox as tm


data_students = {"william": "123"}
data_lecturers = {"kirill": "123"}

class LoginFrame(Frame):
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

        self.pack()

    def _login_btn_clicked_student(self):

        username = self.entry_username.get()
        password = self.entry_password.get()

        if username in data_students and password == data_students[username]:
            tm.showinfo("Login Box", "Welcome " + username.capitalize())
        else:
            tm.showerror("Login error", "Incorrect username or password")

    def _login_btn_clicked_lecturer(self):

        username = self.entry_username.get()
        password = self.entry_password.get()

        if username in data_lecturers and password == data_lecturers[username]:
            tm.showinfo("Login Box", "Welcome " + username.capitalize())
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

root = Tk()
lf = LoginFrame(root)
root.mainloop()
