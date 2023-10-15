from data import lista_personajes
#TP Stark 02 - Tomas Lautaro Diaz Zampella

#A
def muestra_nombres_heroe_genero_nb ():
    '''Muestra los nombres de los superhéroes de género NB'''
    contador_nb = 0
    for heroe in lista_personajes:
            if heroe["genero"] == "NB":
              mensaje = print("Nombre:", heroe["nombre"])
              contador_nb = contador_nb + 1
    if contador_nb == 0:
       mensaje = print("No hay superhéroes de género NB")
    
    return mensaje
#B
def calcular_heroe_mas_alto_femenino ():
    '''Calcula el superhéroe más alto de género F'''
    maxima_altura_f = None
    maxima_altura_f_nombre = None
    for heroe in lista_personajes:
            if heroe["genero"] == "F":
                 if maxima_altura_f == None or maxima_altura_f < float(heroe["altura"]):
                    maxima_altura_f = float(heroe["altura"])
                    maxima_altura_f_nombre = heroe["nombre"]
    mensaje = print (f"El superhéroe más alto de genero femenino es {maxima_altura_f_nombre} \n")
    
    return mensaje
#C
def calcular_heroe_mas_alto_masculino ():
    '''Calcula el superhéroe más alto de género M'''
    maxima_altura_m = None
    maxima_altura_m_nombre = None
    for heroe in lista_personajes:
            if heroe["genero"] == "M":
                 if maxima_altura_m == None or maxima_altura_m < float(heroe["altura"]):
                    maxima_altura_m = float(heroe["altura"])
                    maxima_altura_m_nombre = heroe["nombre"]
    mensaje = print (f"El superhéroe más alto de genero masculino es {maxima_altura_m_nombre} \n")
    
    return mensaje
#D
def calcular_heroe_mas_debil_masculino ():
    '''Calcula el superhéroe más débil de género M'''
    minima_fuerza_m = None
    minima_fuerza_m_nombre = None
    for heroe in lista_personajes:
            if heroe["genero"] == "M":
                 if minima_fuerza_m == None or minima_fuerza_m > float(heroe["fuerza"]):
                    minima_fuerza_m = float(heroe["fuerza"])
                    minima_fuerza_m_nombre = heroe["nombre"]
    mensaje = print (f"El superhéroe más débil de genero masculino es {minima_fuerza_m_nombre} \n")
    
    return mensaje
#E
def calcular_heroe_mas_debil_no_binario ():
    '''Calcula el superhéroe más débil de género NB'''
    minima_fuerza_nb = None
    minima_fuerza_nb_nombre = None
    for heroe in lista_personajes:
            if heroe["genero"] == "NB":
                 if minima_fuerza_nb == None or minima_fuerza_nb > float(heroe["fuerza"]):
                    minima_fuerza_nb = float(heroe["fuerza"])
                    minima_fuerza_nb_nombre = heroe["nombre"]
    if minima_fuerza_nb_nombre != None:
       mensaje = print (f"El superhéroe más débil de genero no binario es {minima_fuerza_nb_nombre} \n")
    else:
       mensaje = print("No hay superhéroes de género NB")
    
    return mensaje   
#F
def calcular_fuerza_promedio_genero_nb ():
    '''Calcula la fuerza promedio de los superhéroes de género NB'''
    contador_no_binario = 0
    acumulador_fuerza_nb = 0
    for heroe in lista_personajes:
                
                if heroe["genero"] == "NB":
                        contador_no_binario = contador_no_binario + 1
                        acumulador_fuerza_nb = acumulador_fuerza_nb + float(heroe["fuerza"])
       
    if contador_no_binario != 0: 
       promedio_fuerza_nb = acumulador_fuerza_nb / contador_no_binario  
       mensaje = print (f"La fuerza promedio de los superhéroes de genero no binario es {promedio_fuerza_nb :.0f} kg\n") #D   
    else:
       mensaje = print("No hay superhéroes de género NB")
    
    return mensaje   
#G
def calcular_heroes_por_color_ojos ():
    '''Calcula la cantidad de superhéroes por color de ojos'''
    
    contador_red = 0
    contador_brown = 0
    contador_yellow_no_irises = 0
    contador_silver = 0
    contador_blue = 0
    contador_yellow = 0
    contador_hazel = 0
    contador_green = 0 
    
    
    for heroe in lista_personajes:
         match heroe["color_ojos"]:
            case "Red":
                   contador_red = contador_red + 1
            case "Brown":
                   contador_brown = contador_brown + 1
            case "Yellow (without irises)":
                   contador_yellow_no_irises = contador_yellow_no_irises + 1
            case "Silver":
                   contador_silver = contador_silver + 1
            case "blue" | "Blue":
                   contador_blue = contador_blue + 1
            case "Yellow":
                     contador_yellow = contador_yellow + 1
            case "Hazel":
                     contador_hazel = contador_hazel + 1
            case "Green":
                     contador_green = contador_green + 1
    
    mensaje = print(f"Red: {contador_red}\n\
Brown: {contador_brown}\n\
Yellow (without irises): {contador_yellow_no_irises}\n\
Silver: {contador_silver}\n\
Blue: {contador_blue}\n\
Yellow: {contador_yellow}\n\
Hazel: {contador_hazel}\n\
Green: {contador_green}\n")
    
    return mensaje
    
#H
def calcular_heroes_por_color_pelo ():
    '''Calcula la cantidad de superhéroes por color de pelo'''
    
    contador_black = 0
    contador_no_hair = 0
    contador_red_orange = 0
    contador_blond = 0
    contador_green = 0
    contador_brown_white = 0
    contador_white = 0
    contador_auburn = 0
    contador_yellow = 0
    contador_red = 0
    contador_brown = 0
    
    
    for heroe in lista_personajes:
       match heroe["color_pelo"]:
              case "Black":
                     contador_black = contador_black + 1
              case "No Hair" | "":
                     contador_no_hair = contador_no_hair + 1
              case "Red / Orange":
                     contador_red_orange = contador_red_orange + 1
              case "Blond" | "blond":
                     contador_blond = contador_blond + 1
              case "Green":
                     contador_green = contador_green + 1
              case "Brown / White":
                     contador_brown_white = contador_brown_white + 1
              case "White":
                     contador_white = contador_white + 1
              case "Auburn":
                     contador_auburn = contador_auburn + 1
              case "Yellow":
                     contador_yellow = contador_yellow + 1
              case "Red":
                     contador_red = contador_red + 1
              case "Brown":
                     contador_brown = contador_brown + 1
            
    mensaje = print(f"No hair: {contador_no_hair}\n\
Black: {contador_black}\n\
Red / Orange: {contador_red_orange}\n\
Blond: {contador_blond}\n\
Green: {contador_green}\n\
Brown / White: {contador_brown_white}\n\
White: {contador_white}\n\
Auburn: {contador_auburn}\n\
Yellow: {contador_yellow}\n\
Red: {contador_red}\n\
Brown: {contador_brown}\n") 
    
    return mensaje   
#I
def listar_heroes_por_color_ojos ():
    '''Agrupa en lista a superhéroes por color de ojos'''
    
    lista_red = []
    lista_brown = []
    lista_yellow_no_irises = []
    lista_silver = []
    lista_blue = []
    lista_yellow = []
    lista_hazel = []
    lista_green = []
    
    
    for heroe in lista_personajes:
         match heroe["color_ojos"]:
            case "Red":
                   lista_red.append(heroe["nombre"])
            case "Brown":
                   lista_brown.append(heroe["nombre"])
            case "Yellow (without irises)":
                   lista_yellow_no_irises.append(heroe["nombre"])
            case "Silver":
                   lista_silver.append(heroe["nombre"])
            case "blue" | "Blue":
                   lista_blue.append(heroe["nombre"])
            case "Yellow":
                     lista_yellow.append(heroe["nombre"])
            case "Hazel":
                     lista_hazel.append(heroe["nombre"])
            case "Green":
                     lista_green.append(heroe["nombre"])
    
    mensaje = print(f"Red: {lista_red}\n\
Brown: {lista_brown}\n\
Yellow (without irises): {lista_yellow_no_irises}\n\
Silver: {lista_silver}\n\
Blue: {lista_blue}\n\
Yellow: {lista_yellow}\n\
Hazel: {lista_hazel}\n\
Green: {lista_green}\n")
    
    return mensaje   
#J
def listar_heroes_por_tipo_inteligencia ():
    '''Agrupa en lista a superhéroes por tipo de inteligencia'''
    lista_sin_inteligencia = []
    lista_good = []
    lista_average = []
    lista_high = []
    
    for heroe in lista_personajes:
         match heroe["inteligencia"]:
            case "":
                   lista_sin_inteligencia.append(heroe["nombre"])
            case "good":
                   lista_good.append(heroe["nombre"])
            case "average":
                   lista_average.append(heroe["nombre"])
            case "high":
                   lista_high.append(heroe["nombre"])
    
    mensaje = print(f"Sin inteligencia: {lista_sin_inteligencia}\n\
good: {lista_good}\n\
average: {lista_average}\n\
high: {lista_high}\n")
    
    return mensaje   

