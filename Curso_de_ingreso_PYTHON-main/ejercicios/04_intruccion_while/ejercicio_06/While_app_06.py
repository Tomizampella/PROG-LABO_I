import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre:Tomas Lautaro
Apellido:Diaz Zampella
...
Ejercicio: while_06
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar 5 números mediante prompt. 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        contador = 0
        cantidad_de_numeros = 5
        suma_acumulada = 0
        
        while contador < cantidad_de_numeros :
            numero_ingresado =prompt("Ingreso", "ingrese 5 numeros")
            
            if numero_ingresado == None:
                alert("", "Debe ingresar 5 numeros")
                break
                
            else:
                numero_ingresado_int = int(numero_ingresado)
                suma_acumulada += numero_ingresado_int
                contador += 1
            
        
        if contador == 5:
            promedio = suma_acumulada / cantidad_de_numeros

            self.txt_suma_acumulada.delete (0,"end")
            self.txt_suma_acumulada.insert (0,suma_acumulada)
            
            self.txt_promedio.delete (0,"end")
            self.txt_promedio.insert (0, promedio) 


        


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()