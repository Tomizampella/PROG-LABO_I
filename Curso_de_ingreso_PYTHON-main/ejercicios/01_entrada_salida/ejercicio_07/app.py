import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Tomas Lautaro
apellido:Diaz Zampella
---
Ejercicio: entrada_salida_07
---
Enunciado:
Al presionar el botón  que corresponde a cada operación (suma, resta, multiplicación, y división), 
se deberán obtener los valores contenidos en las cajas de texto (txtOperadorA y txtOperadorB), 
transformarlos en números enteros, realizar dicha operación y luego mostrar el resultado 
de la misma utilizando el Dialog Alert. Ej: "El resultado de la …… es: 755"  
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Operador A")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_operador_a = customtkinter.CTkEntry(master=self)
        self.txt_operador_a.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="Operador B")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_operador_b = customtkinter.CTkEntry(master=self)
        self.txt_operador_b.grid(row=1, column=1)
        
        self.btn_sumar = customtkinter.CTkButton(master=self, text="Sumar", command=self.btn_sumar_on_click)
        self.btn_sumar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_restar = customtkinter.CTkButton(master=self, text="Restar", command=self.btn_restar_on_click)
        self.btn_restar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_multiplicar = customtkinter.CTkButton(master=self, text="Multiplicar", command=self.btn_multiplicar_on_click)
        self.btn_multiplicar.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_dividir = customtkinter.CTkButton(master=self, text="Dividir", command=self.btn_dividir_on_click)
        self.btn_dividir.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def btn_sumar_on_click(self):
        sumando_texto_a = self.txt_operador_a.get()
        sumando_texto_b = self.txt_operador_b.get ()
        sumando_numero_a = int(sumando_texto_a)
        sumando_numero_b = int (sumando_texto_b)

        resultado = sumando_numero_a + sumando_numero_b
        alert("Producto", "El resultado de la suma es " + str(resultado) )


    def btn_restar_on_click(self):
        restando_texto_a = self.txt_operador_a.get()
        restando_texto_b = self.txt_operador_b.get ()
        restando_numero_a = int(restando_texto_a)
        restando_numero_b = int(restando_texto_b)

        resultado = restando_numero_a - restando_numero_b
        alert("Producto", "El resultado de la resta es " + str(resultado) )

    def btn_multiplicar_on_click(self):
        Multiplicando_texto_a = self.txt_operador_a.get()
        Multiplicando_texto_b = self.txt_operador_b.get ()
        Multiplicando_numero_a = int(Multiplicando_texto_a)
        Multiplicando_numero_b = int(Multiplicando_texto_b)

        resultado = Multiplicando_numero_a * Multiplicando_numero_b
        alert("Producto", "El resultado de la multiplicación es " + str(resultado) )

    def btn_dividir_on_click(self):
        Dividiendo_texto_a = self.txt_operador_a.get()
        Dividiendo_texto_b = self.txt_operador_b.get ()
        Dividiendo_numero_a = int(Dividiendo_texto_a)
        Dividiendo_numero_b = int(Dividiendo_texto_b)

        resultado = Dividiendo_numero_a / Dividiendo_numero_b
        alert("Producto", "El resultado de la división es " + str(resultado) )
        
if __name__ == "__main__":
    app = App()
    app.mainloop()