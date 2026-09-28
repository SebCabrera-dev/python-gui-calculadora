import tkinter as tk
from tkinter import messagebox
import math

class CalculadoraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Interactiva")
        self.root.geometry("380x520")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")  # Tema oscuro

        self.expresion = ""

        # --- PANTALLA / DISPLAY ---
        self.pantalla = tk.Entry(
            root, 
            font=("Arial", 22, "bold"), 
            bg="#313244", 
            fg="#cdd6f4", 
            bd=0, 
            justify="right",
            insertbackground="white"
        )
        self.pantalla.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=18, padx=15, pady=20, sticky="nsew")

        # --- DEFINICIÓN DE BOTONES ---
        botones = [
            ('C', 1, 0, '#f38ba8'), ('√', 1, 1, '#89b4fa'), ('^', 1, 2, '#89b4fa'), ('/', 1, 3, '#fab387'),
            ('7', 2, 0, '#45475a'), ('8', 2, 1, '#45475a'), ('9', 2, 2, '#45475a'), ('*', 2, 3, '#fab387'),
            ('4', 3, 0, '#45475a'), ('5', 3, 1, '#45475a'), ('6', 3, 2, '#45475a'), ('-', 3, 3, '#fab387'),
            ('1', 4, 0, '#45475a'), ('2', 4, 1, '#45475a'), ('3', 4, 2, '#45475a'), ('+', 4, 3, '#fab387'),
            ('0', 5, 0, '#45475a'), ('.', 5, 1, '#45475a'), ('=', 5, 2, '#a6e3a1')
        ]

        # Configurar expansión de filas/columnas
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.root.grid_columnconfigure(j, weight=1)

        # Crear botones en la interfaz
        for item in botones:
            texto = item[0]
            f = item[1]
            c = item[2]
            color_bg = item[3]
            colspan = 2 if texto == '=' else 1
            btn = tk.Button(
                root, 
                text=texto, 
                font=("Arial", 14, "bold"), 
                bg=color_bg, 
                fg="#11111b" if color_bg in ['#f38ba8', '#89b4fa', '#fab387', '#a6e3a1'] else "#cdd6f4",
                activebackground="#585b70",
                bd=0,
                command=lambda t=texto: self.on_button_click(t)
            )
            btn.grid(row=f, column=c, columnspan=colspan, padx=5, pady=5, sticky="nsew")

    def on_button_click(self, char):
        if char == 'C':
            self.expresion = ""
            self.actualizar_pantalla()
        elif char == '=':
            self.calcular_resultado()
        elif char == '√':
            try:
                val = float(self.pantalla.get())
                if val < 0:
                    messagebox.showerror("Error", "No existe raíz real de número negativo")
                else:
                    res = math.sqrt(val)
                    self.expresion = str(res)
                    self.actualizar_pantalla()
            except ValueError:
                messagebox.showerror("Error", "Entrada no válida para raíz")
        elif char == '^':
            self.expresion += "**"
            self.actualizar_pantalla()
        else:
            self.expresion += str(char)
            self.actualizar_pantalla()

    def actualizar_pantalla(self):
        self.pantalla.delete(0, tk.END)
        self.pantalla.insert(0, self.expresion)

    def calcular_resultado(self):
        try:
            if not self.expresion:
                return
            # Evaluar la expresión matemática
            resultado = eval(self.expresion)
            self.expresion = str(resultado)
            self.actualizar_pantalla()
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir por cero")
            self.expresion = ""
            self.actualizar_pantalla()
        except Exception:
            messagebox.showerror("Error", "Expresión matemática inválida")
            self.expresion = ""
            self.actualizar_pantalla()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()