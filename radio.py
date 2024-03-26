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

text_var_q = tkinter.StringVar(value="Which color \n do you like most?")

label_q = ctk.CTkLabel(master=frame,
                       textvariable=text_var_q,
                       width=120,
                       height=25,
                       fg_color=("yellow","yellow"),
                       text_color="black",
                       font=("Arial", 20),
                       corner_radius=8)
label_q.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)


def radiobutton_event():
    text_var_r.set(f"You picked {radio_var.get()}")

radio_var = tkinter.StringVar(value="")

blue_rb = ctk.CTkRadioButton(master=frame,
                             text="Blue",
                             command=radiobutton_event,
                             variable=radio_var,
                             value="Blue",
                             fg_color="blue")
blue_rb.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)


green_rb = ctk.CTkRadioButton(master=frame,
                             text="Green",
                             command=radiobutton_event,
                             variable=radio_var,
                             value="Green",
                             fg_color="green")
green_rb.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

red_rb = ctk.CTkRadioButton(master=frame,
                             text="Red",
                             command=radiobutton_event,
                             variable=radio_var,
                             value="Red",
                             fg_color="red")
red_rb.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

text_var_r = tkinter.StringVar(value="")

label_r = ctk.CTkLabel(master=frame,
                       textvariable=text_var_r,
                       width=120,
                       height=25,
                       fg_color=("black","black"),
                       text_color="white",
                       font=("Arial", 20),
                       corner_radius=8)
label_r.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)


app.mainloop()