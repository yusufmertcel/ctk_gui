import customtkinter as ctk
import tkinter
from tkinter import *

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


app = ctk.CTk()
app.title("By Joseph")

frame = ctk.CTkFrame(master=app,
                     width=400,
                     height=400,
                     corner_radius=10)
frame.pack(padx=200, pady=200)

text_var = ctk.StringVar(value="Do you like this app?")

label_question = ctk.CTkLabel(master=frame,
                              textvariable=text_var,
                              width=220,
                              height=120,
                              text_color="yellow",
                              font=("Arial", 20),
                              fg_color=("black", "black"),
                              corner_radius=8)
label_question.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

check_var_python = tkinter.StringVar(value="off")
check_var_java = tkinter.StringVar(value="off")
check_var_go = tkinter.StringVar(value="off")

def checkbox_event():
    pass

check_python = ctk.CTkCheckBox(master=frame,
                               text="Python",
                               command=checkbox_event,
                               variable=check_var_python,
                               onvalue="on",
                               offvalue="off")
check_python.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

check_java= ctk.CTkCheckBox(master=frame,
                               text="Java",
                               command=checkbox_event,
                               variable=check_var_java,
                               onvalue="on",
                               offvalue="off")
check_java.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

check_go = ctk.CTkCheckBox(master=frame,
                               text="Go",
                               command=checkbox_event,
                               variable=check_var_go,
                               onvalue="on",
                               offvalue="off")
check_go.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

def button_event():
    text = ""
    text_1 = ""
    text_2 = ""
    text_3 = ""

    if check_var_python.get() == "on":
        text_1 = "Python"
    if check_var_java.get() == "on":
        text_2 = "Java"
    if check_var_go.get() == "on":
        text_3 = "Go"
    result = text_1 + " " + text_2 + " " + text_3
    text_var_result.set(result)

button = ctk.CTkButton(master=frame,
                       width=120,
                       height=32,
                       border_width=0,
                       corner_radius=8,
                       text="Send Info",
                       command=button_event)
button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

text_var_result = ctk.StringVar(value="")

label_result = ctk.CTkLabel(master=frame,
                            textvariable=text_var_result,
                            width=220,
                            height=60,
                            text_color="yellow",
                            font=("Arial", 20),
                            fg_color=("black", "black"),
                            corner_radius=8)
label_result.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

app.mainloop()