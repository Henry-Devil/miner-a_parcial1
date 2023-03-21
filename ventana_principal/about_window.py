import tkinter as tk


class AboutWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Acerca de")
        self.geometry("400x300")

        # Agregar la información del programa y los integrantes
        info_label = tk.Label(self, text="Producción de minerales y contraprestaciones económicas\n\nIntegrantes:Henry Viloria, George Ortiz, Jeremy Carrasquilla\n- Integrante 1\n- Integrante 2\n- Integrante 3")
        info_label.pack()