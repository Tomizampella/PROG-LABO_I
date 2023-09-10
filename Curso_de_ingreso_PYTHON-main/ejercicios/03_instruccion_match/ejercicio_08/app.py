import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre:Tomas Lautaro
apellido:Diaz Zampella
...
Ejercicio: match_08
...
Enunciado:
Obtener el destino seleccionado en el combobox_destino, luego al presionar el botón 
‘Informar’ indicar mediante alert si en el destino hace frío o calor la mayoría 
de las estaciones del año.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Ushuaia']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        destino = self.combobox_destino.get()
        match (destino):
            case ("Bariloche"):
                clima = "frio"
            case ("Mar del plata"):
                clima = "calor"
            case ("Cataratas"):
                clima = "calor"
            case ("Ushuaia"):
                clima = "frio"      
        
        mensaje = f"En {destino} hace {clima} la mayoría de las estaciones del año"
        alert(title="Clima", message= mensaje)
    
    
if __name__ == "__main__":
    app = App()
    app.mainloop()