import customtkinter as ctk
import tkinter
from tkinter import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


app = ctk.CTk()
app.title("By Joseph")

frame = ctk.CTkFrame(master=app,
                     width=400,
                     height=400,
                     corner_radius=10)
frame.pack(padx=200, pady=200)

switch_var_1 = ctk.StringVar(value="on")
switch_var_2 = ctk.StringVar(value="off")


def switch_event():
    if switch_var_1.get() == "on" and switch_var_2.get() == "off":
        ctk.set_appearance_mode("dark")
    if switch_var_1.get() == "off" and switch_var_2.get() == "off":
        ctk.set_appearance_mode("System")

switch_1 = ctk.CTkSwitch(master=frame,
                         text="Switch App Mode",
                         command=switch_event,
                         variable=switch_var_1,
                         onvalue="on",
                         offvalue="off")
switch_1.pack(padx=20, pady=10)

switch_2 = ctk.CTkSwitch(master=frame,
                         text="Lock",
                         command=switch_event,
                         variable=switch_var_2,
                         onvalue="on",
                         offvalue="off")
switch_2.pack(padx=20, pady=10)



app.mainloop()