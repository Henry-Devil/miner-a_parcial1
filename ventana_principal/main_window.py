import mysql.connector
from tkinter import *
from tkinter import messagebox
from .insert_record import InsertRecord
from .show_records import ShowRecords
from .about_window import AboutWindow

class Database:
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.cnx = mysql.connector.connect(user=self.user, password=self.password,
                                            host=self.host, database=self.database)
        self.cursor = self.cnx.cursor()
    
    def query(self, query, values=None):
        self.cursor.execute(query, values)
        self.cnx.commit()
        return self.cursor.fetchall()
    
    def __del__(self):
        self.cursor.close()
        self.cnx.close()


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Ventana principal")
        # Cambiar las dimensiones de la ventana
        self.master.geometry("800x600")

        # Botón para salir del sistema
        self.exit_button = Button(self.master, text="Salir", command=self.exit)
        self.exit_button.grid(row=1, column=0, padx=10, pady=10)

        # Crear el menú con tres opciones
        self.menu_bar = Menu(self.master)

        # Opción "Insertar"
        self.insert_menu = Menu(self.menu_bar, tearoff=0)
        self.insert_menu.add_command(
            label="Insertar datos", command=self.insert_data)
        self.menu_bar.add_cascade(label="Insertar", menu=self.insert_menu)

        # Opción "Visualizar"
        self.view_menu = Menu(self.menu_bar, tearoff=0)
        self.view_menu.add_command(
            label="Visualizar datos", command=self.show_data)
        self.menu_bar.add_cascade(label="Visualizar", menu=self.view_menu)

        # Opción "Acerca de"
        self.menu_bar.add_command(label="Acerca de", command=self.show_about_window)

        self.master.config(menu=self.menu_bar)

    def exit(self):
        self.master.destroy()

    def insert_data(self):
        insert_window = Toplevel(self.master)
        insert_record = InsertRecord(insert_window)
        insert_record.save_record()

    def show_data(self):
        show_window = Toplevel(self.master)
        show_records = ShowRecords(show_window)
        show_records.load_data()

    def show_about_window(self):
        AboutWindow(self.master)



if __name__ == "__main__":
    root = Tk()
    app = MainWindow(root)
    root.mainloop()