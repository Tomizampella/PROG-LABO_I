from data_stark import lista_personajes

#0
flag_se_llamo_anteriormente = False
def stark_normalizar_datos(lista_personajes: list) -> bool:
    '''Recibe lista_personajes, castea a float o int las valores numericos y retorna True o False'''
    global flag_se_llamo_anteriormente
    if flag_se_llamo_anteriormente == True or (len(lista_personajes)) < 1:
        return False
    

    flag_dato_modificado = False
    
    for heroe in lista_personajes: 
        for clave, valor in heroe.items(): 
            valor_sin_decimal = valor.replace (".", "") 
            
            if valor_sin_decimal.isdigit() == True:
                if "." in valor:
                    if type(valor) != float:
                        heroe[clave] = float(valor)
                         
                        if flag_dato_modificado == False:
                            flag_dato_modificado = True
                else:
                    if type(valor) != int:
                        heroe[clave] = int(valor) 
                        
                        if flag_dato_modificado == False:
                            flag_dato_modificado = True
    
    flag_se_llamo_anteriormente = True
    if flag_dato_modificado == True:
        
        return True 
    

#1.1

def obtener_dato(heroe: dict, clave: str) -> str:
    '''Recibe diccionario y clave. Retornar valor de la clave'''
    for indice in lista_personajes:
        if "nombre" in indice and (len(lista_personajes)) > 0 :
            if indice["nombre"] == heroe :
                mensaje =  print(f"{clave} : {indice[clave]}")
        else:
            mensaje = print (False)
            
    return mensaje

#1.2

def obtener_nombre(heroe: dict) -> str:
    '''Recibe diccionario como heroe y retorna nombre del heroe en formato: Nombre: (nombre informado)'''
    clave = "nombre"
    for indice in lista_personajes:
        if "nombre" in indice and (len(lista_personajes)) > 0 :
            if indice["nombre"] == heroe :
                mensaje =  print(f"{clave} : {indice[clave]}")
        else:
            mensaje = print (False)
            
    return mensaje

#2

def obtener_nombre_y_dato(heroe: dict, clave: str) -> str:
    '''Recibe diccionario como heroe y dato como clave y retorna en formato: Nombre: (nombre informado) | dato: (valor dato) '''
    clave_nombre = "nombre"
    for indice in lista_personajes:
        if clave_nombre in indice and (len(lista_personajes)) > 0 :
            if indice[clave_nombre] == heroe :
                mensaje =  print(f"{clave_nombre}: {indice[clave_nombre]} | {clave}: {indice[clave]}")
                
                
                           
        else:
            mensaje = print (False)
            
    return mensaje

#3.1
def obtener_maximo(lista: list, clave: str):
    ''' Recibe lista y clave. Retorna de ese clave el valor maximo'''
    maximo = None
    for heroe in lista:
        if type(heroe[clave]) == int or type(heroe[clave]) == float and (len(lista)) > 0 :
            if maximo == None or heroe[clave] > maximo:
                maximo = heroe[clave]
            mensaje = (f"El maximo de {clave} es {maximo}")        
            
        else:
            mensaje = (False)
        
    return print(mensaje)

#3.2
def obtener_minimo(lista: list, clave: str):
    ''' Recibe lista y clave. Retorna de ese clave el valor minimo'''
    minimo = None
    for heroe in lista:
        if type(heroe[clave]) == int or type(heroe[clave]) == float and (len(lista)) > 0 :
            if minimo == None or heroe[clave] < minimo:
                minimo = heroe[clave]
            mensaje = (f"El minimo de {clave} es {minimo}")        
            
        else:
            mensaje = (False)
        
    return print(mensaje)

#3.3
def obtener_dato_cantidad(lista: list ,valor: int | float ,clave: str) -> list:
    ''' Recibe lista, valor y clave. Retorna lista de los heroes que cumplen con el valor y clave solicitadas'''
    lista_heroes_cumplen_condicion = []
    for heroe in lista:
        if type(heroe[clave]) == int or type(heroe[clave]) == float and (len(lista)) > 0 :
            if heroe[clave] == valor:
                lista_heroes_cumplen_condicion.append(heroe["nombre"])
            mensaje = (f"Los héroes que tienen {valor} de {clave} son: {lista_heroes_cumplen_condicion}")        
            
        else:
            mensaje = (False)
        
    return print(mensaje)

#3.4
def stark_imprimir_heroes(lista: list) -> list:
    ''' Recibe lista y la imprime si no se encuentra vacia'''
    if (len(lista)) > 0 :
        mensaje = lista
    else:
        mensaje = (False)
    
    return print(mensaje)

#4.1
def sumar_dato_heroe (lista: list, clave: str) -> str:
    ''' Recibe lista y clave. Retorna la suma de todos los valores de la clave solicitada'''
    suma = 0
    for heroe in lista:
        if type(heroe) == dict and (len(heroe)) > 0 :
            suma = heroe[clave] + suma
                
            
        else:
            return False

    return suma

#4.2
def dividir(dividendo: int | float, divisor: int | float ):
    ''' Redibe dividendo y divisor. Retornar resultado de la division entre dividendo y divisor'''
    if divisor > 0:
        division = dividendo / divisor
        return division
    
    else:
        return False


#4.3
def calcular_promedio (lista: list, clave: str) -> float:
    ''' recibe lista y clave. Retorna el promedio del dato solicitado'''
    total = sumar_dato_heroe(lista, clave)
    cantidad_heroes = len(lista)
    promedio = dividir(total,cantidad_heroes)
    
        
    return promedio

#4.4
def mostrar_promedio_dato(lista:list, clave:str)-> float:
    ''' Recibe lista y clave, valida si el valor de la clave es de tipo int o float y muestra promedio'''
    suma = 0
    for heroe in lista:
        if type(heroe[clave]) == int or type(heroe[clave]) == float and (len(lista)) > 0 :
            
            mostrar_promedio = calcular_promedio(lista, clave)
                
            
        else:
            return False

    return mostrar_promedio


#5.1
def imprimir_menu():
    '''Imprime menú'''
    print("Menú:")
    print("1. Normalizar datos (Seleccione 1 para poder acceder al menú )")
    print("2. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB")
    print("3. Recorrer la lista y determinar cuál es el superhéroe más alto de género F")
    print("4. Recorrer la lista y determinar cuál es el superhéroe más alto de género M")
    print("5. Recorrer la lista y determinar cuál es el superhéroe más débil de género M")
    print("6. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB")
    print("7. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB")
    print("8. Determinar cuántos superhéroes tienen cada tipo de color de ojos.")
    print("9. Determinar cuántos superhéroes tienen cada tipo de color de pelo.")
    print("10. Listar todos los superhéroes agrupados por color de ojos.")
    print("11. Listar todos los superhéroes agrupados por tipo de inteligencia")
    print("12. Salir\n")
            

#5.2
def validar_entero(string_numero: str)-> bool:
    '''Recibe string de numero, valida si es un string conformado únicamente por dígitos. Retorna True si cumple condición, caso contrario, false '''
    if type(string_numero) == str and string_numero.isdigit():
        return True
    else:
        return False

#5.3
def stark_menu_principal():
    '''Imprime menú, pide al usuario que ingrese número. Si es correcto retorna el numero casteado a "int", caso contrario False'''
    imprimir_menu()
    opcion_elegida = input("Seleccione un numero: ")
    validacion = validar_entero(opcion_elegida)
    if validacion == True:
        opcion_elegida_int = int(opcion_elegida)
        return opcion_elegida_int
    else:
        return False
    
#6
def stark_marvel_app(lista_personajes):
    '''Recibe la lista de héroes y se encargará de la ejecución principal de nuestro programa'''
    flag_datos_normalizados = False
    while(True):
        opcion_elegida = stark_menu_principal()
        
        if opcion_elegida != False and opcion_elegida >= 1 and opcion_elegida <= 12:
            if opcion_elegida == 1:
                    estado_normalizacion = stark_normalizar_datos(lista_personajes)
                    if estado_normalizacion == True:
                        print("Datos Normalizados\n")
                        flag_datos_normalizados = True
                    else: 
                        print("Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente")
                        flag_datos_normalizados = False
                        break
            if flag_datos_normalizados == True:
                match(opcion_elegida) :    
                    case 2:
                        muestra_nombres_heroe_genero_nb ()
                    case 3:
                        calcular_heroe_mas_alto_femenino ()
                    case 4:
                        calcular_heroe_mas_alto_masculino ()
                    case 5:
                        calcular_heroe_mas_debil_masculino ()
                    case 6:
                        calcular_heroe_mas_debil_no_binario ()
                    case 7:
                        calcular_fuerza_promedio_genero_nb ()
                    case 8:
                        calcular_heroes_por_color_ojos ()
                    case 9:
                        calcular_heroes_por_color_pelo ()
                    case 10:
                        listar_heroes_por_color_ojos ()
                    case 11:
                        listar_heroes_por_tipo_inteligencia ()
                    case 12:
                        break
        else:
            print("Opción incorrecta, ingrese un numero del 1 al 12")              


#7

#B-2
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
#C-3
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
#D-4
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
#E-5
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
#F-6
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
#G-7
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
       mensaje = print (f"La fuerza promedio de los superhéroes de genero no binario es {promedio_fuerza_nb :.0f} kg\n")   
    else:
       mensaje = print("No hay superhéroes de género NB")
    
    return mensaje   
#H-8
def calcular_heroes_por_color_ojos ():
    '''Calcula la cantidad de superhéroes por color de ojos'''
    contador_colores_ojos = {}

    for heroe in lista_personajes:
        color_ojos = heroe["color_ojos"]
    
        if color_ojos in contador_colores_ojos:
            contador_colores_ojos[color_ojos] = contador_colores_ojos[color_ojos] + 1
        
        else:
            contador_colores_ojos[color_ojos] = 1
        
    for color, cantidad in contador_colores_ojos.items():
        mensaje = print(f"Color de ojos: {color}, Cantidad: {cantidad}")
    
    return mensaje
        
#I-9
def calcular_heroes_por_color_pelo ():
    '''Calcula la cantidad de superhéroes por color de pelo'''
    
    contador_colores_pelo = {}

    for heroe in lista_personajes:
        color_pelo = heroe["color_pelo"]
    
        if color_pelo in contador_colores_pelo:
            contador_colores_pelo[color_pelo] = contador_colores_pelo[color_pelo] + 1
        
        else:
            contador_colores_pelo[color_pelo] = 1
        
    for color, cantidad in contador_colores_pelo.items():
        mensaje = print(f"Color de pelo: {color}, Cantidad: {cantidad}")
    
    return mensaje

#J-10
def listar_heroes_por_color_ojos ():
    '''Agrupa en lista a superhéroes por color de ojos'''

    heroes_por_color_ojos = {}

    for heroe in lista_personajes:
        color_ojos = heroe["color_ojos"]
        
        if color_ojos not in heroes_por_color_ojos:
            heroes_por_color_ojos[color_ojos] = []
        

        heroes_por_color_ojos[color_ojos].append(heroe["nombre"])

    for color, heroes in heroes_por_color_ojos.items():
        mensaje = print(f"Color de ojos {color} : {heroes}")
        
    return mensaje

#K-11
def listar_heroes_por_tipo_inteligencia ():
    '''Agrupa en lista a superhéroes por tipo de inteligencia'''
    
    heroes_por_tipo_inteligencia = {}

    for heroe in lista_personajes:
        tipo_inteligencia = heroe["inteligencia"]

        if tipo_inteligencia not in heroes_por_tipo_inteligencia:
            heroes_por_tipo_inteligencia[tipo_inteligencia] = []

        heroes_por_tipo_inteligencia[tipo_inteligencia].append(heroe["nombre"])

    for inteligencia, heroes in heroes_por_tipo_inteligencia.items():
        mensaje = print(f"Tipo inteligencia {inteligencia} : {heroes}")
        
    return mensaje



            



            




