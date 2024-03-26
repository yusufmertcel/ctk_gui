import tkinter
from typing import Tuple
import customtkinter as ctk
from tkinter import *
import cv2 
from PIL import Image, ImageTk 
import time
import threading
from tkinter import ttk
from db import DataBase
import os

class CustomApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Kia App")
        self._set_appearance_mode("dark")
        
        self.frame = CustomFrame(self)
        
class CustomFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=450,
                     height=350,bg_color="green",
                     fg_color="gray75",
                     corner_radius=10)
        self.pack(padx=200, pady=200)

        login_image = ctk.CTkImage(light_image=Image.open(os.path.join(os.path.dirname(__file__), 'images/kia_logo.png')), dark_image=Image.open(os.path.join(os.path.dirname(__file__), 'images/kia_logo.png')), size=(300,168)) #width, height

        self.label_logo = ctk.CTkLabel(master=self,
                                       text="",
                                       image=login_image)
        self.label_logo.place(relx=0.5, rely=0.13, anchor=tkinter.CENTER)

        self.user_id_entry = ctk.CTkEntry(master=self,
                             placeholder_text="Kullanıcı Adı",
                             width=200,
                             height=35,
                             border_width=2,
                             corner_radius=10)
        self.user_id_entry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        self.password_entry = ctk.CTkEntry(master=self,
                             placeholder_text="Şifre",
                             width=200,
                             height=35,
                             show="*",
                             border_width=2,
                             corner_radius=10)
        self.password_entry.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        
        self.button = ctk.CTkButton(self, text="Giriş", command=self.on_button_click)
        self.button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

        self.str_var = StringVar(value="")

        self.label = ctk.CTkLabel(master=self,
                            textvariable=self.str_var,
                            width=120,
                            height=25,
                            fg_color=("gray","gray75"),
                            corner_radius=8,
                            text_color="white")
        self.label.place(relx=0.5, rely=0.95, anchor=tkinter.CENTER)  

        self.toggle_btn = ctk.CTkButton(master=self, text='Şifreyi Göster/Gizle', width=15, command=self.toggle_password)
        self.toggle_btn.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)
          

    def toggle_password(self):
        if self.password_entry.cget('show') == '':
            self.password_entry.configure(show='*')
        else:
            self.password_entry.configure(show='')

    def on_button_click(self):
        #self.update()
        entry_username = self.user_id_entry.get()
        username, password, fullname = inst_db.find_user(username=entry_username)
        if (self.user_id_entry.get() == username) and (self.password_entry.get() == password) and (username == "admin"):
            self.str_var.set("Admin Paneline Bağlandı")
            self.open_admin_frame(fullname)
        elif (self.user_id_entry.get() == username) and (self.password_entry.get() == password):
            self.str_var.set("Bağlandı")
            self.open_new_frame(fullname)   
        else:
            self.str_var.set("Hatalı şifre veya kullanıcı adı")
    
    def open_new_frame(self, username):
        new_frame = NewFrame(self, username)
    
    def open_admin_frame(self, username):
        new_admin_frame = AdminFrame(self, username)

class AdminFrame(ctk.CTkToplevel):
    def __init__(self, parent, username):
        super().__init__(parent, width=350,
                     height=250,fg_color="gray75")
        self.title("Admin Panel")
        tabView = ctk.CTkTabview(self)
        tabView.pack(padx=20, pady=20)

        tabView.add("Kullanıcılar")
        tabView.add("Görseller")

        tabView.set("Kullanıcılar")
        self.frame_left = ctk.CTkFrame(master=tabView.tab("Kullanıcılar"),
                                             width=200,
                                             corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        add_user_btn = ctk.CTkButton(master=self.frame_left, text="Kullanıcı Ekle", command=self.add_user_event)
        add_user_btn.grid(row=0, column=0, padx=20, pady=20)

        del_user_btn = ctk.CTkButton(master=self.frame_left, text="Kullanıcı Sil", command=self.del_user_event)
        del_user_btn.grid(row=3, column=0, padx=20, pady=20)

        upd_user_btn = ctk.CTkButton(master=self.frame_left, text="Kullanıcı Güncelle", command=self.upd_user_event)
        upd_user_btn.grid(row=6, column=0, padx=20, pady=20)

        self.frame_right = ctk.CTkFrame(master=tabView.tab("Kullanıcılar"), bg_color="blue")
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=15, pady=15)

        self.frame_left.grid_rowconfigure(0, minsize=10)
        self.frame_left.grid_rowconfigure(8, minsize=20)
        self.frame_left.grid_rowconfigure(11, minsize=10)

        self.add_menu_display211 = ctk.CTkFrame(master=self.frame_right,
                                                        corner_radius=15,
                                                        height=400,
                                                        width=600)
        self.add_menu_display211.grid(pady=15, padx=15, sticky="nws")

        columns = ("Number", 'id', 'name', 'username', 'password')

        self.table = ttk.Treeview(master=self.add_menu_display211,
                                columns=columns,
                                height=17,
                                selectmode='browse',
                                show='headings')

        self.table.column("#1", anchor="c", minwidth=50, width=50)
        self.table.column("#2", anchor="w", minwidth=220, width=220)
        self.table.column("#3", anchor="c", minwidth=120, width=120)
        self.table.column("#4", anchor="c", minwidth=120, width=120)
        self.table.column("#5", anchor="c", minwidth=120, width=120)

        self.table.heading('Number', text='Sıra')
        self.table.heading('id', text='ID')
        self.table.heading('name', text='Tam İsim')
        self.table.heading('username', text='Kullanıcı Adı')
        self.table.heading('password', text='Şifre')

        self.table.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        self.table.bind('<Motion>', 'break')

        ctk_table_scrollbar = ctk.CTkScrollbar(self.add_menu_display211, command=self.table.yview)
        ctk_table_scrollbar.grid(row=0, column=1, stick="ns")

        self.table.configure(yscrollcommand=ctk_table_scrollbar.set)
        result_data = inst_db.users_col.find()

        self.add_data(result_data)
    
    def add_data(self, data):
        for index,datum in enumerate(data):
            print(datum)
            self.table.insert("", 'end', values=[index+1]+list(datum.values()))

    def add_user_event(self):
        pass

    def del_user_event():
        pass

    def upd_user_event():
        pass

    


class NewFrame(ctk.CTkToplevel):
    def __init__(self, parent, username):
        super().__init__(parent, width=350,
                     height=250,fg_color="gray75")
        self.title("Kamera Panel")
        self.label = ctk.CTkLabel(master=self,
                            text=f"Hoşgeldin {username}. \nLütfen Kamera Bütün Vücudunu Görecek Şekilde Durun",
                            width=120,
                            height=25,
                            fg_color=("gray","gray75"),
                            corner_radius=8,
                            text_color="white")
        self.label.grid(row=0, column=0, padx=20, pady=20)

        self.frame_cam = ctk.CTkFrame(master=self,
                                      width=1000,
                                      height=1000,
                                      bg_color="gray",
                                      fg_color="gray75",
                                      corner_radius=10)
        self.frame_cam.grid(row=1,column=0)
        
        x = threading.Thread(target=self.camera_open)
        #time.sleep(5)
        x.start()
        #x.join()
        print("Thread is finished")

    def camera_open(self):
        self.camera = Camera(self.frame_cam, 1000, 1000)
        

class Camera(threading.Thread):
    def __init__(self, frame, width, height):
        #super().__init__()
        self.vid = cv2.VideoCapture(0)
        self.width, self.height = width, height

        self.vid.set(cv2.CAP_PROP_FRAME_WIDTH, self.width) 
        self.vid.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
  
        # Create a label and display it on app 
        self.label_widget = ctk.CTkLabel(master=frame, text="")
        self.label_widget.pack(padx=15, pady=15) 

        # Create a button to open the camera in GUI app 
        self.button1 = Button(frame, text="Kamerayı Aç", command=self.open_camera) 
        self.button1.pack(padx=15, pady=15)

        # Create a button to open the camera in GUI app 
        self.button2 = Button(frame, text="Mail Gonder", command=self.open_camera) 
        self.button2.pack(padx=15, pady=15)

        self.button1['state'] = "active" 

    def open_camera(self): 
        self.button1['state'] = "disabled"
        # Capture the video frame by frame 
        _, frame = self.vid.read() 
    
        # Convert image from one color space to other 
        opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) 
    
        # Capture the latest frame and transform to image 
        captured_image = Image.fromarray(opencv_image) 
    
        # Convert captured image to photoimage 
        photo_image = ImageTk.PhotoImage(image=captured_image)
    
        # Displaying photoimage in the label 
        self.label_widget.photo_image = photo_image 
    
        # Configure image in the label 
        self.label_widget.configure(image=photo_image) 
    
        # Repeat the same process after every 10 seconds 
        self.label_widget.after(10, self.open_camera) 
  


if __name__ == "__main__":
    inst_db = DataBase("mydatabase")
    app = CustomApp()
    app.bind('<Escape>', lambda e: app.quit())
    app.mainloop()

