import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Nombre:Tomas Lautaro
Apellido:Diaz Zampella
...
Ejercicio: while_03
Enunciado:
Al presionar el botón ‘Pedir clave’, solicitar al usuario que ingrese una contraseña mediante prompt. 
Comprobar que la contraseña ingresada sea ‘utn750’. En caso de no coincidir, volverla a solicitar hasta que coincidan
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_pedir_clave = customtkinter.CTkButton(master=self, text="Pedir clave", command=self.btn_pedir_clave_on_click)
        self.btn_pedir_clave.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_pedir_clave_on_click(self):
        contraseña = prompt(title = "Acceso", prompt = "Ingrese su contraseña")
        ingreso = True
        
        while contraseña != "utn750" :
            contraseña = prompt(title = "Acceso", prompt = "Ingrese su contraseña")

        while contraseña == "utn750" and ingreso == True:
            mensaje = "Usuario logueado"
            ingreso = False


        alert(title = "Acceso", message = mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()