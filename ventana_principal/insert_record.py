from tkinter import *
from tkinter import messagebox
from database.db import Database

class InsertRecord:
    def __init__(self, master):
        self.master = master
        self.master.title("Insertar registro")
        self.master.geometry("500x300")

        # Conectar a la base de datos
        self.db = Database(user="root", password="admin123",
                           host="localhost", database="bd_csv")

        # Resto del código para crear la interfaz de usuario
        # ...
         # Crear etiquetas y campos de entrada
        Label(self.master, text="Codigo DANE").grid(row=0, column=0)
        self.col1_entry = Entry(self.master)
        self.col1_entry.grid(row=0, column=1)

        Label(self.master, text="Municipio Productor").grid(row=1, column=0)
        self.col2_entry = Entry(self.master)
        self.col2_entry.grid(row=1, column=1)

        Label(self.master, text="Departamento").grid(row=2, column=0)
        self.col3_entry = Entry(self.master)
        self.col3_entry.grid(row=2, column=1)

        Label(self.master, text="Recurso Natural").grid(row=3, column=0)
        self.col4_entry = Entry(self.master)
        self.col4_entry.grid(row=3, column=1)

        Label(self.master, text="Nombre del proyecto").grid(row=4, column=0)
        self.col5_entry = Entry(self.master)
        self.col5_entry.grid(row=4, column=1)

        Label(self.master, text="Año Producción").grid(row=5, column=0)
        self.col6_entry = Entry(self.master)
        self.col6_entry.grid(row=5, column=1)

        Label(self.master, text="Trimestre").grid(row=6, column=0)
        self.col7_entry = Entry(self.master)
        self.col7_entry.grid(row=6, column=1)

        Label(self.master, text="Unidad Medida").grid(row=7, column=0)
        self.col8_entry = Entry(self.master)
        self.col8_entry.grid(row=7, column=1)

        Label(self.master, text="Tipo Contraprestación").grid(row=8, column=0)
        self.col9_entry = Entry(self.master)
        self.col9_entry.grid(row=8, column=1)

        Label(self.master, text="Valor Contraprestación").grid(row=9, column=0)
        self.col10_entry = Entry(self.master)
        self.col10_entry.grid(row=9, column=1)

        Label(self.master, text="Cantidad Producción").grid(row=10, column=0)
        self.col11_entry = Entry(self.master)
        self.col11_entry.grid(row=10, column=1)

        # Crear botón para guardar el registro
        Button(self.master, text="Guardar", command=self.save_record).grid(row=11, column=1)

    def save_record(self):
        # Obtener los valores de los campos de entrada
        col1 = self.col1_entry.get()
        col2 = self.col2_entry.get()
        col3 = self.col3_entry.get()
        col4 = self.col4_entry.get()
        col5 = self.col5_entry.get()
        col6 = self.col6_entry.get()
        col7 = self.col7_entry.get()
        col8 = self.col8_entry.get()
        col9 = self.col9_entry.get()
        col10 = self.col10_entry.get()
        col11 = self.col11_entry.get()

        # Insertar el nuevo registro en la tabla
        query = "INSERT INTO data (`COL 1`, `COL 2`, `COL 3`, `COL 4`, `COL 5`, `COL 6`, `COL 7`, `COL 8`, `COL 9`, `COL 10`, `COL 11`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11)

        try:
                result = self.db.query(query, values)
                if result:
                    messagebox.showinfo("Success", "Record inserted successfully")
                    # Clear the input fields
                    self.col1_entry.delete(0, END)
                    self.col2_entry.delete(0, END)
                    self.col3_entry.delete(0, END)
                    self.col4_entry.delete(0, END)
                    self.col5_entry.delete(0, END)
                    self.col6_entry.delete(0, END)
                    self.col7_entry.delete(0, END)
                    self.col8_entry.delete(0, END)
                    self.col9_entry.delete(0, END)
                    self.col10_entry.delete(0, END)
                    self.col11_entry.delete(0, END)
        except Exception as e:
                messagebox.showerror("Error", f"Failed to insert record: {str(e)}")
