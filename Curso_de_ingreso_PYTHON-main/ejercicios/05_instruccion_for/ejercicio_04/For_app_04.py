import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre:Tomas Lautaro
Apellido:Diaz Zampella
...
Ejercicio: For_04

Al presionar el botón Mostrar pedir valores por prompt hasta que el usuario ingrese el valor 9 (se deberá utilizar 'BREAK').
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        iteracion = [0]
        for i in iteracion:
            numero_ingresado =prompt("Ingreso", "Ingrese un numero")
            if numero_ingresado == "9":
                break
            
            iteracion.append (1)    #uso Metodo append que suma +1 a la lista hasta que se ingrese "9"
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()