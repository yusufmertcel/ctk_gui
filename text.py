import customtkinter as ctk
import tkinter

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


app = ctk.CTk()
app.geometry("400x240")

textbox = ctk.CTkTextbox(app)
textbox.grid(row=0, column=0)

text = """
    Welcome to Turtle Code
"""

textbox.insert("0.0", text)
#textbox.configure(state="disabled") #read permission
textbox.configure(state="normal")

def button_clicked():
    print(textbox.get("0.0", "end"))

btn = ctk.CTkButton(master=app, text="Button",command=button_clicked)
btn.place(relx=0.7, rely=0.3, anchor=tkinter.CENTER)

app.mainloop()