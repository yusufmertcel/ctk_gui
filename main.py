import customtkinter as ctk
import tkinter

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()

app.title("Button App by ME")
app.geometry("400x240")

def button_function1():
    print("Button 1 pressed!!")


def button_function2():
    print("Button 2 pressed!!")


frame = ctk.CTkFrame(master=app,
                     width=200,
                     height=200,
                     corner_radius=20,
                     bg_color="white"
                     )
frame.pack(padx=20, pady=20)

button1 = ctk.CTkButton(master=frame, text="Button 1", command=button_function1)
button1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

button2 = ctk.CTkButton(master=frame, text="Button 2", command=button_function2)
button2.place(relx=0.6, rely=0.7, anchor=tkinter.CENTER)




app.mainloop()