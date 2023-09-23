from data import lista_personajes
from funciones import *
#TP Stark 02 - Tomas Lautaro Diaz Zampella




while (True):
    print("Menú:")
    print("A. Nombre de cada superhéroe de género NB")
    print("B. Superhéroe más alto de género F")
    print("C. Superhéroe más alto de género M")
    print("D. Superhéroe más débil de género M")
    print("E. Superhéroe más débil de género NB")
    print("F. Fuerza promedio de los superhéroes de género NB")
    print("G. Cantidad de superhéroes por cada tipo de color de ojos")
    print("H. Cantidad de superhéroes por cada tipo de color de pelo")
    print("I. Superhéroes agrupados por color de ojos")
    print("J. Superhéroes agrupados por tipo de inteligencia")
    print("K. Salir\n")
    

    opcion_elegida = input("Seleccione una letra: ")


    match opcion_elegida:
       case "A" | "a":
              muestra_nombres_heroe_genero_nb ()
       case "B" | "b":
              calcular_heroe_mas_alto_femenino()
       case "C" | "c":
              calcular_heroe_mas_alto_masculino()
       case "D" | "d":
              calcular_heroe_mas_debil_masculino()
       case "E" | "e":
              calcular_heroe_mas_debil_no_binario()
       case "F" | "f":
              calcular_fuerza_promedio_genero_nb()
       case "G" | "g":
              calcular_heroes_por_color_ojos()
       case "H" | "h":
              calcular_heroes_por_color_pelo()
       case "I" | "i":
              listar_heroes_por_color_ojos()
       case "J" | "j":
              listar_heroes_por_tipo_inteligencia()
       case "K" | "k":
              break
