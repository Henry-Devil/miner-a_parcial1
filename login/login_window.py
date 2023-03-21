from database.db import Database
from tkinter import *
from ventana_principal.main_window import MainWindow
from tkinter import messagebox


class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Inicio de sesión")
        self.master.geometry("300x150")
        
        # Conectar a la base de datos
        self.db = Database(
            host="localhost",
            user="root",
            password="admin123",
            database="bd_csv"
        )

        # Resto del código para crear la interfaz de usuario
        # ...
        self.username_label = Label(self.master, text="Usuario:")
        self.username_label.pack()
        self.username_entry = Entry(self.master)
        self.username_entry.pack()

        self.password_label = Label(self.master, text="Contraseña:")
        self.password_label.pack()
        self.password_entry = Entry(self.master, show="*")
        self.password_entry.pack()

        self.login_button = Button(self.master, text="Iniciar sesión", command=self.login)
        self.login_button.pack()
        
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Verificar si el usuario y la contraseña son correctos
        self.db.cursor.execute("SELECT * FROM user WHERE user=%s AND password=%s", (username, password))
        result = self.db.cursor.fetchone()
        if result:
            self.master.destroy()  # Cerrar la ventana de inicio de sesión
            main_window = Tk()
            MainWindow(main_window)
            main_window.mainloop()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
