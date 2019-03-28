import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tm
import re
import tkinter.font as tkFont
from tkinter import ttk
import csv
import os
import datetime
import time

LARGE_FONT = ("Verdana", 12)


class main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "DQS Coursework 3")
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        style = ttk.Style()
        style.theme_use('clam')
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menu_bar = tk.Menu(container)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Save settings", command=lambda: tm.showinfo("Something",
                                                                                 "Hey There buddy keep it down"))
        file_menu.add_separator()
        menu_bar.add_cascade(label="File", menu=file_menu)

        tk.Tk.config(self, menu=menu_bar)

        self.frames = {}

        for F in (LoginPage, RegisterPage, DashboardStu, DashboardLec, SummativeTest, FormativeTest, Results, FeedbackPage, CreateFeedback, DetailedResults, CreateSummative, CreateFormative):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.label_username = ttk.Label(self, text="Username")
        self.label_password = ttk.Label(self, text="Password")

        self.entry_username = ttk.Entry(self)
        self.entry_password = ttk.Entry(self, show="*")

        self.label_username.grid(row=0, sticky='n', columnspan=2)
        self.label_password.grid(row=1, sticky='n', columnspan=2)
        self.entry_username.grid(row=0, column=2, columnspan=2)
        self.entry_password.grid(row=1, column=2, columnspan=2)

        self.btnLecturer = ttk.Button(self, text="Login Lecturer", command=lambda: self.login("lec", controller))
        self.btnLecturer.grid(columnspan=2)

        self.btnStudent = ttk.Button(self, text="Login Student", command=lambda: self.login("stu", controller))
        self.btnStudent.grid(columnspan=2)

        button1 = ttk.Button(self, text="Register", command=lambda: controller.show_frame(RegisterPage))
        button1.grid(columnspan=2)

    def login(self, cat, cont):

        username = self.entry_username.get()
        password = self.entry_password.get()

        if cat == "lec":
            if self.verify(username, password, "lec"):
                tm.showinfo("Login Box", "Welcome " + username.capitalize())
                current_users.append(str(username))
                self.entry_username.delete(0, 'end')
                self.entry_password.delete(0, 'end')
                return cont.show_frame(DashboardLec)
            else:
                tm.showerror("Login error", "Incorrect username or password")
        else:
            if self.verify(username, password, "stu"):
                tm.showinfo("Login Box", "Welcome " + username.capitalize())
                current_users.append(str(username))
                self.entry_username.delete(0, 'end')
                self.entry_password.delete(0, 'end')
                return cont.show_frame(DashboardStu)
            else:
                tm.showerror("Login error", "Incorrect username or password")

    def verify(self, username, password, cat):

        if cat == "lec":
            file = open("loginlecturer.txt", "r")
            trigger = False
            for line in file:
                line = line.split()
                if username == line[0]:
                    if password == line[1]:
                        trigger = True
            file.close()
            return trigger
        else:
            file2 = open("loginstudent.txt", "r")
            trigger = False
            for line in file2:
                line = line.split()
                if username == line[0]:
                    if password == line[1]:
                        trigger = True
            file2.close()
            return trigger


class RegisterPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Register", font=LARGE_FONT)
        label.grid(row=0, column=0)

        self.label_username = ttk.Label(self, text="Username")
        self.label_password = ttk.Label(self, text="Password")
        self.label_f_name = ttk.Label(self, text="First Name")
        self.label_surname = ttk.Label(self, text="Surname")
        self.label_id = ttk.Label(self, text="Student Id")
        self.label_email = ttk.Label(self, text="University Email")

        self.entry_username = ttk.Entry(self)
        self.entry_password = ttk.Entry(self, show="*")
        self.entry_f_name = ttk.Entry(self)
        self.entry_surname = ttk.Entry(self)
        self.entry_id = ttk.Entry(self)
        self.entry_email = ttk.Entry(self)

        self.label_username.grid(row=3, column=0)
        self.entry_username.grid(row=3, column=1)
        self.label_password.grid(row=4, column=0)
        self.entry_password.grid(row=4, column=1)
        self.label_f_name.grid(row=5, column=0)
        self.entry_f_name.grid(row=5, column=1)
        self.label_surname.grid(row=5, column=2)
        self.entry_surname.grid(row=5, column=3)
        self.label_id.grid(row=6, column=0)
        self.entry_id.grid(row=6, column=1)
        self.label_email.grid(row=7, column=0)
        self.entry_email.grid(row=7, column=1)

        mainframe = ttk.Frame(self)
        mainframe.grid(column=0, row=0)
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe.grid()

        tkvar = tk.StringVar(self)
        choices = {'', 'BSC-Computer_Science', 'BSC-Dentistry', 'BA-Business'}
        popupMenu = ttk.OptionMenu(self, tkvar, *choices)
        ttk.Label(self, text="Your degree: ").grid(row=9, column=0)
        popupMenu.grid(row=9, column=1)

        regbtn = ttk.Button(self, text="Register", command=lambda: self.registerStudent(tkvar.get(), controller))
        regbtn.grid(row=10, column=1)
        button1 = ttk.Button(self, text="Back to Login Page", command=lambda: controller.show_frame(LoginPage))
        button1.grid(row=11, column=1)


    def registerStudent(self, var, cont):

        username = self.entry_username.get()
        password = self.entry_password.get()
        f_name = self.entry_f_name.get()
        surname = self.entry_surname.get()
        id = self.entry_id.get()
        email = self.entry_email.get()
        infos = [username, password, var, f_name, surname, id, email]

        if self.isUsernameRepeated(username):
            tm.showinfo("Register Box", "Username already taken")
        elif len(username) < 5 or len(username) > 18 or (' ' in username):
            tm.showinfo("Register Box", "Length of username must be between 6 and 18 characters. No spaces")
        elif self.verifyPasswordRequirements(password):
            tm.showinfo("Register Box",
                        "Length of password must be between 6 and 18 characters. Must contain one number, one special character, and an upper letter. No spaces")
        elif var == "":
            tm.showinfo("Register Box", "You must choose a degree")
        elif len(f_name) < 3 or len(f_name) > 15:
            tm.showinfo("Register Box", "Length of first name must be between 3 and 15 characters.")
        elif len(surname) < 3 or len(surname) > 15:
            tm.showinfo("Register Box", "Length of surname must be between 3 and 15 characters.")
        elif len(id)<3:
            tm.showinfo("Register Box", "Input your student id")
        elif len(email)<8:
            tm.showinfo("Register Box", "Input your email")
        else:
            with open("loginstudent.txt", "a") as file:
                for info in infos:
                    file.write(info+" ")
                file.write("\n")
            file.close()
            tm.showinfo("Register Box",
                        "Welcome " + username + ". Please log in")
            cont.show_frame(LoginPage)
            self.entry_username.delete(0, 'end')
            self.entry_password.delete(0, 'end')
            self.entry_f_name.delete(0, 'end')
            self.entry_surname.delete(0, 'end')
            self.entry_id.delete(0, 'end')
            self.entry_email.delete(0, 'end')

    def isUsernameRepeated(self, inp_usernm):
        with open("loginstudent.txt","r") as file:
            for line in file:
                line = line.split()
                if inp_usernm == line[0]:
                    return True
                else:
                    return False

    def verifyPasswordRequirements(self, password):

        def check_special(input):

            specials = 0
            special_list = "! @ $ % ^ & * ( ) _ - + = { } [ ] | , . > < / ? ~ ` \" ' : ;".split()
            for char in input:
                if char in special_list:
                    specials += 1
            if specials > 0:
                return True
            else:
                return False

        if len(password) < 5 or len(password) > 18:
            return True
        elif not re.search("[a-z]", password):
            return True
        elif not re.search("[A-Z]", password):
            return True
        elif not re.search("[0-9]", password):
            return True
        elif not check_special(password):
            return True
        elif ' ' in password:
            return True
        else:
            return False


class DashboardStu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Dashboard Student", font=LARGE_FONT)
        label.grid(row=0, column=0, sticky='nsew')

        tests = ttk.Button(self, text="Take summative assessment", command=lambda: controller.show_frame(SummativeTest))
        tests.grid(row=1, column=0)

        testf = ttk.Button(self, text="Take formative assessment", command=lambda: controller.show_frame(FormativeTest))
        testf.grid(row=2, column=0)

        res = ttk.Button(self, text="View results", command=lambda: controller.show_frame(Results))
        res.grid(row=3, column=0)

        feed = ttk.Button(self, text="View feedback", command=lambda: controller.show_frame(FeedbackPage))
        feed.grid(row=4, column=0)

        button1 = ttk.Button(self, text="Back to Login Page", command=lambda: controller.show_frame(LoginPage))
        button1.grid(row=20, column=20)


class DashboardLec(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Dashboard Lecturer", font=LARGE_FONT)
        label.grid(row=0, column=0)

        tests = ttk.Button(self, text="Create summative assessment", command=lambda: controller.show_frame(CreateSummative))
        tests.grid(row=1, column=0)

        testf = ttk.Button(self, text="Create formative assessment", command=lambda: controller.show_frame(CreateFormative))
        testf.grid(row=2, column=0)

        res = ttk.Button(self, text="View results", command=lambda: controller.show_frame(DetailedResults))
        res.grid(row=3, column=0)

        feed = ttk.Button(self, text="Create feedback", command=lambda: controller.show_frame(CreateFeedback))
        feed.grid(row=4, column=0)

        button1 = ttk.Button(self, text="Back to Login Page", command=lambda: controller.show_frame(LoginPage))
        button1.grid()


class SummativeTest(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Summative Test", font=LARGE_FONT)
        label.grid(row=0, column=10)

        self.results = []
        self.question = []
        self.choice = tk.IntVar()
        self.username = ""
        self.deadline = ""

        # We want to display all the quizzes as buttons according to the user's degree
        # Get session username

        button1 = ttk.Button(self, text="Back to Student Dashboard",
                             command=lambda: controller.show_frame(DashboardStu))
        button1.grid(row=20)
        self.activatePage = ttk.Button(self, text="View Tests Available", command=lambda: self.user())
        self.activatePage.grid()

    def user(self):
        self.activatePage.config(state="disabled")
        self.username = current_users[-1]
        # Find student's degree using the data in the according txt file

        degree = ""
        file = open('loginstudent.txt', 'r')
        for line in file:
            line = line.split()
            if line[0] == self.username:
                degree = line[2]
        file.close()

        # Get Quiz Names according to fetched degree

        global names
        names = []
        with open('tests.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if line[1] == degree and line[4] == "Summative":
                    if not (line[0] in names):
                        names.append(line[0])
                        i = names.index(line[0])
                        ttk.Button(self, text=line[0],
                                   command=lambda i=i: self.createWindow(i)).grid()
        csv_file.close()

    def createWindow(self, index):
        self.results = []
        global window
        window = tk.Toplevel()
        window.geometry("500x400")
        global now, h
        now = datetime.datetime.now()
        with open("tests.csv") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if line[0] == names[index]:
                    h = int(line[6])
        self.deadline = (now + datetime.timedelta(minutes=h)).replace(microsecond=0)
        self.displayTest(index, 0, self.deadline)

    def displayTest(self, index, qu, deadline):
        self.question = []
        choice = tk.IntVar()
        ttk.Label(window, text=names[index]).grid()
        tk.Label(window, text="Finish by: " + str(self.deadline)).grid()

        # Questions and answers in a list called self.question

        with open("tests.csv") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if line[0] == names[index]:
                    self.question.append(line)
        csv_file.close()
        # Display Question according to qu which is the question number

        ttk.Label(window, text=self.question[qu][7]).grid()

        # Display options

        for i in range(len(self.question[qu]) - 9):
            ttk.Radiobutton(window, variable=choice, value=i + 9, text=self.question[qu][9 + i]).grid()

        # Next and submit button

        ttk.Button(window, text="Next/Submit", command=lambda: self.next(qu, index, choice.get(), deadline)).grid()

    def allChildren(self, win):
        _list = win.winfo_children()
        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())
        return _list

    def next(self, qu, index, choice, deadline):
        try:
            now = datetime.datetime.now()
            if now > deadline:
                tm.showinfo("Time", "You went out of time")
                score = 0
                nb_questions = 0
                with open("tests.csv") as csv_file3:
                    csv_reader = csv.reader(csv_file3)
                    for line in csv_reader:
                        if line[0] == names[index]:
                            nb_questions += 1
                to_add = nb_questions - len(self.results)
                for k in range(to_add):
                    self.results.append("0")
                if os.stat("results.csv").st_size == 0:
                    with open("results.csv", "w", newline='') as csv_file:
                        csv_writer = csv.writer(csv_file)
                        post = [self.username, names[index], "Formative", "1"]
                        for i in self.results:
                            post.append(i)
                        csv_writer.writerow(post)
                    csv_file.close()
                    for j in self.results:
                        score += int(j)
                    tm.showinfo("Test", "You scored: " + str(score) + " out of " + str(len(
                        self.results)) + ".End of test, you will be redirected towards your dashboard. Attempt nb: 1")
                else:
                    # Adds attempt number
                    attempt_nb = []
                    with open("results.csv", "r") as csv_file2:
                        csv_reader = csv.reader(csv_file2)
                        for line in csv_reader:
                            if names[index] == line[1] and line[0] == self.username:
                                attempt_nb.append(int(line[3]))
                    csv_file2.close()
                    try:
                        attempt = max(attempt_nb) + 1
                    except ValueError:
                        attempt = 1
                    # Writes all information to csv file
                    with open("results.csv", "a", newline='') as csv_file:
                        csv_writer = csv.writer(csv_file)
                        post = [self.username, names[index], "Formative", str(attempt)]
                        for i in self.results:
                            post.append(i)
                        csv_writer.writerow(post)
                    csv_file.close()
                    answers = []
                    for answer in self.question:
                        answers.append(answer[7])
                    answers = '. '.join(answers)
                    for j in self.results:
                        score += int(j)
                    tm.showinfo("Test", "You scored: " + str(score) + " out of " + str(len(
                        self.results)) + ". End of test, you will be redirected towards your dashboard. Attempt nb:" + str(
                        attempt) + ". The answer(s) were: " + answers)
            else:
                if self.question[qu][8] == self.question[qu][choice]:
                    self.results.append("1")
                else:
                    self.results.append("0")
                qu += 1
                widget_list = self.allChildren(window)
                for item in widget_list:
                    item.grid_forget()
                self.displayTest(index, qu, self.deadline)
        except IndexError:
            score = 0
            if os.stat("results.csv").st_size == 0:
                with open("results.csv", "w", newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    post = [self.username, names[index], "Formative", "1"]
                    for i in self.results:
                        post.append(i)
                    csv_writer.writerow(post)
                csv_file.close()
                for j in self.results:
                    score += int(j)
                tm.showinfo("Test", "You scored: " + str(score) + " out of " + str(
                    len(self.results)) + ".End of test, you will be redirected towards your dashboard. Attempt nb: 1")
            else:
                # Adds attempt number
                attempt_nb = []
                with open("results.csv", "r") as csv_file2:
                    csv_reader = csv.reader(csv_file2)
                    for line in csv_reader:
                        if names[index] == line[1] and line[0] == self.username:
                            attempt_nb.append(int(line[3]))
                csv_file2.close()
                try:
                    attempt = max(attempt_nb) + 1
                except ValueError:
                    attempt = 1
                # Writes all information to csv file
                with open("results.csv", "a", newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    post = [self.username, names[index], "Formative", str(attempt)]
                    for i in self.results:
                        post.append(i)
                    csv_writer.writerow(post)
                csv_file.close()
                answers = []
                for answer in self.question:
                    answers.append(answer[7])
                answers = '. '.join(answers)
                for j in self.results:
                    score += int(j)
                tm.showinfo("Test", "You scored: " + str(score) + " out of " + str(len(
                    self.results)) + ". End of test, you will be redirected towards your dashboard. Attempt nb:" + str(
                    attempt) + ". The answer(s) were: " + answers)
            window.destroy()
            window.after(500)




class FormativeTest(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Formative Test", font=LARGE_FONT)
        label.grid(row=0, column=10)
        self.results = []
        self.question = []
        self.choice = tk.IntVar()
        self.username = ""
        self.deadline = ""
        # We want to display all the quizzes as buttons according to the user's degree
        # Get session username
        button1 = ttk.Button(self, text="Back to Student Dashboard",
                             command=lambda: controller.show_frame(DashboardStu))
        button1.grid(row=20)
        self.activatePage = ttk.Button(self, text="View Tests Available", command=lambda: self.user())
        self.activatePage.grid()

    def user(self):
        self.activatePage.config(state="disabled")
        self.username = current_users[-1]
        # Find student's degree using the data in the according txt file

        degree = ""
        file = open('loginstudent.txt', 'r')
        for line in file:
            line = line.split()
            if line[0] == self.username:
                degree = line[2]
        file.close()

        # Get Quiz Names according to fetched degree

        global names
        names = []
        with open('tests.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if line[1] == degree and line[4] == "Formative":
                    if not (line[0] in names):
                        names.append(line[0])
                        i = names.index(line[0])
                        ttk.Button(self, text=line[0],
                                   command=lambda i=i: self.createWindow(i)).grid()
        csv_file.close()

    def createWindow(self, index):
        self.results = []
        global window
        window = tk.Toplevel()
        window.geometry("500x400")
        global now, h
        now = datetime.datetime.now()
        with open("tests.csv") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if line[0] == names[index]:
                    h = int(line[6])
        self.deadline = (now + datetime.timedelta(minutes=h)).replace(microsecond=0)
        self.displayTest(index,0,self.deadline)

    def displayTest(self, index, qu, deadline):
        self.question = []
        choice = tk.IntVar()
        ttk.Label(window, text=names[index]).grid()
        tk.Label(window, text="Finish by: " + str(self.deadline)).grid()

        # Questions and answers in a list called self.question

        with open("tests.csv") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if line[0] == names[index]:
                    self.question.append(line)
        csv_file.close()
        # Display Question according to qu which is the question number

        ttk.Label(window, text=self.question[qu][7]).grid()

        # Display options

        for i in range(len(self.question[qu]) - 9):
            ttk.Radiobutton(window, variable=choice, value=i + 9, text=self.question[qu][9 + i]).grid()

        # Next and submit button

        ttk.Button(window, text="Next/Submit", command=lambda: self.next(qu, index, choice.get(), deadline)).grid()


    def allChildren(self, win):
        _list = win.winfo_children()
        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())
        return _list

    def next(self, qu, index, choice, deadline):
        try:
            now = datetime.datetime.now()
            if now > deadline:
                tm.showinfo("Time", "You went out of time")
                score = 0
                nb_questions = 0
                with open("tests.csv") as csv_file3:
                    csv_reader = csv.reader(csv_file3)
                    for line in csv_reader:
                        if line[0] == names[index]:
                            nb_questions+=1
                to_add = nb_questions-len(self.results)
                for k in range(to_add):
                    self.results.append("0")
                if os.stat("results.csv").st_size == 0:
                    with open("results.csv", "w", newline='') as csv_file:
                        csv_writer = csv.writer(csv_file)
                        post = [self.username, names[index], "Formative", "1"]
                        for i in self.results:
                            post.append(i)
                        csv_writer.writerow(post)
                    csv_file.close()
                    for j in self.results:
                        score += int(j)
                    tm.showinfo("Test", "You scored: " + str(score) + " out of " + str(len(
                        self.results)) + ".End of test, you will be redirected towards your dashboard. Attempt nb: 1")
                else:
                    # Adds attempt number
                    attempt_nb = []
                    with open("results.csv", "r") as csv_file2:
                        csv_reader = csv.reader(csv_file2)
                        for line in csv_reader:
                            if names[index] == line[1] and line[0] == self.username:
                                attempt_nb.append(int(line[3]))
                    csv_file2.close()
                    try:
                        attempt = max(attempt_nb) + 1
                    except ValueError:
                        attempt = 1
                    # Writes all information to csv file
                    with open("results.csv", "a", newline='') as csv_file:
                        csv_writer = csv.writer(csv_file)
                        post = [self.username, names[index], "Formative", str(attempt)]
                        for i in self.results:
                            post.append(i)
                        csv_writer.writerow(post)
                    csv_file.close()
                    answers = []
                    for answer in self.question:
                        answers.append(answer[7])
                    answers = '. '.join(answers)
                    for j in self.results:
                        score += int(j)
                    tm.showinfo("Test", "You scored: " + str(score) + " out of " + str(len(self.results)) + ". End of test, you will be redirected towards your dashboard. Attempt nb:" + str(attempt) + ". The answer(s) were: " + answers)
            else:
                if self.question[qu][8] == self.question[qu][choice]:
                    self.results.append("1")
                else:
                    self.results.append("0")
                qu += 1
                widget_list = self.allChildren(window)
                for item in widget_list:
                    item.grid_forget()
                self.displayTest(index, qu, self.deadline)
        except IndexError:
            score = 0
            if os.stat("results.csv").st_size == 0:
                with open("results.csv", "w", newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    post = [self.username,names[index],"Formative","1"]
                    for i in self.results:
                        post.append(i)
                    csv_writer.writerow(post)
                csv_file.close()
                for j in self.results:
                    score += int(j)
                tm.showinfo("Test", "You scored: " + str(score) + " out of " + str(len(self.results)) + ".End of test, you will be redirected towards your dashboard. Attempt nb: 1")
            else:
                # Adds attempt number
                attempt_nb = []
                with open("results.csv", "r") as csv_file2:
                    csv_reader = csv.reader(csv_file2)
                    for line in csv_reader:
                        if names[index] == line[1] and line[0]==self.username:
                            attempt_nb.append(int(line[3]))
                csv_file2.close()
                try:
                    attempt = max(attempt_nb)+1
                except ValueError:
                    attempt = 1
                # Writes all information to csv file
                with open("results.csv", "a", newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    post = [self.username, names[index],"Formative", str(attempt)]
                    for i in self.results:
                        post.append(i)
                    csv_writer.writerow(post)
                csv_file.close()
                answers = []
                for answer in self.question:
                    answers.append(answer[7])
                answers = '. '.join(answers)
                for j in self.results:
                    score += int(j)
                tm.showinfo("Test", "You scored: " + str(score) + " out of " + str(len(self.results)) + ". End of test, you will be redirected towards your dashboard. Attempt nb:" + str(attempt) +". The answer(s) were: "+ answers)
            window.destroy()
            window.after(500)


class Results(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Results", font=LARGE_FONT)
        label.grid(row=0, column=10)

        button1 = ttk.Button(self, text="Back to Student Dashboard", command=lambda: controller.show_frame(DashboardStu))
        button1.grid()


class FeedbackPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Feedback Page", font=LARGE_FONT)
        label.grid(row=0, column=10)

        button1 = ttk.Button(self, text="Back to Student Dashboard", command=lambda: controller.show_frame(DashboardStu))
        button1.grid()

class CreateSummative(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Create Summative Test", font=LARGE_FONT)
        label.grid(row=0, column=10)

        button1 = ttk.Button(self, text="Back to Lecturer Dashboard", command=lambda: controller.show_frame(DashboardLec))
        button1.grid()


class CreateFormative(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Create Formative Test", font=LARGE_FONT)
        label.grid(row=0, column=10)

        button1 = ttk.Button(self, text="Back to Lecturer Dashboard", command=lambda: controller.show_frame(DashboardLec))
        button1.grid()


class DetailedResults(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Detailed results", font=LARGE_FONT)
        label.grid(row=0, column=10)

        button1 = ttk.Button(self, text="Back to Lecturer Dashboard", command=lambda: controller.show_frame(DashboardLec))
        button1.grid()


class CreateFeedback(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Create Feedback", font=LARGE_FONT)
        label.grid(row=0, column=10)

        button1 = ttk.Button(self, text="Back to Lecturer Dashboard", command=lambda: controller.show_frame(DashboardLec))
        button1.grid()


current_users = ["Nothing"]
# To get session username, type <current_users[-1]>
app = main()
app.geometry("1280x720")
app.mainloop()
