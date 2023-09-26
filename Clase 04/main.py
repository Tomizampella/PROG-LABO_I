from data_stark import lista_personajes
from stark_biblioteca import *


print("N. Normalizar los datos")
opcion_normalizacion = input("Seleccione la letra N para normalizar datos y acceder al menú ")

while opcion_normalizacion != "N" and opcion_normalizacion != "n":
    opcion_normalizacion = input("Error - Seleccione la letra N para normalizar datos y acceder al menú ")

estado_normalizacion = stark_normalizar_datos(lista_personajes)

if estado_normalizacion == True:
            print("Datos Normalizados\n")
            while (estado_normalizacion == True):
                print("Menú:")
                print("A. Normalizar datos (No se debe poder acceder a los otros puntos)")
                print("B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB")
                print("C. Recorrer la lista y determinar cuál es el superhéroe más alto de género F")
                print("D. Recorrer la lista y determinar cuál es el superhéroe más alto de género M")
                print("E. Recorrer la lista y determinar cuál es el superhéroe más débil de género M")
                print("F. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB")
                print("G. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB")
                print("H. Determinar cuántos superhéroes tienen cada tipo de color de ojos.")
                print("I. Determinar cuántos superhéroes tienen cada tipo de color de pelo.")
                print("J. Listar todos los superhéroes agrupados por color de ojos.")
                print("K. Listar todos los superhéroes agrupados por tipo de inteligencia")
                print("K. Salir\n")
                opcion_elegida = input("Seleccione una letra: ")


                match opcion_elegida:
                    case "A" | "a":
                            pass
                    case "B" | "b":
                            pass
                    case "C" | "c":
                            pass
                    case "D" | "d":
                            pass
                    case "E" | "e":
                            pass
                    case "F" | "f":
                            pass
                    case "G" | "g":
                            pass
                    case "H" | "h":
                            pass
                    case "I" | "i":
                            pass
                    case "J" | "j":
                            pass
                    case "K" | "k":
                            break      
else: 
            print("Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente")