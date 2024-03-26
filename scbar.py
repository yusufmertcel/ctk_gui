import customtkinter as ctk
import tkinter
from tkinter import *

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


app = ctk.CTk()
#app.geometry("400x240")

frame = ctk.CTkFrame(master=app,
                     width=200,
                     height=200,
                     corner_radius=10)
frame.pack(padx=20, pady=20)

tk_textbox = tkinter.Text(frame, highlightthickness=0)
tk_textbox.grid(row=0, column=0, sticky="nsew")

ctk_textbox_scrollbar = ctk.CTkScrollbar(frame, command=tk_textbox.yview)
ctk_textbox_scrollbar.grid(row=0, column=1, stick="ns")

tk_textbox.configure(yscrollcommand=ctk_textbox_scrollbar.set)

my_str_var = StringVar()


def button_event():
    print(tk_textbox.get("0.0","end"))
    textbox_text = tk_textbox.get("0.0","end")
    my_str_var.set(str(textbox_text))


button = ctk.CTkButton(master=frame, text="Button", command=button_event)
button.grid(padx=20, pady=10)

label = ctk.CTkLabel(master=frame, 
                     fg_color=("white", "gray75"),
                     textvariable=my_str_var,
                     width=120,
                     height=25,
                     corner_radius=8)
label.grid(padx=20, pady=10)

app.mainloop()