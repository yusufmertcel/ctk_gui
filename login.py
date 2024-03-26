import customtkinter as ctk
import tkinter
from tkinter import *

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


app = ctk.CTk()
app.title("By Joseph")

frame = ctk.CTkFrame(master=app,
                     width=350,
                     height=250,
                     bg_color="green",
                     fg_color="white",
                     corner_radius=10)
frame.pack(padx=20, pady=20)

user_id_entry = ctk.CTkEntry(master=frame,
                             placeholder_text="Username",
                             width=200,
                             height=35,
                             border_width=2,
                             corner_radius=10)
user_id_entry.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

password_entry = ctk.CTkEntry(master=frame,
                             placeholder_text="Password",
                             width=200,
                             height=35,
                             show="*",
                             border_width=2,
                             corner_radius=10)
password_entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

def button_event():
    if (user_id_entry.get() == user_id) and (password_entry.get() == password):
        str_var.set("Connected")
    else:
        str_var.set("Wrong password or username")


user_id ="admin"
password = "12345"

button = ctk.CTkButton(master=frame,
                       text="BUTTON",
                       command=button_event)
button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

str_var = StringVar()

label = ctk.CTkLabel(master=frame,
                     textvariable= str_var,
                     width=120,
                     height=25,
                     fg_color=("white","gray75"),
                     corner_radius=8)
label.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)

app.mainloop()