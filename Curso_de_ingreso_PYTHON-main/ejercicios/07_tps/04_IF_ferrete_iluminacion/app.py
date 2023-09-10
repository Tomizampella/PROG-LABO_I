import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Tomas Lautaro
apellido:Diaz Zampella
...
Ejercicio: TP4 FERRETE ILUMINACION CON MATCH

Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del
          30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca 
        el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento
          del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        marca = self.combobox_marca.get()
        cantidad_lamparas = int (self.combobox_cantidad.get())
        costo_lamparas = cantidad_lamparas * 800
        
        
        match cantidad_lamparas:  #A
            case 6 | 7 | 8 | 9 | 10 | 11| 12:
                descuento = costo_lamparas * 0.5
        
            case 5 :   #B
                match marca:
                    case "ArgentinaLuz":
                        descuento = costo_lamparas * 0.4
                    case _:
                         descuento = costo_lamparas * 0.3

            case 4: #C
                match marca:
                    case "ArgentinaLuz" | "FelipeLamparas":
                        descuento = costo_lamparas * 0.25
                    case _:
                        descuento = costo_lamparas * 0.2

            case 3 : #D
                match marca:
                    case "ArgentinaLuz":
                        descuento = costo_lamparas * 0.15
                    case "FelipeLamparas":
                        descuento = costo_lamparas * 0.10
                    case _:
                        descuento = costo_lamparas * 0.05
            case _:
                descuento = 0

        precio_final_C_DESCUENTO = costo_lamparas - descuento

        if precio_final_C_DESCUENTO > 4000:  #E
            descuento_extra = 0.05
            precio_final_C_DESCUENTO = precio_final_C_DESCUENTO - descuento_extra * precio_final_C_DESCUENTO

        
    
        mensaje = f"Usted compro {cantidad_lamparas} lamparas marca {marca}, precio final = ${precio_final_C_DESCUENTO}"

        alert("Iluminacion", message= mensaje)
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()