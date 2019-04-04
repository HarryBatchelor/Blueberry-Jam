import tkinter as tk
from tkinter import font
import tkinter.messagebox as tm
import re
from tkinter import ttk
import csv
import os
import datetime
import numpy as np
import matplotlib.pyplot as plt

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
        file_menu.add_command(label="Say Hello", command=lambda: tm.showinfo("Message",
                                                                                 "Hello There!"))
        file_menu.add_separator()
        menu_bar.add_cascade(label="File", menu=file_menu)

        tk.Tk.config(self, menu=menu_bar)

        self.frames = {}

        for F in (LoginPage, RegisterPage, DashboardStu, DashboardLec, SummativeTest, FormativeTest, Results, FeedbackPage, DetailedResults, CreateSummative, CreateFormative):

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

        frame = tk.Frame(self)
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        label = tk.Label(self, text="Login", font=LARGE_FONT, background="aquamarine2")
        label.grid(row=0, column=0)

        bg_image = tk.PhotoImage(file="bg2.png")
        bg_label = tk.Label(self, image=bg_image)
        bg_label.image = bg_image
        bg_label.place(relwidth=1, relheight=1)

        self.label_username = tk.Label(self, text="Username", background='orange red')
        self.label_username.config(font=("Courier", 30))
        self.label_password = tk.Label(self, text="Password", background='orange red')
        self.label_password.config(font=("Courier", 30))

        self.entry_username = ttk.Entry(self)
        self.entry_username.config(font=("Courier", 30))
        self.entry_password = ttk.Entry(self, show="*")
        self.entry_password.config(font=("Courier", 30))

        self.label_username.place(relx=0.2, rely=0.2)
        self.label_password.place(relx=0.2, rely=0.3)
        self.entry_username.place(relx=0.4, rely=0.2)
        self.entry_password.place(relx=0.4, rely=0.3)

        self.btnLecturer = tk.Button(self, text="Login Lecturer", command=lambda: self.login("lec", controller), background='green4')
        self.btnLecturer.config(height=2, width=15, font=("Courier", 19))
        self.btnLecturer.place(relx=0.28, rely=0.4)

        self.btnStudent = tk.Button(self, text="Login Student", command=lambda: self.login("stu", controller), background='green4')
        self.btnStudent.config(height=2, width=15, font=("Courier", 19))
        self.btnStudent.place(relx=0.5, rely=0.4)

        self.button1 = tk.Button(self, text="Register", command=lambda: controller.show_frame(RegisterPage), background='red4')
        self.button1.config(height=3, width=15, font=("Courier", 10, 'bold'))
        self.button1.place(relx=0.8, rely=0.05)

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

        frame = tk.Frame(self)
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        label = tk.Label(self, text="Register", font=LARGE_FONT, background='red4')
        label.grid(row=0, column=0)

        bg_image = tk.PhotoImage(file="bg2.png")
        bg_label = tk.Label(self, image=bg_image)
        bg_label.image = bg_image
        bg_label.place(relwidth=1, relheight=1)

        self.label_username = tk.Label(self, text="Username", background='orange red')
        self.label_username.config(font=("Courier", 20))
        self.label_password = tk.Label(self, text="Password", background='orange red')
        self.label_password.config(font=("Courier", 20))
        self.label_f_name = tk.Label(self, text="First Name", background='orange red')
        self.label_f_name.config(font=("Courier", 20))
        self.label_surname = tk.Label(self, text="Surname", background='orange red')
        self.label_surname.config(font=("Courier", 20))
        self.label_id = tk.Label(self, text="Student Id", background='orange red')
        self.label_id.config(font=("Courier", 20))
        self.label_email = tk.Label(self, text="University Email", background='orange red')
        self.label_email.config(font=("Courier", 20))

        self.entry_username = ttk.Entry(self)
        self.entry_username.config(font=("Courier", 20))
        self.entry_password = ttk.Entry(self, show="*")
        self.entry_password.config(font=("Courier", 20))
        self.entry_f_name = ttk.Entry(self)
        self.entry_f_name.config(font=("Courier", 20))
        self.entry_surname = ttk.Entry(self)
        self.entry_surname.config(font=("Courier", 20))
        self.entry_id = ttk.Entry(self)
        self.entry_id.config(font=("Courier", 20))
        self.entry_email = ttk.Entry(self)
        self.entry_email.config(font=("Courier", 20))

        self.label_username.place(relx=0.2, rely=0.1)
        self.entry_username.place(relx=0.45, rely=0.1)
        self.label_password.place(relx=0.2, rely=0.16)
        self.entry_password.place(relx=0.45, rely=0.16)
        self.label_f_name.place(relx=0.2, rely=0.22)
        self.entry_f_name.place(relx=0.45, rely=0.22)
        self.label_surname.place(relx=0.2, rely=0.28)
        self.entry_surname.place(relx=0.45, rely=0.28)
        self.label_id.place(relx=0.2, rely=0.34)
        self.entry_id.place(relx=0.45, rely=0.34)
        self.label_email.place(relx=0.2, rely=0.40)
        self.entry_email.place(relx=0.45, rely=0.40)

        mainframe = ttk.Frame(self)
        mainframe.grid(column=0, row=0)
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe.grid()

        tkvar = tk.StringVar(self)
        choices = {'', 'BSC-Computer_Science', 'BSC-Dentistry', 'BA-Business'}
        popupMenu = tk.OptionMenu(self, tkvar, *choices)
        self.label_degree = tk.Label(self, text="Your degree: ", background='orange red')
        self.label_degree.place(relx=0.2, rely=0.5)
        self.label_degree.config(font=("Courier", 20))
        popupMenu.config(width=8, height=2, background='red', font=("Courier", 20))
        tkvar.set("Press me")
        popupMenu.place(relx=0.5, rely=0.48)

        regbtn = tk.Button(self, text="Register", background="RoyalBlue1", command=lambda: self.registerStudent(tkvar.get(), controller))
        regbtn.config(height=2, width=13, font=("Courier", 25))
        regbtn.place(relx=0.4, rely=0.63)
        button1 = tk.Button(self, text="Back", background="MistyRose4", command=lambda: controller.show_frame(LoginPage))
        button1.config(height=2, width=13, font=("Courier", 25))
        button1.place(relx=0.4, rely=0.8)


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
        elif len(username) < 5 or len(username) > 18 or (' ' in username) or (',' in username):
            tm.showinfo("Register Box", "Length of username must be between 6 and 18 characters. No spaces, no commas.")
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

        frame = tk.Frame(self)
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        bg_image = tk.PhotoImage(file="bg.png")
        bg_label = tk.Label(self, image=bg_image)
        bg_label.image = bg_image
        bg_label.place(relwidth=1, relheight=1)

        label = tk.Label(self, text="Student Dashboard", font=LARGE_FONT)
        label.config(font=("Courier", 25), background="cyan")
        label.place(relx=0.35, rely=0.2)

        tests = tk.Button(self, text="Summative", background="turquoise", command=lambda: controller.show_frame(SummativeTest))
        tests.config(height=2, width=13, font=("Courier", 25))
        tests.place(relx=0.55, rely=0.3)

        testf = tk.Button(self, text="Formative", background="turquoise", command=lambda: controller.show_frame(FormativeTest))
        testf.config(height=2, width=13, font=("Courier", 25))
        testf.place(relx=0.25, rely=0.3)

        res = tk.Button(self, text="View results", background="turquoise", command=lambda: controller.show_frame(Results))
        res.config(height=2, width=13, font=("Courier", 25))
        res.place(relx=0.55, rely=0.45)

        feed = tk.Button(self, text="Feedback", background="turquoise", command=lambda: controller.show_frame(FeedbackPage))
        feed.config(height=2, width=13, font=("Courier", 25))
        feed.place(relx=0.25, rely=0.45)

        button1 = tk.Button(self, text="Back", background="MistyRose4", command=lambda: controller.show_frame(LoginPage))
        button1.config(height=2, width=13, font=("Courier", 25))
        button1.place(relx=0.39, rely=0.6)


class DashboardLec(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = tk.Frame(self)
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        bg_image = tk.PhotoImage(file="bg3.png")
        bg_label = tk.Label(self, image=bg_image)
        bg_label.image = bg_image
        bg_label.place(relwidth=1, relheight=1)

        label = tk.Label(self, text="Dashboard Lecturer", font=LARGE_FONT)
        label.config(font=("Courier", 25), background="saddle brown")
        label.place(relx=0.35, rely=0.2)

        tests = tk.Button(self, text="Summative", background="DarkOrange4", command=lambda: controller.show_frame(CreateSummative))
        tests.config(height=2, width=13, font=("Courier", 25))
        tests.place(relx=0.55, rely=0.3)

        testf = tk.Button(self, text="Formative", background="DarkOrange4", command=lambda: controller.show_frame(CreateFormative))
        testf.config(height=2, width=13, font=("Courier", 25))
        testf.place(relx=0.25, rely=0.3)

        res = tk.Button(self, text="View results", background="DarkOrange4", command=lambda: controller.show_frame(DetailedResults))
        res.config(height=2, width=13, font=("Courier", 25))
        res.place(relx=0.55, rely=0.45)

        button1 = tk.Button(self, text="Back", background="MistyRose4",
                            command=lambda: controller.show_frame(LoginPage))
        button1.config(height=2, width=13, font=("Courier", 25))
        button1.place(relx=0.39, rely=0.6)


class SummativeTest(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = tk.Frame(self)
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        bg_image = tk.PhotoImage(file="bg3.png")
        bg_label = tk.Label(self, image=bg_image)
        bg_label.image = bg_image
        bg_label.place(relwidth=1, relheight=1)

        label = tk.Label(self, text="Summative Test", font=LARGE_FONT)
        label.config(font=("Courier", 25), background="saddle brown")
        label.place(relx=0.385, rely=0.2)

        self.results = []
        self.question = []
        self.choice = tk.IntVar()
        self.username = ""
        self.timer = ""

        # We want to display all the quizzes as buttons according to the user's degree
        # Get session username
        button1 = tk.Button(self, text="Back", background="MistyRose4",
                            command=lambda: controller.show_frame(DashboardStu))
        button1.config(height=2, width=13, font=("Courier", 25))
        button1.place(relx=0.39, rely=0.8)
        self.activatePage = tk.Button(self, text="Load Tests", background='firebrick4', command=lambda: self.user())
        self.activatePage.config(font=("Courier", 25))
        self.activatePage.place(relx=0.41, rely=0.32)

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
            next(csv_file)
            csv_reader = csv.reader(csv_file)
            counter = 0.39
            for line in csv_reader:
                if line[1] == degree and line[4] == "Summative":
                    if not (line[0] in names):
                        a = datetime.datetime.strptime(line[5], "%d/%m/%y")
                        b = datetime.datetime.now()
                        names.append(line[0])
                        i = names.index(line[0])
                        if a < b:
                            counter += 0.035
                            tk.Button(self, text=line[0] + " - " + line[2] + ". Put online by: " + line[
                                3] + ". To be completed by: " + line[5], font=("Courier", 8), background='dark sea green',
                                       command=lambda i=i: self.late(i)).place(relx=0.26, rely=counter)
                        else:
                            counter += 0.035
                            names.append(line[0])
                            i = names.index(line[0])
                            tk.Button(self, text=line[0]+" - " +line[2] + ". Put online by: " + line[3] + ". To be completed by: "+ line[5], font=("Courier", 8), background='dark sea green',
                                       command=lambda i=i: self.createWindow(i)).place(relx=0.26, rely=counter)
        csv_file.close()

    def late(self, index):
        tm.showinfo("Error", "You cannot take this test after the deadline")

        self.trigger = False
        with open("results.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if line[1] == names[index]:
                    self.trigger = True

        if self.trigger == False:
            nb_questions = 0
            with open("tests.csv", "r") as csv_file2:
                csv_reader = csv.reader(csv_file2)
                for line in csv_reader:
                    if line[0] == names[index]:
                        nb_questions += 1
            with open("results.csv", "w", newline='') as csv_file3:
                csv_writer = csv.writer(csv_file3)
                post = [self.username, names[index], "Summative", "1"]
                for i in range(nb_questions):
                    post.append("0")
                csv_writer.writerow(post)
            csv_file2.close()
            csv_file3.close()

        csv_file.close()
        self.trigger = False


    def createWindow(self, index):

        global now, h
        global window
        self.username = current_users[-1]
        self.results = []
        complete = 0
        with open("results.csv") as csv_file4:
            csv_reader = csv.reader(csv_file4)
            for line in csv_reader:
                if line[1] == names[index] and line[0] == self.username:
                    if line[3] == "1":
                        tm.showinfo("Page", "You can only take this test once")
                        complete += 1
        if complete == 0:
            window = tk.Toplevel()
            window.geometry("1280x720")
            now = datetime.datetime.now()
            with open("tests.csv") as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    if line[0] == names[index]:
                        h = int(line[6])
            self.timer = (now + datetime.timedelta(minutes=h)).replace(microsecond=0)
            self.displayTest(index, 0, self.timer)


    def displayTest(self, index, qu, timer):

        frame = tk.Frame(window, bg="#e3dfe4")
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        self.question = []
        choice = tk.IntVar()
        label_test_name = tk.Label(window, text=names[index], background='slate gray')
        label_test_name.config(font=("Courier", 15))
        label_test_name.place(relx=0.1, rely=0.1)

        label_finish = tk.Label(window, text="Finish by: " + str(self.timer), background='light pink')
        label_finish.config(font=("Courier", 13))
        label_finish.place(relx=0.6, rely=0.1)

        # Questions and answers in a list called self.question

        with open("tests.csv") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if line[0] == names[index]:
                    self.question.append(line)
        csv_file.close()
        # Display Question according to qu which is the question number

        question = ttk.Label(window, text=self.question[qu][7], background='NavajoWhite4')
        question.config(font=("Courier", 17))
        question.place(relx=0.15, rely=0.15)


        # Display options

        counter = 0.2
        for i in range(len(self.question[qu]) - 9):
            counter += 0.05
            tk.Radiobutton(window, variable=choice, value=i + 9, text=self.question[qu][9 + i], font=("Courier", 13)).place(relx=0.13, rely=counter)


        # Next and submit button

        btn_nex = tk.Button(window, text="Next/Submit", background="coral", command=lambda: self.next(qu, index, choice.get(), timer))
        btn_nex.config(font=("Courier", 25))
        btn_nex.place(relx=0.39, rely=0.8)

    def allChildren(self, win):
        _list = win.winfo_children()
        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())
        return _list

    def next(self, qu, index, choice, timer):
        try:
            now = datetime.datetime.now()
            if now > timer:
                tm.showinfo("Time", "You went out of time")
                score = 0
                nb_questions = 0
                with open("tests.csv", "r") as csv_file3:
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
                        post = [self.username, names[index], "Summative", "1"]
                        for i in self.results:
                            post.append(i)
                        csv_writer.writerow(post)
                    csv_file.close()
                    answers = []
                    for answer in self.question:
                        answers.append(answer[8])
                    answers = ' - '.join(answers)
                    for j in self.results:
                        score += int(j)
                    tm.showinfo("Test", "You scored: " + str(score) + " out of " + str(len(
                        self.results)) + ". End of test, you will be redirected towards your dashboard. Attempt nb: 1."
                                + " The answer(s) were: " + answers)
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
                        post = [self.username, names[index], "Summative", str(attempt)]
                        for i in self.results:
                            post.append(i)
                        csv_writer.writerow(post)
                    csv_file.close()
                    for j in self.results:
                        score += int(j)
                    tm.showinfo("Test", "You scored: " + str(score) + " out of " + str(len(
                        self.results)) + ". End of test, you will be redirected towards your dashboard. Attempt nb:" + str(
                        attempt) + ". The answer(s) will be available after the deadline.")
            else:
                if self.question[qu][8] == self.question[qu][choice]:
                    self.results.append("1")
                else:
                    self.results.append("0")
                qu += 1
                widget_list = self.allChildren(window)
                for item in widget_list:
                    item.grid_forget()
                self.displayTest(index, qu, timer)

        except IndexError:
            score = 0
            if os.stat("results.csv").st_size == 0:
                with open("results.csv", "w", newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    post = [self.username, names[index], "Summative", "1"]
                    for i in self.results:
                        post.append(i)
                    csv_writer.writerow(post)
                csv_file.close()
                for j in self.results:
                    score += int(j)
                tm.showinfo("Test", "You scored: " + str(score) + " out of " + str(
                    len(self.results)) + ".End of test, you will be redirected towards your dashboard. Attempt nb: 1. The answer(s) will be available after the deadline.")
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
                    post = [self.username, names[index], "Summative", str(attempt)]
                    for i in self.results:
                        post.append(i)
                    csv_writer.writerow(post)
                csv_file.close()
                for j in self.results:
                    score += int(j)
                tm.showinfo("Test", "You scored: " + str(score) + " out of " + str(len(
                    self.results)) + ". End of test, you will be redirected towards your dashboard. Attempt nb:" + str(
                    attempt) + ". The answer(s) will be available after the deadline.")
            window.destroy()
            window.after(500)


class FormativeTest(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = tk.Frame(self)
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        bg_image = tk.PhotoImage(file="bg4.png")
        bg_label = tk.Label(self, image=bg_image)
        bg_label.image = bg_image
        bg_label.place(relwidth=1, relheight=1)

        label = tk.Label(self, text="Formative Test", font=LARGE_FONT)
        label.config(font=("Courier", 25), background="saddle brown")
        label.place(relx=0.385, rely=0.2)

        self.results = []
        self.question = []
        self.choice = tk.IntVar()
        self.username = ""
        self.timer = ""
        # We want to display all the quizzes as buttons according to the user's degree
        # Get session username
        button1 = tk.Button(self, text="Back", background="MistyRose4",
                            command=lambda: controller.show_frame(DashboardStu))
        button1.config(height=2, width=13, font=("Courier", 25))
        button1.place(relx=0.39, rely=0.8)

        self.activatePage = tk.Button(self, text="Load Tests", background='cornflower blue',
                                      command=lambda: self.user())
        self.activatePage.config(font=("Courier", 25))
        self.activatePage.place(relx=0.41, rely=0.32)

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
            next(csv_file)
            csv_reader = csv.reader(csv_file)
            counter = 0.39
            for line in csv_reader:
                if line[1] == degree and line[4] == "Formative":
                    if not (line[0] in names):
                        a = datetime.datetime.strptime(line[5], "%d/%m/%y")
                        b = datetime.datetime.now()
                        if a < b:
                            counter += 0.035
                            names.append(line[0])
                            i = names.index(line[0])
                            tk.Button(self, text=line[0] + " - " + line[2] + ". Put online by: " + line[
                                3] + ". To be completed by: " + line[5], font=("Courier", 8), background='DeepSkyBlue2',
                                       command=lambda i=i: self.late(i)).place(relx=0.26, rely=counter)
                        else:
                            counter += 0.035
                            names.append(line[0])
                            i = names.index(line[0])
                            tk.Button(self, text=line[0] + " - " + line[2] + ". Put online by: " + line[
                                3] + ". To be completed by: " + line[5], font=("Courier", 8), background='DeepSkyBlue2',
                                       command=lambda i=i: self.createWindow(i)).place(relx=0.26, rely=counter)
        csv_file.close()

    def late(self, index):
        tm.showinfo("Error", "You cannot take this test after the deadline")

        self.trigger = False
        with open("results.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if line[1] == names[index]:
                    self.trigger = True

        if self.trigger == False:
            nb_questions = 0
            with open("tests.csv", "r") as csv_file2:
                csv_reader = csv.reader(csv_file2)
                for line in csv_reader:
                    if line[0] == names[index]:
                        nb_questions += 1
            with open("results.csv", "w", newline='') as csv_file3:
                csv_writer = csv.writer(csv_file3)
                post = [self.username, names[index], "Formative", "1"]
                for i in range(nb_questions):
                    post.append("0")
                csv_writer.writerow(post)
            csv_file2.close()
            csv_file3.close()

        csv_file.close()
        self.trigger = False

    def createWindow(self, index):
        self.results = []
        global window
        window = tk.Toplevel()
        window.geometry("1280x720")
        global now, h
        now = datetime.datetime.now()
        with open("tests.csv") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if line[0] == names[index]:
                    h = int(line[6])
        self.timer = (now + datetime.timedelta(minutes=h)).replace(microsecond=0)
        self.displayTest(index, 0, self.timer)

    def displayTest(self, index, qu, timer):

        frame = tk.Frame(window, bg="#e3dfe4")
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        self.question = []
        choice = tk.IntVar()

        label_finish = tk.Label(window, text="Finish by: " + str(self.timer), background='light pink')
        label_finish.config(font=("Courier", 13))
        label_finish.place(relx=0.6, rely=0.1)

        label_test_name = tk.Label(window, text=names[index], background='slate gray')
        label_test_name.config(font=("Courier", 15))
        label_test_name.place(relx=0.1, rely=0.1)



        # Questions and answers in a list called self.question

        with open("tests.csv") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if line[0] == names[index]:
                    self.question.append(line)
        csv_file.close()
        # Display Question according to qu which is the question number

        question = ttk.Label(window, text=self.question[qu][7], background='NavajoWhite4')
        question.config(font=("Courier", 17))
        question.place(relx=0.15, rely=0.15)

        # Display options

        counter = 0.2
        for i in range(len(self.question[qu]) - 9):
            counter += 0.05
            tk.Radiobutton(window, variable=choice, value=i + 9, text=self.question[qu][9 + i], font=("Courier", 13)).place(relx=0.13, rely=counter)


        # Next and submit button

        btn_nex = tk.Button(window, text="Next/Submit", background="coral", command=lambda: self.next(qu, index, choice.get(), timer))
        btn_nex.config(font=("Courier", 25))
        btn_nex.place(relx=0.39, rely=0.8)

    def allChildren(self, win):
        _list = win.winfo_children()
        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())
        return _list

    def next(self, qu, index, choice, timer):
        try:
            now = datetime.datetime.now()
            if now > timer:
                tm.showinfo("Time", "You went out of time")
                score = 0
                nb_questions = 0
                with open("tests.csv", "r") as csv_file3:
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
                    answers = []
                    for answer in self.question:
                        answers.append(answer[8])
                    answers = '. '.join(answers)
                    for j in self.results:
                        score += int(j)
                    tm.showinfo("Test", "You scored: " + str(score) + " out of " + str(len(self.results)) + ". End of test, you will be redirected towards your dashboard. Attempt nb:1." + ". The answer(s) were: " + answers)
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
                        answers.append(answer[8])
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
                self.displayTest(index, qu, timer)
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
                answers = []
                for answer in self.question:
                    answers.append(answer[8])
                answers = '. '.join(answers)
                for j in self.results:
                    score += int(j)
                tm.showinfo("Test", "You scored: " + str(score) + " out of " + str(len(
                    self.results)) + ". End of test, you will be redirected towards your dashboard. Attempt nb:1" + ". The answer(s) were: " + answers)
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
                    post = [self.username, names[index], "Formative", str(attempt)]
                    for i in self.results:
                        post.append(i)
                    csv_writer.writerow(post)
                csv_file.close()
                answers = []
                for answer in self.question:
                    answers.append(answer[8])
                answers = '. '.join(answers)
                for j in self.results:
                    score += int(j)
                tm.showinfo("Test", "You scored: " + str(score) + " out of " + str(len(self.results)) + ". End of test, you will be redirected towards your dashboard. Attempt nb:" + str(attempt) +". The answer(s) were: "+ answers)
            window.destroy()
            window.after(500)


class Results(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = tk.Frame(self)
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        bg_image = tk.PhotoImage(file="bg5.png")
        bg_label = tk.Label(self, image=bg_image)
        bg_label.image = bg_image
        bg_label.place(relwidth=1, relheight=1)

        label = tk.Label(self, text="Results", font=LARGE_FONT)
        label.config(font=("Courier", 25), background="forest green")
        label.place(relx=0.435, rely=0.2)

        button1 = tk.Button(self, text="Back", background="MistyRose4",
                            command=lambda: controller.show_frame(DashboardStu))
        button1.config(height=2, width=13, font=("Courier", 25))
        button1.place(relx=0.39, rely=0.6)

        self.username = ''
        self.results_s = {}
        self.results_f = {}
        self.deadline_s = []
        self.deadline_f = []
        self.module_id = []
        self.activate = tk.Button(self, text="View grades", background='SeaGreen1', command=lambda: self.viewg())
        self.activate.config(font=("Courier", 25))
        self.activate.place(relx=0.4, rely=0.32)

    def viewg(self):

        self.activate.config(state='disabled')
        self.username = current_users[-1]

        if os.stat("results.csv").st_size == 0:
            tm.showinfo("Error", "No results available")
        else:
            with open("results.csv", "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    if line[0] == self.username and line[2] == "Summative":
                        self.results_s[line[1]] = line[4:]
                    elif line[0] == self.username and line[2] == "Formative" and line[3] == "1":
                        self.results_f[line[1]] = line[4:]
            csv_file.close()

        if self.results_s:
            for result in self.results_s:
                score = 0
                total = 0
                for i in self.results_s[result]:
                    score += int(i)
                    total += 1
                self.results_s[result] = (round((score / total) * 100, 2))

        if self.results_f:
            for result in self.results_f:
                score = 0
                total = 0
                for i in self.results_f[result]:
                    score += int(i)
                    total += 1
                self.results_f[result] = (round((score / total) * 100, 2))

        if os.stat("tests.csv").st_size != 0 and os.stat("results.csv").st_size != 0:
            for i in self.results_s:
                with open("tests.csv", "r") as csv_file:
                    csv_reader = csv.reader(csv_file)
                    for line in csv_reader:
                        if line[0] == i:
                            if not (line[5] in self.deadline_s):
                                self.deadline_s.append(line[5])
                            elif not (line[2] in self.module_id):
                                self.module_id.append(line[2])
            for i in self.results_f:
                with open("tests.csv", "r") as csv_file:
                    csv_reader = csv.reader(csv_file)
                    for line in csv_reader:
                        if line[0] == i:
                            if not (line[5] in self.deadline_f):
                                self.deadline_f.append(line[5])
                            elif not (line[2] in self.module_id):
                                self.module_id.append(line[2])

        if self.results_s:
            counter = 0.4
            for count, line in enumerate(self.results_s):
                a = datetime.datetime.strptime(self.deadline_s[count], "%d/%m/%y")
                b = datetime.datetime.now()
                if a < b:
                    counter += 0.1
                    tk.Label(self, font=("Courier", 9), background='green2', text="Module: " + self.module_id[count] + ". Grade: " + str(self.results_s[line])).place(relx=0.26, rely=counter)


class FeedbackPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = tk.Frame(self)
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        bg_image = tk.PhotoImage(file="bg5.png")
        bg_label = tk.Label(self, image=bg_image)
        bg_label.image = bg_image
        bg_label.place(relwidth=1, relheight=1)

        label = tk.Label(self, text="Feedback Page", font=LARGE_FONT)
        label.config(font=("Courier", 25), background="forest green")
        label.place(relx=0.388, rely=0.2)

        button1 = tk.Button(self, text="Back", background="MistyRose4",
                            command=lambda: controller.show_frame(DashboardStu))
        button1.config(height=2, width=13, font=("Courier", 25))
        button1.place(relx=0.39, rely=0.6)

        self.feedback = []
        self.deadline = []
        self.names = []
        self.answers = {}
        self.degree = ''
        self.username = ''

        self.feed = tk.Button(self, text="View Feedback", background='SeaGreen1', command=lambda: self.viewf())
        self.feed.config(font=("Courier", 25))
        self.feed.place(relx=0.38, rely=0.32)

    def viewf(self):

        self.username = current_users[-1]
        file = open("loginstudent.txt", "r")
        for line in file:
            line = line.split()
            if line[0] == self.username:
                self.degree = line[2]

        if os.stat("feedback.csv").st_size == 0:
            ttk.Label(self, text="No feedback available").grid()
        else:
            with open("feedback.csv", "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    if line[1] == self.degree:
                        self.feedback.append(line)
                        self.names.append(line[0])
            csv_file.close()

        if os.stat("tests.csv").st_size != 0 and os.stat("feedback.csv").st_size != 0:
            for i in self.feedback:
                with open("tests.csv", "r") as csv_file:
                    csv_reader = csv.reader(csv_file)
                    for line in csv_reader:
                        if line[0] == i[0]:
                            if not(line[5] in self.deadline):
                                self.deadline.append(line[5])

        if os.stat("tests.csv").st_size != 0:
            with open("tests.csv", "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    if line[0] in self.names:
                        if line[0] not in self.answers:
                            self.answers[line[0]] = [line[8]]
                        elif line[0] in self.answers:
                            self.answers[line[0]].append(line[8])

        if self.feedback:
            counter = 0.34
            for count, line in enumerate(self.feedback):
                a = datetime.datetime.strptime(self.deadline[count], "%d/%m/%y")
                b = datetime.datetime.now()
                if a < b:
                    counter += 0.1
                    tk.Button(self, font=("Courier", 9),
                               text="Module: "+line[2]+". Feedback for: "+line[0]+". Put online by: "+line[3],
                               command=lambda count=count: self.showfeed(count), background = 'green2'
                               ).place(relx=0.26, rely=counter)

    def showfeed(self, index):
        windo = tk.Toplevel()
        windo.geometry("1280x720")

        frame = tk.Frame(windo, bg="#e3dfe4")
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        modu = tk.Label(windo, font=("Courier", 20), background='turquoise1', text="Module: "+self.feedback[index][2]+". Feedback for: "+self.feedback[index][0]+". Put online by: "+self.feedback[index][3])
        modu.place(relx=0.1, rely=0.1)
        feed = tk.Text(windo, height=9, width=60, wrap='word')
        feed.insert(tk.INSERT, self.feedback[index][4])
        feed.config(state='disabled', font=("Courier", 20))
        feed.place(relx=0.1, rely=0.22)
        answ = tk.Text(windo, height=6, width=70, wrap='word')
        answ.insert(tk.INSERT, "The answers were: "+str(self.answers[self.feedback[index][0]]))
        answ.config(state='disabled')
        answ.place(relx=0.2, rely=0.7)


class CreateSummative(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = tk.Frame(self)
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        bg_image = tk.PhotoImage(file="bg4.png")
        bg_label = tk.Label(self, image=bg_image)
        bg_label.image = bg_image
        bg_label.place(relwidth=1, relheight=1)

        button1 = tk.Button(self, text="Back", background="MistyRose4",
                            command=lambda: controller.show_frame(DashboardLec))
        button1.config(height=2, width=13, font=("Courier", 25))
        button1.place(relx=0.41, rely=0.65)

        button2 = tk.Button(self, text="Create Summative Test", background='blue2', command=lambda: self.createWindow2())
        button2.config(font=("Courier", 25))
        button2.place(relx=0.34, rely=0.05)

        tests = tk.Button(self, text="Refresh", background='turquoise',
                          command=lambda: controller.show_frame(CreateSummative))
        tests.config(font=("Courier", 25))
        tests.place(relx=0.44, rely=0.18)

        self.questions = []
        self.username = ""
        self.deadline = ""
        self.degree = ""
        self.module_id = ""
        self.nb_alt = 1

        # We want to display all the quizzes as buttons according to the user's name
        # Get session username

        self.activatePage = tk.Button(self, text="Load Tests", command=lambda: self.user(), background='cadetblue1')
        self.activatePage.config(font=("Courier", 25))
        self.activatePage.place(relx=0.4, rely=0.3)


    def createWindow2(self):
        global window2
        window2 = tk.Toplevel()
        window2.geometry("600x500")
        self.create_new()

    def create_new(self):

        # Name,Degree,Mudule ID,Lecturer Username,Type,Deadline,Time,Question,Answer,Alt1,Alt2,Alt3,Alt4

        widget_list = self.allChildren(window2)
        for item in widget_list:
            item.grid_forget()

        self.username = current_users[-1]
        file = open("loginlecturer.txt", "r")
        for line in file:
            line = line.split()
            if line[0] == self.username:
                self.degree = line[2]
                self.module_id = line[3]
        self.questions = []
        button1 = tk.Button(window2, text="Back", background="MistyRose4",
                            command=lambda: window2.destroy())
        button1.config(height=2, width=13, font=("Courier", 25))
        button1.grid(row=0, column=0)

        ttk.Label(window2, text="Name of test:").grid(row=1, column=0)
        entry_name = ttk.Entry(window2)
        if self.questions:
            entry_name.insert(0, self.questions[0][0])
        entry_name.grid(row=1, column=1)

        ttk.Label(window2, text="Deadline(DD/MM/YY):").grid(row=2, column=0)
        entry_dead = ttk.Entry(window2)
        if self.questions:
            entry_dead.insert(0, self.questions[0][5])
        entry_dead.grid(row=2, column=1)

        ttk.Label(window2, text="Time(min):").grid(row=3, column=0)
        entry_time = ttk.Entry(window2)
        if self.questions:
            entry_dead.insert(0, self.questions[0][6])
        entry_time.grid(row=3, column=1)

        global question
        if self.questions:
            for i, question in enumerate(self.questions):
                ttk.Button(window, text=self.questions[i][7],
                           command=lambda question=question: self.show_details(question, entry_name.get())).grid()

        ttk.Button(window2, text="Create first question", command=lambda: self.save_new(entry_name.get(), self.degree, self.module_id, self.username, entry_dead.get(), entry_time.get(), window2)).grid()

    def save_new(self, name, degree, module, username, deadline, time, wind, nb_alt=1):

        widget_list = self.allChildren(wind)
        for item in widget_list:
            item.grid_forget()

        self.nb_alt = nb_alt

        ttk.Label(wind, text="Question").grid(row=1, column=0)
        entry_qu = tk.Text(wind, height=3, width=40, wrap='word')
        entry_qu.grid(row=1, column=1)

        ttk.Label(wind, text="Answer").grid(row=2, column=0)
        entry_answ = tk.Text(wind, height=2, width=30, wrap='word')
        entry_answ.grid(row=2, column=1)

        ttk.Label(wind, text="Alternatives: ").grid(row=3, column=0)

        but1 = ttk.Button(wind, text="Add Alternative", command=lambda: add_alt(self.nb_alt))
        but1.grid(row=4, column=0)

        but2 = ttk.Button(wind, text="Delete Alternative", command=lambda: del_alt(self.nb_alt))
        but2.grid(row=4, column=1)

        def del_alt(nb_alt):
            if nb_alt > 1:
                nb_alt -= 1
                self.save_new(name, degree, module, username, deadline, time, wind, nb_alt)

        def add_alt(nb_alt):
            if nb_alt < 9:
                nb_alt += 1
                self.save_new(name, degree, module, username, deadline, time, wind, nb_alt)

        alt1, alt2, alt3, alt4, alt5, alt6, alt7, alt8, alt9 = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()
        entry_names = [alt1, alt2, alt3, alt4, alt5, alt6, alt7, alt8, alt9]
        for i in range(self.nb_alt):
            entry = ttk.Entry(wind, textvariable=entry_names[i])
            entry.grid()

        tk.Button(wind, text="Save changes",
                  command=lambda: save_now(
                                            name,
                                            degree,
                                            module,
                                            username,
                                            deadline,
                                            time,
                                            entry_qu.get(1.0, 'end')[:-1],
                                            entry_answ.get(1.0, 'end')[:-1],
                                            entry_names[:self.nb_alt]
                  )).grid(row=0, column=1)

        def save_now(name, degree, module, username, deadline, time, question, answer, alternatives):

            with open("tests.csv", "a", newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                post = [name, degree, module, username, "Summative", deadline, time, question, answer]
                for i in alternatives:
                    post.append(i.get())
                csv_writer.writerow(post)
                tm.showinfo("Save", "Correctly saved")
                wind.destroy()
                self.user()

    def user(self):

        self.username = current_users[-1]
        global names

        # Get Test Names according to fetched username
        names = []
        with open('tests.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for count, line in enumerate(csv_reader):
                if line[3] == self.username and line[4] == "Summative":
                    if not (line[0] in names):
                        names.append(line[0])
                        i = names.index(line[0])
                        ttk.Button(self, text=line[0] + "Deadline of test: " + line[5],
                                   command=lambda i=i: self.createWindow(i)).grid(row=4+count)
        csv_file.close()


    def createWindow(self, index):
        global window
        self.username = current_users[-1]
        window = tk.Toplevel()
        window.geometry("600x500")
        self.displayTest(index)

    def displayTest(self, index):

        self.username = current_users[-1]
        file = open("loginlecturer.txt", "r")
        for line in file:
            line = line.split()
            if line[0] == self.username:
                self.degree = line[2]
                self.module_id = line[3]
        widget_list = self.allChildren(window)
        for item in widget_list:
            item.grid_forget()
        self.questions = []
        button1 = tk.Button(window, text="Back", background="MistyRose4",
                            command=lambda: window.destroy())
        button1.config(height=2, width=13, font=("Courier", 25))
        button1.grid(row=0, column=0)
        ttk.Label(window, text=names[index]).grid(row=1, column=0)
        ttk.Button(window, text="X", command=lambda: self.deleteTest(names[index])).grid(row=1, column=1)
        ttk.Button(window, text="Create Feedback for test", command=lambda: self.feed(names[index], self.username, self.degree, self.module_id)).grid(row=0, column=2)

        # Questions and answers in a list called self.question

        with open("tests.csv") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if line[0] == names[index]:
                    self.questions.append(line)
        csv_file.close()

        ttk.Label(window, text="Deadline(DD/MM/YY):").grid(row=2, column=0)
        entry_dead = ttk.Entry(window)
        entry_dead.insert(0, self.questions[0][5])
        entry_dead.grid(row=2, column=1)

        ttk.Label(window, text="Time(min)").grid(row=3, column=0)
        entry_time = ttk.Entry(window)
        entry_time.insert(0, self.questions[0][6])
        entry_time.grid(row=3, column=1)

        ttk.Button(window, text="Save time and deadline", command=lambda: self.save_deadline(entry_dead.get(), index, entry_time.get())).grid(row=4)

        ttk.Button(window, text="Add Question", command=lambda: self.save_new(names[index],
                                                                              self.degree,
                                                                              self.module_id,
                                                                              self.username,
                                                                              entry_dead.get(),
                                                                              entry_time.get(),
                                                                              window
                                                                              )
                   ).grid()

        # Questions are clickable so that user can modify them

        global question
        for i, question in enumerate(self.questions):
            ttk.Button(window, text=self.questions[i][7], command=lambda question=question:  self.show_details(question,index)).grid()

    def feed(self, test_name, lecturer, degree, module):

        trigger = False
        if not(os.stat("feedback.csv").st_size == 0):
            with open("feedback.csv", "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    if line[0] == test_name:
                        trigger = True
        if trigger:
            tm.showinfo("Error", "You have already created a feedback. No modification is possible. It is irreversible.")
        else:
            windo = tk.Toplevel(self)
            windo.geometry("700x500")
            button1 = tk.Button(windo, text="Back", background="MistyRose4",
                                command=lambda: windo.destroy())
            button1.config(height=2, width=13, font=("Courier", 25))
            button1.grid(row=0, column=0)
            ttk.Label(windo, text="Create feedback for test: "+test_name).grid(row=1, column=0)
            ttk.Label(windo, text="Feedback: ").grid(row=2, column=0)
            entry_qu = tk.Text(windo, height=5, width=50, wrap='word')
            entry_qu.grid(row=2, column=1)

            ttk.Button(windo, text="Submit Feedback", command=lambda: self.post_feed(test_name, lecturer, entry_qu.get(1.0, 'end')[:-1], windo, degree, module)).grid()

    def post_feed(self, test, username, feedback, wi, degree, module):
        if os.stat("feedback.csv").st_size == 0:
            with open("feedback.csv", "w", newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                post = [test,degree,module,username,feedback]
                csv_writer.writerow(post)
                csv_file.close()
        else:
            with open("feedback.csv", "a", newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                post = [test,degree,module,username,feedback]
                csv_writer.writerow(post)
            csv_file.close()
        tm.showinfo("Success", "Your feedback has been correctly saved, you will be redirected towards your test dashboard")
        wi.after(200)
        wi.destroy()

    def save_deadline(self, input, index, time):
        self.modify_csv('tests.csv', 0, names[index], 5, input)
        self.modify_csv('tests.csv', 0, names[index], 6, time)
        tm.showinfo("Save", "Correctly saved")

    def deleteTest(self, test_name):

        # Fetch lines to be removed

        lines_del = []
        with open("tests.csv", "r") as csv_filee:
            csv_read = csv.reader(csv_filee)
            lines = list(csv_read)

        for line in lines:
            if line[0] == test_name:
                lines_del.append(line)

        for lin in lines_del:
            lines.remove(lin)

        with open("tests.csv", 'w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

        csv_filee.close()
        writeFile.close()
        names.remove(test_name)

        tm.showinfo("Success", "Test was deleted, you will be redirected towards your dashboard")
        window.after(300)
        window.destroy()

    def show_details(self, question, index):
        widget_list = self.allChildren(window)
        for item in widget_list:
            item.grid_forget()
        button1 = tk.Button(window, text="Back", background="MistyRose4",
                            command=lambda: self.displayTest(index))
        button1.config(height=2, width=13, font=("Courier", 25))
        button1.grid(row=5)

        # Entries that user can modify

        ttk.Label(window, text="Question").grid(row=1, column=0)
        entry_qu = tk.Text(window, height=3, width=40, wrap='word')
        entry_qu.insert(tk.INSERT, question[7])
        entry_qu.grid(row=1, column=1)

        ttk.Label(window, text="Answer").grid(row=2, column=0)
        entry_answ = tk.Text(window, height=2, width=30, wrap='word')
        entry_answ.insert(tk.INSERT, question[8])
        entry_answ.grid(row=2, column=1)

        ttk.Label(window, text="Alternatives: ").grid(row=3, column=0)

        alternatives = []
        with open("tests.csv") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if line[0] == names[index] and line[7] == question[7]:
                    for j in line[9:]:
                        alternatives.append(j)
        csv_file.close()

        with open("tests.csv") as csv_file:
            csv_reader = csv.reader(csv_file)
            for count, line in enumerate(csv_reader):
                if line[0] == names[index] and line[7] == question[7]:
                    row = count
        csv_file.close()

        alt1, alt2, alt3, alt4, alt5, alt6, alt7, alt8, alt9 = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()
        entry_names = [alt1, alt2, alt3, alt4, alt5, alt6, alt7, alt8, alt9]
        for i, alt in enumerate(alternatives):
            entry = ttk.Entry(window, textvariable=entry_names[i])
            entry.insert(0, alt)
            entry_names[i].set(alt)
            entry.grid()

        length = len(alternatives)

        ttk.Button(window, text="Save changes", command=lambda: self.save_changes(entry_qu.get(1.0, 'end'), entry_answ.get(1.0, 'end'), entry_names[:length], row, index)).grid(row=0, column=1)

        ttk.Button(window, text="Delete question", command=lambda: self.delete_qu(entry_qu.get(1.0, 'end'), index)).grid(row=0, column=2)

    def delete_qu(self, question, index):

        with open("tests.csv", 'r') as readFile:
            reader = csv.reader(readFile)
            lines = list(reader)
            for line in lines:
                if line[7] == question[:-1]:
                    lines.remove(line)

        with open("tests.csv", 'w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

        readFile.close()
        writeFile.close()

        tm.showinfo("Success", "Question was deleted, you will be redirected towards your dashboard")
        window.after(300)
        self.displayTest(index)


    def save_changes(self, question, answer, alternatives, row, index):

        info_to_input = []

        with open("tests.csv", "r") as csv_file2:
            csv_reader = csv.reader(csv_file2)
            for i, line in enumerate(csv_reader):
                if i == row:
                    info_to_input = line

        info_to_input[7] = question[:-1]
        info_to_input[8] = answer[:-1]

        for count, i in enumerate(alternatives):
            info_to_input[9+count] = i.get()

        with open("tests.csv", 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            lines = list(csv_reader)
            lines[row] = info_to_input

        with open("tests.csv", 'w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

        csv_file2.close()
        csv_file.close()
        writeFile.close()

        tm.showinfo("Success", "Successfully saved")
        window.after(300)
        self.displayTest(index)

    def allChildren(self, win):
        _list = win.winfo_children()
        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())
        return _list

    def modify_csv(self, filename, index, special, row_index, info):

        rows = []
        data = []

        with open(filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for i, line in enumerate(csv_reader):
                if line[index] == special:
                    rows.append(i)
                    data.append(line)

        for item in data:
            item[row_index] = info

        for count, i in enumerate(rows):
            with open(filename, 'r') as readFile:
                reader = csv.reader(readFile)
                lines = list(reader)
                lines[i] = data[count]

            with open(filename, 'w', newline='') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(lines)

            readFile.close()
            writeFile.close()


class CreateFormative(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Create/View/Modify Formative Test(s)", font=LARGE_FONT)
        label.grid(row=0, column=10)

        button1 = tk.Button(self, text="Back", background="MistyRose4",
                            command=lambda: controller.show_frame(DashboardLec))
        button1.config(height=2, width=13, font=("Courier", 25))
        button1.grid(row=1, column=0)

        button2 = ttk.Button(self, text="Create Formative Test", command=lambda: self.createWindow2())
        button2.grid()

        self.names = []
        self.questions = []
        self.username = ""
        self.deadline = ""
        self.degree = ""
        self.module_id = ""
        self.nb_alt = 1

        # We want to display all the quizzes as buttons according to the user's name
        # Get session username

        self.activatePage = tk.Button(self, text="Load Tests", command=lambda: self.user())
        self.activatePage.config(height=3, width=15, font=("Courier", 25))
        self.activatePage.grid()

    def createWindow2(self):
        global window2
        window2 = tk.Toplevel()
        window2.geometry("600x500")
        self.create_new()

    def create_new(self):

        widget_list = self.allChildren(window2)
        for item in widget_list:
            item.grid_forget()

        self.username = current_users[-1]
        file = open("loginlecturer.txt", "r")
        for line in file:
            line = line.split()
            if line[0] == self.username:
                self.degree = line[2]
                self.module_id = line[3]
        self.questions = []
        button1 = tk.Button(window2, text="Back", background="MistyRose4",
                            command=lambda: window2.destroy())
        button1.config(height=2, width=13, font=("Courier", 25))
        button1.grid(row=0, column=0)

        ttk.Label(window2, text="Name of test:").grid(row=1, column=0)

        entry_name = ttk.Entry(window2)
        if self.questions:
            entry_name.insert(0, self.questions[0][0])
        entry_name.grid(row=1, column=1)

        ttk.Label(window2, text="Deadline(DD/MM/YY):").grid(row=2, column=0)
        entry_dead = ttk.Entry(window2)
        if self.questions:
            entry_dead.insert(0, self.questions[0][5])
        entry_dead.grid(row=2, column=1)

        ttk.Label(window2, text="Time(min):").grid(row=3, column=0)
        entry_time = ttk.Entry(window2)
        if self.questions:
            entry_dead.insert(0, self.questions[0][6])
        entry_time.grid(row=3, column=1)

        global question
        if self.questions:
            for i, question in enumerate(self.questions):
                ttk.Button(window, text=self.questions[i][7],
                           command=lambda question=question: self.show_details(question, entry_name.get())).grid()

        ttk.Button(window2, text="Create first question",
                   command=lambda: self.save_new(entry_name.get(), self.degree, self.module_id, self.username,
                                                 entry_dead.get(), entry_time.get(), window2)).grid()

    def save_new(self, name, degree, module, username, deadline, time, wind, nb_alt=1):

        widget_list = self.allChildren(wind)
        for item in widget_list:
            item.grid_forget()

        self.nb_alt = nb_alt

        ttk.Label(wind, text="Question").grid(row=1, column=0)
        entry_qu = tk.Text(wind, height=3, width=40, wrap='word')
        entry_qu.grid(row=1, column=1)

        ttk.Label(wind, text="Answer").grid(row=2, column=0)
        entry_answ = tk.Text(wind, height=2, width=30, wrap='word')
        entry_answ.grid(row=2, column=1)

        ttk.Label(wind, text="Alternatives: ").grid(row=3, column=0)

        but1 = ttk.Button(wind, text="Add Alternative", command=lambda: add_alt(self.nb_alt))
        but1.grid(row=4, column=0)

        but2 = ttk.Button(wind, text="Delete Alternative", command=lambda: del_alt(self.nb_alt))
        but2.grid(row=4, column=1)

        def del_alt(nb_alt):
            if nb_alt > 1:
                nb_alt -= 1
                self.save_new(name, degree, module, username, deadline, time, wind, nb_alt)

        def add_alt(nb_alt):
            if nb_alt < 9:
                nb_alt += 1
                self.save_new(name, degree, module, username, deadline, time, wind, nb_alt)

        alt1, alt2, alt3, alt4, alt5, alt6, alt7, alt8, alt9 = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()
        entry_names = [alt1, alt2, alt3, alt4, alt5, alt6, alt7, alt8, alt9]
        for i in range(self.nb_alt):
            entry = ttk.Entry(wind, textvariable=entry_names[i])
            entry.grid()

        tk.Button(wind, text="Save changes",
                  command=lambda: save_now(
                      name,
                      degree,
                      module,
                      username,
                      deadline,
                      time,
                      entry_qu.get(1.0, 'end')[:-1],
                      entry_answ.get(1.0, 'end')[:-1],
                      entry_names[:self.nb_alt]
                  )).grid(row=0, column=1)

        def save_now(name, degree, module, username, deadline, time, question, answer, alternatives):

            with open("tests.csv", "a", newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                post = [name, degree, module, username, "Formative", deadline, time, question, answer]
                for i in alternatives:
                    post.append(i.get())
                csv_writer.writerow(post)
                tm.showinfo("Save", "Correctly saved")
                wind.destroy()
                self.user()

    def user(self):

        self.username = current_users[-1]

        # Get Test Names according to fetched username
        self.names = []
        with open('tests.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for count, line in enumerate(csv_reader):
                if line[3] == self.username and line[4] == "Formative":
                    if not (line[0] in self.names):
                        self.names.append(line[0])
                        i = self.names.index(line[0])
                        ttk.Button(self, text=line[0] + "Deadline of test: " + line[5],
                                   command=lambda i=i: self.createWindow(i)).grid(row=4 + count)
        csv_file.close()

    def createWindow(self, index):
        global window
        self.username = current_users[-1]
        window = tk.Toplevel()
        window.geometry("600x500")
        self.displayTest(index)

    def displayTest(self, index):
        widget_list = self.allChildren(window)
        for item in widget_list:
            item.grid_forget()
        self.questions = []
        button1 = tk.Button(self, text="Back", background="MistyRose4",
                            command=lambda: window.destroy())
        button1.config(height=2, width=13, font=("Courier", 25))
        button1.grid(row=0, column=0)
        ttk.Label(window, text=self.names[index]).grid(row=1, column=0)
        ttk.Button(window, text="X", command=lambda: self.deleteTest(self.names[index])).grid(row=1, column=1)


        # Questions and answers in a list called self.question

        with open("tests.csv") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if line[0] == self.names[index]:
                    self.questions.append(line)
        csv_file.close()

        ttk.Label(window, text="Deadline(DD/MM/YY):").grid(row=2, column=0)
        entry_dead = ttk.Entry(window)
        entry_dead.insert(0, self.questions[0][5])
        entry_dead.grid(row=2, column=1)

        ttk.Label(window, text="Time(min)").grid(row=3, column=0)
        entry_time = ttk.Entry(window)
        entry_time.insert(0, self.questions[0][6])
        entry_time.grid(row=3, column=1)

        ttk.Button(window, text="Save time and deadline",
                   command=lambda: self.save_deadline(entry_dead.get(), index, entry_time.get())).grid(row=4)

        # name, degree, module, username, deadline, time, nb_alt=1

        self.username = current_users[-1]
        file = open("loginlecturer.txt", "r")
        for line in file:
            line = line.split()
            if line[0] == self.username:
                self.degree = line[2]
                self.module_id = line[3]

        ttk.Button(window, text="Add Question", command=lambda: self.save_new(self.names[index],
                                                                              self.degree,
                                                                              self.module_id,
                                                                              self.username,
                                                                              entry_dead.get(),
                                                                              entry_time.get(),
                                                                              window
                                                                              )
                   ).grid()

        # Questions are clickable so that user can modify them

        global question
        for i, question in enumerate(self.questions):
            ttk.Button(window, text=self.questions[i][7],
                       command=lambda question=question: self.show_details(question, index)).grid()

    def deleteTest(self, test_name):

        # Fetch lines to be removed

        lines_del = []
        with open("tests.csv", "r") as csv_file:
            csv_read = csv.reader(csv_file)
            lines = list(csv_read)

        for line in lines:
            if line[0] == test_name:
                lines_del.append(line)

        for lin in lines_del:
            lines.remove(lin)

        with open("tests.csv", 'w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

        csv_file.close()
        writeFile.close()
        self.names.remove(test_name)
        tm.showinfo("Success", "Test was deleted, you will be redirected towards your dashboard")
        window.after(300)
        window.destroy()

    def save_deadline(self, input, index, time):
        self.modify_csv('tests.csv', 0, self.names[index], 5, input)
        self.modify_csv('tests.csv', 0, self.names[index], 6, time)
        tm.showinfo("Save", "Correctly saved")

    def show_details(self, question, index):
        widget_list = self.allChildren(window)
        for item in widget_list:
            item.grid_forget()
        button1 = tk.Button(window, text="Back", background="MistyRose4",
                            command=lambda: self.displayTest(index))
        button1.config(height=2, width=13, font=("Courier", 25))
        button1.grid()

        # Entries that user can modify

        ttk.Label(window, text="Question").grid(row=1, column=0)
        entry_qu = tk.Text(window, height=3, width=40, wrap='word')
        entry_qu.insert(tk.INSERT, question[7])
        entry_qu.grid(row=1, column=1)

        ttk.Label(window, text="Answer").grid(row=2, column=0)
        entry_answ = tk.Text(window, height=2, width=30, wrap='word')
        entry_answ.insert(tk.INSERT, question[8])
        entry_answ.grid(row=2, column=1)

        ttk.Label(window, text="Alternatives: ").grid(row=3, column=0)

        alternatives = []
        with open("tests.csv") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if line[0] == self.names[index] and line[7] == question[7]:
                    for j in line[9:]:
                        alternatives.append(j)
        csv_file.close()

        with open("tests.csv") as csv_file:
            csv_reader = csv.reader(csv_file)
            for count, line in enumerate(csv_reader):
                if line[0] == self.names[index] and line[7] == question[7]:
                    row = count
        csv_file.close()

        alt1, alt2, alt3, alt4, alt5, alt6, alt7, alt8, alt9 = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()
        entry_names = [alt1, alt2, alt3, alt4, alt5, alt6, alt7, alt8, alt9]
        for i, alt in enumerate(alternatives):
            entry = ttk.Entry(window, textvariable=entry_names[i])
            entry.insert(0, alt)
            entry_names[i].set(alt)
            entry.grid()

        length = len(alternatives)

        ttk.Button(window, text="Save changes",
                   command=lambda: self.save_changes(entry_qu.get(1.0, 'end'), entry_answ.get(1.0, 'end'),
                                                     entry_names[:length], row, index)).grid(row=0, column=1)

        ttk.Button(window, text="Delete question",
                   command=lambda: self.delete_qu(entry_qu.get(1.0, 'end'), index)).grid(row=0, column=2)

    def delete_qu(self, question, index):

        with open("tests.csv", 'r') as readFile:
            reader = csv.reader(readFile)
            lines = list(reader)
            for line in lines:
                if line[7] == question[:-1]:
                    lines.remove(line)

        with open("tests.csv", 'w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

        readFile.close()
        writeFile.close()

        tm.showinfo("Success", "Question was deleted, you will be redirected towards your dashboard")
        window.after(300)
        self.displayTest(index)

    def save_changes(self, question, answer, alternatives, row, index):

        info_to_input = []

        with open("tests.csv", "r") as csv_file2:
            csv_reader = csv.reader(csv_file2)
            for i, line in enumerate(csv_reader):
                if i == row:
                    info_to_input = line

        info_to_input[7] = question[:-1]
        info_to_input[8] = answer[:-1]

        for count, i in enumerate(alternatives):
            info_to_input[9 + count] = i.get()

        with open("tests.csv", 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            lines = list(csv_reader)
            lines[row] = info_to_input

        with open("tests.csv", 'w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

        csv_file2.close()
        csv_file.close()
        writeFile.close()

        tm.showinfo("Success", "Successfully saved")
        window.after(300)
        self.displayTest(index)

    def allChildren(self, win):
        _list = win.winfo_children()
        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())
        return _list

    def modify_csv(self, filename, index, special, row_index, info):

        rows = []
        data = []

        with open(filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for i, line in enumerate(csv_reader):
                if line[index] == special:
                    rows.append(i)
                    data.append(line)

        for item in data:
            item[row_index] = info

        for count, i in enumerate(rows):
            with open(filename, 'r') as readFile:
                reader = csv.reader(readFile)
                lines = list(reader)
                lines[i] = data[count]

            with open(filename, 'w', newline='') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(lines)

            readFile.close()
            writeFile.close()


class DetailedResults(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Detailed results", font=LARGE_FONT)
        label.grid(row=0, column=10)
        button1 = tk.Button(self, text="Back", background="MistyRose4",
                            command=lambda: controller.show_frame(DashboardLec))
        button1.config(height=2, width=13, font=("Courier", 25))
        button1.grid()

        self.load = tk.Button(self, text="Load Tests", command=lambda: self.viewTests())
        self.load.config(height=3, width=15, font=("Courier", 25))
        self.load.grid()

        self.username = ''
        self.tests_s = []
        self.tests_f = []
        self.deadline_s = []
        self.deadline_f = []

    def viewTests(self):

        self.username = current_users[-1]

        #Summative

        with open("tests.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if line[3] == self.username and line[4] == "Summative":
                    if not(line[0] in self.tests_s):
                        self.tests_s.append(line[0])
                        self.deadline_s.append(line[5])
        csv_file.close()

        # Formative

        with open("tests.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if line[3] == self.username and line[4] == "Formative":
                    if not (line[0] in self.tests_f):
                        self.tests_f.append(line[0])
                        self.deadline_f.append(line[5])

        ttk.Label(self, text="Summative Tests: ").grid()

        for count, test in enumerate(self.tests_s):
            a = datetime.datetime.strptime(self.deadline_s[count], "%d/%m/%y")
            b = datetime.datetime.now()
            if a < b:
                ttk.Button(self, text=test,
                           command=lambda count=count: self.viewResults_s(count)).grid()
        csv_file.close()

        ttk.Label(self, text="Formative Tests: ").grid()

        for count, test in enumerate(self.tests_f):
            a = datetime.datetime.strptime(self.deadline_f[count], "%d/%m/%y")
            b = datetime.datetime.now()
            if a < b:
                ttk.Button(self, text=test,
                           command=lambda count=count: self.viewResults_f(count)).grid()
        csv_file.close()

    def viewResults_s(self, index):
        results = []
        resultperstudent = {}
        with open("results.csv") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if line[1] == self.tests_s[index]:
                    a = 0
                    b = len(line[4:])
                    for j in line[4:]:
                        results.append(int(j))
                        a += int(j)
                    resultperstudent[line[0]] = round(((a/b)*100), 2)
        average = round(((sum(results)/len(results))*100), 2)
        highest_name = (','.join(str(key) for min_value in (max(resultperstudent.values()),) for key in resultperstudent if resultperstudent[key] == min_value)).split(',')
        lowest_name = (','.join(str(key) for min_value in (min(resultperstudent.values()),) for key in resultperstudent if resultperstudent[key] == min_value)).split(',')
        mark_max = resultperstudent[max(resultperstudent.keys(), key=(lambda k: resultperstudent[k]))]
        mark_min = resultperstudent[min(resultperstudent.keys(), key=(lambda k: resultperstudent[k]))]
        plt.rcdefaults()

        objects = ('Average', str(highest_name), str(lowest_name))
        y_pos = np.arange(len(objects))
        performance = [average, mark_max, mark_min]

        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects, rotation=10)
        plt.ylabel('Marks')
        plt.title(self.tests_s[index])
        plt.show()

    def viewResults_f(self, index):
        results = []
        resultperstudent = {}
        with open("results.csv") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if line[1] == self.tests_f[index] and line[3] == "1":
                    a = 0
                    b = len(line[4:])
                    for j in line[4:]:
                        results.append(int(j))
                        a += int(j)
                    resultperstudent[line[0]] = round(((a / b) * 100), 2)
        average = round(((sum(results) / len(results)) * 100), 2)
        highest_name = (','.join(
            str(key) for min_value in (max(resultperstudent.values()),) for key in resultperstudent if
            resultperstudent[key] == min_value)).split(',')
        lowest_name = (','.join(
            str(key) for min_value in (min(resultperstudent.values()),) for key in resultperstudent if
            resultperstudent[key] == min_value)).split(',')
        mark_max = resultperstudent[max(resultperstudent.keys(), key=(lambda k: resultperstudent[k]))]
        mark_min = resultperstudent[min(resultperstudent.keys(), key=(lambda k: resultperstudent[k]))]
        plt.rcdefaults()

        objects = ('Average', str(highest_name), str(lowest_name))
        y_pos = np.arange(len(objects))
        performance = [average, mark_max, mark_min]

        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Marks')
        plt.title(self.tests_f[index])
        plt.show()

current_users = ["Nothing"]
# To get session username, type <current_users[-1]>
app = main()
app.geometry("1280x720")
app.mainloop()
