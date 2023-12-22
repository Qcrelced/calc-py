import tkinter as tk
from modules.const import *
from math import sqrt, sin, cos, pi, log

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("380x500")
        self.resizable(False, False)

        for i in range(15):
            self.grid_rowconfigure(i)

        #Création des parties de la calculatrice
        self.frame = tk.Frame(self)
        self.frame.grid(row=0, column=0, rowspan=2)
        self.frame2 = tk.Frame(self)
        self.frame2.grid(row=3, column=0, rowspan=10)
        self.frame3 = tk.Frame(self)
        self.frame3.grid(row=13, column=0, rowspan=15)

        self.result_var = tk.StringVar()
        self.result_var.set("")

        self.entry = tk.Entry(self.frame, textvariable=self.result_var, font=("Helvetica", 20), justify="right", bd=10, width=24)
        self.entry.grid(row=0, column=0)

        # Définition du mode et création des boutons
        self.mode = "standard"
        self.create_buttons()

    # Définition des bouton en fonction du mode
    def create_buttons(self):
        buttons = [
            ['%', 'CE', 'C', 'DEL'],
            ['1/x', 'x²', '2Rx', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['MODE', '0', '.', '='],
        ]

        buttons_scientific = [
            ['sin', 'cos', 'tan', 'log'],
            ['(', ')', 'π', 'ln'],
            ['10^x']
        ]

        # Ajout des boutons sur l'application
        for row, line in enumerate(buttons):
            for col, text in enumerate(line):
                button = tk.Button(self.frame2, text=text, font=("Helvetica", 18), command=lambda t=text: self.on_button_click(t), width=6)
                if self.mode == "scientific":
                    for row, line in enumerate(buttons_scientific):
                        for col, text in enumerate(line):
                            button = tk.Button(self.frame3, text=text, font=("Helvetica", 18), command=lambda t=text: self.on_button_click(t), width=6)
                            button.grid(row=row, column=col)
                button.grid(row=row, column=col)

    def toggle_scientific_mode(self, ):
            self.mode = "scientific"
            self.create_buttons()

    # Renvoie la commande en fonction du bouton
    def on_button_click(self, button_text):
        current_text = self.result_var.get()
        match button_text:
            case "=":
                try:
                    result = eval(self.result_var.get())
                    self.result_var.set(result)
                except ZeroDivisionError:
                    self.result_var.set("Error Zero Division")
                except Exception as e:
                    self.result_var.set("Error")
            case "CE":
                self.result_var.set("")
            case "C":
                self.result_var.set("")
            case "DEL":
                TEMP = self.result_var.get()
                TEMP = TEMP[:-1]
                self.result_var.set(TEMP)
            case "x²":
                result = (current_text + "**2")
                self.result_var.set(str(result))
            case '%':
                # self.result_var.set(current_text)
                self.result_var.set("")
            case "2Rx":
                self.result_var.set(str(sqrt(float(current_text))))
            case "1/x":
                self.result_var.set(str(1 / int(current_text)))
            case "MODE":
                self.toggle_scientific_mode()
            case "(", ")":
                self.result_var.set(current_text + button_text)
            case "log":
                self.result_var.set(log(int(current_text), 10))
            case "ln":
                self.result_var.set(log(int(current_text)))
            case "π":
                self.result_var.set(current_text + str(pi))
            case "10^x":
                self.result_var.set((10 ** int(current_text) ))
            case _:
                current_text = self.result_var.get()
                if current_text == "0":
                    self.result_var.set(button_text)
                else:
                    self.result_var.set(current_text + button_text)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
