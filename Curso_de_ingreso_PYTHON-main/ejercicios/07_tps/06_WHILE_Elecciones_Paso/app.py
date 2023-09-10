'''
Nombre:Tomas Lautaro
Apellido:Diaz Zampella
...
Ejercicio: TP_06_WHILE_ELECCIONES
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) 
que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.

e. se pide ingresar el sexo (M , F , NB) , informar cuantos candidatos hay de cada sexo

f. se pide ingresar nivel de aceptacion de imagen del candidato (entre -100 y 100) informar el
nombre y sexo del que mejor nivel tiene 

g.de las personas de sexo femenino ,informar cuanta hay mayores a 50 y cuantas menores a esa edad

Todos los datos se ingresan por prompt y los resultados por consola (print)

h. de que sexo hubo mas candidatos


'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        
        flag_continuar = True
        minimo_votos = None
        maximo_votos = None
        total_votos_emitidos = 0
        candidato_mas_votado = ""
        candidato_menos_votado = ""
        edad_menos_votado = None
        acumulador_edad = 0
        contador_candidatos = 0
        contador_M = 0
        contador_F = 0
        contador_NB = 0
        nombre_mejor_nivel = None
        genero_mejor_nivel = ""
        mayor_nivel_aceptacion = None
        fem_mayor_50 = 0
        fem_menor_50 = 0
        genero_mas_candidatos = None

        while flag_continuar == True:
            
            nombre_candidato = prompt ("Nombre", "Ingrese el nombre del candidato")
            while nombre_candidato == None or nombre_candidato == "" or nombre_candidato == "":
                nombre_candidato = prompt ("Invalido", "Ingrese el nombre del candidato")


            edad_candidato = prompt ("Edad", "Ingrese la edad del candidato")

            while edad_candidato == None or int(edad_candidato) < 25 or edad_candidato == "":
             edad_candidato = prompt ("Invalido", "Ingrese la edad del candidato")   
            
            cantidad_votos = prompt("Voto", "Ingrese votos")
            
            while cantidad_votos == None or int (cantidad_votos) < 0 or cantidad_votos == "":
                cantidad_votos = prompt ("Invalido", "Ingrese la edad del candidato")  

            genero_candidato = prompt("Genero","Ingrese genero (M , F , NB)" )
            while genero_candidato != "M" and genero_candidato != "F" and genero_candidato != "NB":
                genero_candidato = prompt("Invalido","Ingrese genero (M , F , NB)" )

            nivel_aceptacion_ingresada = prompt ("Nivel aceptación de imagen", "Ingrese nivel aceptación del -100 al 100")
            while nivel_aceptacion_ingresada == nivel_aceptacion_ingresada.isalpha or int(nivel_aceptacion_ingresada) < -100 and int(nivel_aceptacion_ingresada) > 100 :
                nivel_aceptacion_ingresada = prompt ("Invalido", "Ingrese nivel aceptación del -100 al 100")


            edad_candidato = int(edad_candidato)
            cantidad_votos = int(cantidad_votos)

            acumulador_edad += edad_candidato
            contador_candidatos +=1
            total_votos_emitidos += cantidad_votos


            match genero_candidato:
                case "M" :
                    contador_M += 1
                    genero_candidato = "masculino"
                case "F" :
                    contador_F += 1
                    genero_candidato = "femenino"
                    if edad_candidato > 50 :
                        fem_mayor_50 += 1
                    else :
                        fem_menor_50 += 1
                case _:
                    contador_NB += 1
                    genero_candidato = "no binario"

            if mayor_nivel_aceptacion == None or nivel_aceptacion_ingresada > mayor_nivel_aceptacion :
                mayor_nivel_aceptacion = nivel_aceptacion_ingresada
                nombre_mejor_nivel = nombre_candidato
                genero_mejor_nivel = genero_candidato
            

            if maximo_votos == None or cantidad_votos > maximo_votos:
                maximo_votos = cantidad_votos
                candidato_mas_votado = nombre_candidato
            if minimo_votos == None or cantidad_votos < minimo_votos:
                minimo_votos = cantidad_votos
                candidato_menos_votado = nombre_candidato
                edad_menos_votado = edad_candidato

            if contador_F > contador_M and contador_F > contador_NB:
                genero_mas_candidatos = "femenino"
            
            if contador_M > contador_F and contador_M > contador_NB:
                genero_mas_candidatos = "masculino"
            else:
                genero_mas_candidatos = "no binario"


            flag_continuar = question("", "¿Quiere añadir un voto más?")
        
        promedio_edades = acumulador_edad / contador_candidatos

        print ("El candidato más votado es "+ candidato_mas_votado) #A
        print ("nombre y edad del candidato con menos votos es " + candidato_menos_votado +" "+ str(edad_menos_votado)+ " años") #B
        print ("El promedio de edades de los candidatos es "+ str(promedio_edades)) #C
        print ("El total de votos emitidos es " + str(total_votos_emitidos)) #D
        print ("Candidatos masculinos " + str(contador_M) + ", canditados femeninos " + str(contador_F) + ", candidatos no binarios " +\
                str (contador_NB)) #E
        print("El candidato con mayor nivel de aceptacion de imagen es " + (nombre_mejor_nivel) + ", " + (genero_mejor_nivel))#F
        print("Hay " + str(fem_mayor_50)+ " candidatas mayores a 50 años y " + str(fem_menor_50)+ " candidatas menores a 50 años") #G
        print ("Genero con más candidatos: " + str(genero_mas_candidatos))
                
            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()


