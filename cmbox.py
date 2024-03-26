import customtkinter as ctk
import tkinter
from tkinter import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


app = ctk.CTk()
app.title("By Joseph")

frame = ctk.CTkFrame(master=app,
                     width=350,
                     height=350,
                     corner_radius=10)
frame.pack(padx=20, pady=20)


name_entry = ctk.CTkEntry(master=frame,
                          placeholder_text="Name",
                          width=150,
                          height=30,
                          border_width=2,
                          corner_radius=10)
name_entry.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)


surname_entry = ctk.CTkEntry(master=frame,
                          placeholder_text="Surname",
                          width=150,
                          height=30,
                          border_width=2,
                          corner_radius=10)
surname_entry.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

optionmenu_var = ctk.StringVar(value="Male")

gender_combobox = ctk.CTkComboBox(master=frame,
                                  values=["Male", "Female"],
                                  variable=optionmenu_var)
gender_combobox.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

def button_event():
    name = str(name_entry.get())
    surname = str(surname_entry.get())
    gender = str(gender_combobox.get())
    text_var.set(f"Name: {name} \n Surname: {surname} \n Gender: {gender}")


button = ctk.CTkButton(master=frame,
                       text="Button",
                       command=button_event)
button.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)


text_var = StringVar()

label = ctk.CTkLabel(master=frame,
                     textvariable=text_var,
                     width=150,
                     height=50,
                     fg_color=("black", "yellow"),
                     text_color="black",
                     corner_radius=8)
label.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

app.mainloop()