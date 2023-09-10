import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre:Tomas Lautaro
Apellido:Diaz Zampella
...
Ejercicio: TP_08_LISTAS_CONTEO
...
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos
    
    nivel A:
    i. el listado de numeros pares
    j. que se ingreso mas ?, positivos , negativos o ceros

    nivel Ninja:
    k. el listado de los numeros mayores , si es que hay mas de un mayor

Informar los resultados mediante alert()

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                             columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.lista = []
        

    def btn_comenzar_ingreso_on_click(self):
        numero_ingresado = ""
        
        while numero_ingresado != None:
            numero_ingresado = prompt ("", "Ingrese un numero")

            if numero_ingresado != None:
                numero_ingresado = int(numero_ingresado)
                self.lista.append (numero_ingresado)
        
        

                
    def btn_mostrar_estadisticas_on_click(self):
    
        acumulador_negativos = 0
        acumulador_positivos = 0
        contador_positivos = 0
        contador_negativos = 0
        contador_ceros = 0
        minimo_negativos = None
        maximo_positivos = None
        lista_numeros_pares = []
        lista_numeros_mayores = []
        for i in self.lista:
            if i < 0:
                acumulador_negativos += i
                contador_negativos += 1
                if minimo_negativos == None or i > minimo_negativos:
                    minimo_negativos = i
            elif i > 0:
                acumulador_positivos += i
                contador_positivos += 1
                if maximo_positivos == None or i > maximo_positivos:
                    maximo_positivos = i
                    lista_numeros_mayores = []
                
                if maximo_positivos == i:
                    lista_numeros_mayores.append(i)
            
            else:
                contador_ceros += 1
            
            if i % 2 == 0:
                lista_numeros_pares.append(i)
                
        
        if contador_negativos != 0: 
            promedio_negativos = acumulador_negativos / contador_negativos
            promedio_negativos = abs(promedio_negativos)
        else:
            promedio_negativos = 0
        
        if contador_positivos > contador_negativos and contador_positivos > contador_ceros:
            numero_mas_ingresado = "positivos"
        elif contador_negativos > contador_positivos and contador_negativos > contador_ceros:
            numero_mas_ingresado = "negativos"
        else:
            numero_mas_ingresado = "ceros"

    
        mensaje = (f"La suma acumulada de numeros negativos es {acumulador_negativos}\n") #a 
        mensaje +=(f"La suma acumulada de numeros positivos es {acumulador_positivos}\n") #b
        mensaje +=(f"La cantidad de números positivos ingresados es {contador_positivos}\n") #c
        mensaje +=(f"La cantidad de números negativos ingresados es {contador_negativos}\n") #d
        mensaje +=(f"La cantidad de ceros ingresados es {contador_ceros}\n") #e
        mensaje +=(f"El minimo de los numeros negativos es {minimo_negativos}\n") #f
        mensaje +=(f"El máximo de los numeros positivos es {maximo_positivos}\n") #g
        mensaje +=(f"El promedio de los negativos es {promedio_negativos}\n") #h
        mensaje +=(f"Listado de numeros pares {lista_numeros_pares}\n") #i
        mensaje +=(f"Se ingresaron en mayor medida {numero_mas_ingresado}\n") #j
        mensaje +=(f"El listado de los numeros mayores es {lista_numeros_mayores}") #k 

        alert("Estadisticas", mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
