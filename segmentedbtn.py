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
frame.pack(padx=10, pady=10)

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


age_entry = ctk.CTkEntry(master=frame,
                          placeholder_text="Age",
                          width=150,
                          height=30,
                          border_width=2,
                          corner_radius=10)
age_entry.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


def segmented_button_callback(value):
    text_var.set("")
    if value == "Name":
        text_var.set(f"Name: {name_entry.get()}")
    if value == "Surname":
        text_var.set(f"Surname: {surname_entry.get()}")
    if value == "Age":
        text_var.set(f"Age: {age_entry.get()}")

segmented_button = ctk.CTkSegmentedButton(master=frame,
                                          values=["Name", "Surname", "Age"], command=segmented_button_callback)
segmented_button.place(relx=0.27, rely=0.6)
segmented_button.set("Name")

text_var = tkinter.StringVar(value="")


label = ctk.CTkLabel(master=frame,
                        textvariable=text_var,
                        width=120,
                        height=25,
                        text_color="black",
                        corner_radius=8,
                        fg_color=("yellow", "yellow"),
                        bg_color="yellow")
label.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)





app.mainloop()