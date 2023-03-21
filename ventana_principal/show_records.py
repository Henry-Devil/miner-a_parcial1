import mysql.connector
import tkinter as tk
import tkinter.ttk as ttk

class ShowRecords(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Mostrar registros")
        self.geometry("800x600")

        self.table = ttk.Treeview(self)
        self.table.pack(fill="both", expand=True)

        self.load_data()

    def load_data(self):
        # Conectar a la base de datos
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin123",
            database="bd_csv"
        )

        # Seleccionar los registros de la tabla deseada
        cursor = db.cursor()
        cursor.execute("SELECT * FROM data")
        data = cursor.fetchall()

        # Configurar las columnas de la tabla
        self.table["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9", "col10", "col11")
        self.table.column("#0", width=0, stretch=tk.NO)
        self.table.column("col1", anchor=tk.W, width=100)
        self.table.column("col2", anchor=tk.W, width=100)
        self.table.column("col3", anchor=tk.W, width=100)
        self.table.column("col4", anchor=tk.W, width=100)
        self.table.column("col5", anchor=tk.W, width=100)
        self.table.column("col6", anchor=tk.W, width=100)
        self.table.column("col7", anchor=tk.W, width=100)
        self.table.column("col8", anchor=tk.W, width=100)
        self.table.column("col9", anchor=tk.W, width=100)
        self.table.column("col10", anchor=tk.W, width=100)
        self.table.column("col11", anchor=tk.W, width=100)

        # Configurar las cabeceras de las columnas
        self.table.heading("#0", text="")
        self.table.heading("col1", text="COL 1")
        self.table.heading("col2", text="COL 2")
        self.table.heading("col3", text="COL 3")
        self.table.heading("col4", text="COL 4")
        self.table.heading("col5", text="COL 5")
        self.table.heading("col6", text="COL 6")
        self.table.heading("col7", text="COL 7")
        self.table.heading("col8", text="COL 8")
        self.table.heading("col9", text="COL 9")
        self.table.heading("col10", text="COL 10")
        self.table.heading("col11", text="COL 11")

        # Agregar los registros a la tabla
        for idx, row in enumerate(data):
            self.table.insert(parent="", index=idx, iid=idx, values=row)

        # Cerrar la conexión a la base de datos
        db.close()