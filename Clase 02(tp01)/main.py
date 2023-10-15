from data import lista_personajes
#TP Stark 01 - Tomas Lautaro Diaz Zampella

maximo_fuerza = None
minimo_altura = None
contador_masculino = 0
acumulador_peso_masc = 0
contador_femenino = 0
acumulador_fuerza_fem = 0

while (True):
    print("Menú:")
    print("A. Imprime todos los datos de cada superhéroe")
    print("B. Imprime la identidad y el peso del superhéroe con mayor fuerza")
    print("C. Imprime el nombre e identidad del superhéroe más bajo")
    print("D. Imprime el peso promedio de los superhéroes masculinos")
    print("E. Imprime nombre y peso de los superhéroes los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino")
    print("F. Salir\n")

    opcion_elegida = input("Seleccione una letra: ")


    match opcion_elegida:
        case "A" | "a":
            for heroe in lista_personajes:
                print("Nombre:", heroe["nombre"])
                print("Identidad:", heroe["identidad"])
                print("Altura:", heroe["altura"])
                print("Peso:", heroe["peso"])
                print("Genero:", heroe["genero"])
                print("Color de ojos:", heroe["color_ojos"])
                print("Color de pelo:", heroe["color_pelo"])
                print("Fuerza:", heroe["fuerza"])
                print("inteligencia:", heroe["inteligencia"], "\n")
                
                

        case "B" | "b":
            for heroe in lista_personajes:
        
                if maximo_fuerza == None or maximo_fuerza < int(heroe["fuerza"]):
                    maximo_fuerza = int(heroe["fuerza"])
            
            print("Superhéroes con mayor fuerza")
            for heroe in lista_personajes:
                if maximo_fuerza == int(heroe["fuerza"]): #B
                    print("Identidad:", heroe["identidad"])
                    print("Peso:", float(heroe["peso"]), "kg")
                    print("")
        
        case "C" | "c":
            for heroe in lista_personajes:
                
                if minimo_altura == None or minimo_altura > float(heroe["altura"]):
                    minimo_altura = float(heroe["altura"])
                    minimo_altura_identidad = heroe["identidad"]
                    minimo_altura_nombre = heroe["nombre"]
            print (f"El superhéroe más bajo es {minimo_altura_nombre} y su identidad es {minimo_altura_identidad} \n") #C
        
        case "D" | "d":
            for heroe in lista_personajes:
                
                if heroe["genero"] == "M":
                        contador_masculino = contador_masculino + 1
                        acumulador_peso_masc = acumulador_peso_masc + float(heroe["peso"])
            
            promedio_peso_masc = acumulador_peso_masc / contador_masculino        
            print (f"El peso promedio de los superhéroes masculinos es {promedio_peso_masc :.0f} kg\n") #D       

        case "E" | "e":
            for heroe in lista_personajes:
                
                if heroe["genero"] == "F":
                    contador_femenino = contador_femenino + 1 #E
                    acumulador_fuerza_fem = acumulador_fuerza_fem + float(heroe["fuerza"])     
            
            promedio_fuerza_fem = acumulador_fuerza_fem / contador_femenino
            
            print("Nombre y peso de los superhéroes los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino\n")
            for heroe in lista_personajes:
                if float(heroe["fuerza"]) > promedio_fuerza_fem:
                    print("Nombre:", heroe["nombre"])
                    print("Peso:", float(heroe["peso"]),"kg\n")
                       

        case "F" | "f":
            break

        case _:
            print("Ingrese una letra de la A a la F")         
                
