import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre:Tomas Lautaro
Apellido:Diaz Zampella
...
Ejercicio: For_08

Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        for _ in range(100):
            numero_ingresado = prompt("Numero", "Ingrese un numero")
            
            if numero_ingresado == None:
                break
            numero_ingresado = int(numero_ingresado)
            if numero_ingresado % 2 != 0:
                mensaje ="Número primo"
            else :
                mensaje ="Número par"
            alert("", mensaje)

        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()