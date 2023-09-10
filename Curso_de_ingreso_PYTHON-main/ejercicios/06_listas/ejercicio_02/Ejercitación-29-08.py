import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón 'CARGAR' se le solicitarán tres números al usuario mediante el Dialog Prompt, los mismos deberán ser almacenados en un vector lista_datos. 
Al presionar el botón 'MOSTRAR', se deberán mostrar los números almacenados en el vector utilizando Dialog Alert para informar cada elemento.
'''
# Para cada amigo:
# - Nombre del amigo,
# - Plato principal elegido ("Pizza", "Hamburguesa", "Ensalada").
# - Cantidad de platos principales pedidos (debe ser al menos 1).
# - Bebida elegida ("Refresco", "Agua", "Jugo").
# - Cantidad de bebidas pedidas (debe ser al menos 1).


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.lista_de_nombres = ["Juan", "María", "Pedro", "Laura", "Carlos","Ana", "Luis", "Elena", "Miguel", "Sofía"]
        self.lista_plato_principal = ["Pizza", "Hamburguesa", "Ensalada", "Pizza","Hamburguesa", "Ensalada", "Pizza", "Hamburguesa", "Ensalada", "Pizza"]
        self.lista_cantidad_de_platos = [2, 1, 3, 2, 2, 4, 3, 1, 1, 3]
        self.lista_bebidas_elegidas = ["Refresco", "Agua", "Jugo", "Refresco","Agua", "Jugo", "Refresco", "Agua", "Jugo", "Refresco"]
        self.lista_cantidad_de_bebidas = [2, 1, 5, 3, 2, 5, 1, 2, 1, 3]
        self.lista_nombres_tipo_pizza = []
        self.lista_nombres_tipo_hamburguesa = []
        self.lista_nombres_tipo_ensalada = []
        self.lista_nombres_tipo_refresco = []
        self.lista_nombres_tipo_agua = []
        self.lista_nombres_mayor_3_pedidos = []
        self.lista_nombres_mayor_5_pedidos = []
        self.lista_nombres_mayor_7_pedidos = []
        self.lista_nombres_menor_3_pedidos = []
        self.lista_nombres_menor_5_pedidos = []


    def btn_mostrar_on_click(self):
        # A) El total gastado por el grupo (resultante del costo de los platos principales y las
        # bebidas), y la propina sugerida para el personal del restaurante (esta corresponde al
        # 10% del total gastado).
        cantidad_amigos = len(self.lista_de_nombres)
        precio_unidad_plato_principal = 800
        precio_unidad_bebida = 200
        cantidad_total_platos = 0
        cantidad_total_bebidas = 0
        gasto_total_bebidas = None
        gasto_total_platos = None
        total_gastado = None
        contador_jugo = 0
        gasto_total_jugo = None
        contador_pizza = 0
        contador_ensalada = 0
        contador_hamburguesa = 0
        cantidad_maximo_pedidos = None
        nombre_maximo_pedidos = None
        #A
        for indice in range(cantidad_amigos):
            
            match self.lista_bebidas_elegidas[indice]: #B
                case "Jugo":
                    contador_jugo = contador_jugo + 1
                case "Refresco":
                    self.lista_nombres_tipo_refresco.append(self.lista_de_nombres[indice]) #E.3
                case _:
                    self.lista_nombres_tipo_agua.append(self.lista_de_nombres[indice]) #E.4
            
            match self.lista_plato_principal[indice]: #C
                case "Pizza":
                    contador_pizza = contador_pizza + 1
                    self.lista_nombres_tipo_pizza.append(self.lista_de_nombres[indice]) #E.0

                case "Ensalada":
                    contador_ensalada = contador_ensalada + 1
                    self.lista_nombres_tipo_ensalada.append(self.lista_de_nombres[indice]) #E.0

                case _:
                    contador_hamburguesa = contador_hamburguesa + 1
                    self.lista_nombres_tipo_hamburguesa.append(self.lista_de_nombres[indice]) #E.1

            pedidos_total_por_persona = self.lista_cantidad_de_bebidas[indice] + self.lista_cantidad_de_platos[indice] #D
            if cantidad_maximo_pedidos == None or cantidad_maximo_pedidos < pedidos_total_por_persona:
                cantidad_maximo_pedidos = pedidos_total_por_persona
                nombre_maximo_pedidos = self.lista_de_nombres[indice]
            
            
            if pedidos_total_por_persona > 3:  #E.5
                    self.lista_nombres_mayor_3_pedidos.append(self.lista_de_nombres[indice]) #E.5
            
            if pedidos_total_por_persona > 5:
                    self.lista_nombres_mayor_5_pedidos.append(self.lista_de_nombres[indice]) #E.6
            
            if pedidos_total_por_persona > 7:
                    self.lista_nombres_mayor_7_pedidos.append(self.lista_de_nombres[indice]) #E.7
            
            if pedidos_total_por_persona < 3:
                    self.lista_nombres_menor_3_pedidos.append(self.lista_de_nombres[indice]) #E.8
            
            if pedidos_total_por_persona < 5:
                    self.lista_nombres_menor_5_pedidos.append(self.lista_de_nombres[indice]) #E.9
                

            cantidad_total_platos = cantidad_total_platos + self.lista_cantidad_de_platos[indice]
            cantidad_total_bebidas =  cantidad_total_bebidas + self.lista_cantidad_de_bebidas[indice]
        
        gasto_total_platos = cantidad_total_platos * precio_unidad_plato_principal
        gasto_total_bebidas = cantidad_total_bebidas * precio_unidad_bebida
        total_gastado = gasto_total_platos + gasto_total_bebidas
        propina = total_gastado * 0.1 #A

        print (f"El total gastado por el grupo es ${total_gastado} y la propina es de ${propina}")

        # B) Promedio del dinero gastado en “Jugo”, sobre el grupo de amigos en general.
        gasto_total_jugo = contador_jugo * precio_unidad_bebida
        promedio_gasto_en_jugo = (gasto_total_jugo * 100) / gasto_total_bebidas

        print (f"El promedio del dinero gastado en “Jugo” es {promedio_gasto_en_jugo}%, sobre el grupo de amigos en general")

        # C) Los porcentajes de cada tipo de platos pedidos (teniendo en cuenta su cantidad).
        # Ejemplo: [30% pizza, 40% ensaladas, 30% hamburguesas]
        porcentaje_total_pizza = (contador_pizza * 100) / cantidad_total_platos
        porcentaje_total_ensalada = (contador_ensalada * 100) / cantidad_total_platos
        porcentaje_total_hamburguesa = 100 - (porcentaje_total_pizza + porcentaje_total_ensalada)

        print (f"Los porcentajes de cada tipo de platos pedidos son: {porcentaje_total_pizza:.2f}% pizza, {porcentaje_total_ensalada:.2f}% ensaladas, {porcentaje_total_hamburguesa:.2f}% hamburguesas")
        
        #  D) Además, desean premiar al amigo que realizó la mayor CANTIDAD de pedidos en total
        # (platos principales + bebidas) con una entrada gratuita para otra atracción del parque
        # "Aventuras Extremas".
        print (f"La persona que realizó la mayor CANTIDAD de pedidos en total es {nombre_maximo_pedidos} con {cantidad_maximo_pedidos} pedidos")

        #E.0
        print (f"Amigos que hayan elegido platos principales del tipo Pizza {self.lista_nombres_tipo_pizza}")
        #E.1
        print (f"Amigos que hayan elegido platos principales del tipo hamburguesa {self.lista_nombres_tipo_hamburguesa}")  
        #E.2
        print (f"Amigos que hayan elegido platos principales del tipo ensalada {self.lista_nombres_tipo_ensalada}")  
        #E.3
        print (f"Amigos que hayan elegido bibidas del tipo refresco {self.lista_nombres_tipo_refresco}")     
        #E.4
        print (f"Amigos que hayan elegido bibidas del tipo agua {self.lista_nombres_tipo_agua}")    
        #E.5
        print (f"Amigos que hayan realizado más de 3 pedidos en total {self.lista_nombres_mayor_3_pedidos}")
        #E.6
        print (f"Amigos que hayan realizado más de 5 pedidos en total {self.lista_nombres_mayor_5_pedidos}")
        #E.7
        print (f"Amigos que hayan realizado más de 7 pedidos en total {self.lista_nombres_mayor_7_pedidos}")
        #E.8
        print (f"Amigos que hayan realizado menos de 3 pedidos en total {self.lista_nombres_menor_3_pedidos}")
        #E.9
        print (f"Amigos que hayan realizado menos de 5 pedidos en total {self.lista_nombres_menor_5_pedidos}")



#         5.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado más
# de 3 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.
# 6.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado más
# de 5 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.
# 7.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado más
# de 7 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.
# 8.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado menos
# de 3 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.
# 9.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado menos
# de 5 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.

    
    def btn_cargar_on_click(self):
        #   Nombre del amigo
        nombre = input("nombre del amigo")
        while nombre == None or not nombre.isalpha():
            nombre = input("nombre del amigo correctamente")  

        self.lista_de_nombres.append(nombre)

        # - Plato principal elegido ("Pizza", "Hamburguesa", "Ensalada").
        plato_principal = input("Plato principal elegido")
        while plato_principal != "Pizza" and plato_principal != "Hamburguesa" and plato_principal != "Ensalada":
           plato_principal = input("Plato principal elegido correctamente") 
        
        self.lista_plato_principal.append(plato_principal)

        # - Cantidad de platos principales pedidos (debe ser al menos 1).
        cantidad_platos_principales = input ("Cantidad de platos principales pedidos")
        while int(cantidad_platos_principales) < 1:
           cantidad_platos_principales = input ("Cantidad de platos principales pedidos correctamente") 
        
        self.lista_cantidad_de_platos.append(cantidad_platos_principales)

        # - Bebida elegida ("Refresco", "Agua", "Jugo").
        bebida = input("Bebida elegida")
        while bebida != "Refresco" and bebida != "Agua" and bebida != "Jugo":
            bebida = input("Bebida elegida correctamente")

        self.lista_bebidas_elegidas.append(bebida)
        
        # - Cantidad de bebidas pedidas (debe ser al menos 1).
        cantidad_bebidas = input ("Cantidad de bebidas pedidas")
        while int(cantidad_bebidas) < 1:
           cantidad_bebidas = input ("Cantidad de bebidas pedidas correctamente") 

        self.lista_cantidad_de_bebidas.append(cantidad_bebidas)

        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
        