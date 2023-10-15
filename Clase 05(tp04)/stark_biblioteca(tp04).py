from data_stark import lista_personajes
import re
#TP Stark 04 - Tomas Lautaro Diaz Zampella

#1.1
def extraer_iniciales(nombre_heroe: str) -> str:
    ''' Recibe nombre héroe y retorna solo las iniciales seguidas de un punto'''
    if nombre_heroe != "":
        if "-" in nombre_heroe:
            nombre_heroe = re.sub("-","",nombre_heroe)
        nombre_heroe = re.findall("[A-Z]",nombre_heroe)
        nombre_iniciales = "."
        nombre_iniciales = nombre_iniciales.join(nombre_heroe)
        
        return f"{nombre_iniciales}."
    else:
        return print("N/A")
            


#1.2. 
def definir_iniciales_nombre(heroe: dict) -> bool:
    '''Recibe diccionario, le agrega clave "iniciales" con el valor obtenido de la función extraer_iniciales'''
    if type(heroe) == dict and "nombre" in heroe:
        clave, valor = "iniciales",extraer_iniciales(heroe["nombre"])
        heroe[clave] = valor
        return True
    else:
        return False

#1.3.
def agregar_iniciales_nombre(lista_heroes: list)-> bool:
    '''Recibe lista, se itera y se traspasa diccionario a la función definir_iniciales_nombre'''
    if type(lista_heroes) == list and len(lista_heroes) > 0:
        for heroe in lista_heroes:
            traspaso_diccionario = definir_iniciales_nombre(heroe)
            if traspaso_diccionario == False:
                print("El origen de datos no contiene el formato correcto")
                return False
        
    return True

#1.3.(2)

def stark_imprimir_nombres_con_iniciales(lista_heroes: list):
    agregar_iniciales_nombre(lista_heroes)
    if type(lista_heroes) == list and len(lista_heroes) > 0:
        for heroe in lista_heroes:
            print(f"* {heroe['nombre']} ({heroe['iniciales']})")


#2.1.
def generar_codigo_heroe (id_heroe: int, genero_heroe: str) -> str:
    '''Recibe id heroe como entero y genero heroe como str y retorna str en formato:
    "(genero_heroe)-completa con ceros hasta que el formato llegue a 10 caracteres(id_heroe)'''
    if type(id_heroe) == int and genero_heroe in ["M", "F", "NB"]:
        longitud_cadena = len(f"{genero_heroe}-") 
        candidad_de_ceros = 10 - longitud_cadena
        id_heroe = str(id_heroe)
        codigo_heroe = f"{genero_heroe}-{id_heroe.zfill(candidad_de_ceros)}"
        return codigo_heroe
    else:
        return "N/A"
    

#2.2.
def agregar_codigo_heroe(heroe: dict, id_heroe: int) -> bool:
    '''Recibe diccionario, le agrega clave "iniciales" con el valor obtenido de la función extraer_iniciales'''
    if len(heroe)> 0:
        clave, valor = "codigo_heroe",generar_codigo_heroe(id_heroe,heroe["genero"])
        if len(valor) == 10:
            heroe[clave] = valor
            return True
    else:
        return False
    

#2.3. 
def stark_generar_codigos_heroes(lista_heroes: list):
    '''Recibe lista, se itera y le agrega el código a cada uno de los personajes'''
    
    if len(lista_heroes) > 0:
        for heroe in lista_heroes:
            if  type(heroe) == dict and "genero" in heroe:
                id_heroe = lista_heroes.index(heroe) + 1
                agregar_codigo_heroe(heroe, id_heroe)
        
        print(f"\nSe asignaron {len(lista_personajes)} códigos\n"
              f"El código del primer héroe es: {lista_heroes[0]['codigo_heroe']}\n"
              f"El código del último héroe es: {lista_heroes[-1]['codigo_heroe']}")
    else:
        print("El origen de datos no contiene el formato correcto")


#3.1. 
def sanitizar_entero(numero_str: str)-> int:
    ''' Recibe str, retorna -1 si no tiene caracteres numéricos, -2 si es un numero negativo, -3 si no se puede convertir a entero
    ó retorna el numero casteado a entero si es un numero entero positivo'''
    numero_str = numero_str.strip()
    if re.match(r"^[-+]?[0-9]+$", numero_str):
        if re.match(r"^[+]?[0-9]+$", numero_str):
            numero_int = int(numero_str)
            return numero_int
        else:
            return -2
    elif re.match(r"[^0-9]", numero_str): 
            return -1
    else:
            return -3

#3.2.   
def sanitizar_flotante(numero_str: str):
    ''' Recibe str, retorna -1 si no tiene caracteres numéricos, -2 si es un numero negativo, -3 si no se puede convertir a entero
    ó retorna el numero casteado a entero si es un numero decimal positivo'''
    numero_str = numero_str.strip()
    if re.match(r"^[-+]?[0-9]+\.[0-9]+$", numero_str):
        if re.match(r"^[+]?[0-9]+\.[0-9]+$", numero_str):
            numero_float = float(numero_str)
            return numero_float
        else:
            return -2
    elif re.match(r"[^0-9]", numero_str): 
            return -1
    else:
            return -3
    
#3.3.
def sanitizar_string(valor_str: str, valor_por_defecto = "-")-> str:
    ''' Recibe valor_str y tiene un valor por defecto, retorna "N/A" si valor_str contiene numeros, sino retorna el valor_str todo 
    en minuscula. Si el valor_str está vacio, retorna valor valor_por_defecto en minuscula'''
    valor_str = valor_str.strip()
    valor_por_defecto = valor_por_defecto.strip()
    if re.match(r"\d", valor_str):
        return "N/A"
    elif not valor_str and valor_por_defecto:
        return valor_por_defecto.lower()
    else:
        valor_str = valor_str.replace("/", " ")
        valor_str = valor_str.lower()
        return valor_str

#3.4. 
def sanitizar_dato(heroe: dict, clave: str, tipo_dato: str)-> bool:
    ''' Recibe diccionario, clave y tipo de dato, Castea el valor asociado a la clave al tipo de dato solicitado.
    si tipo de dato no coincide retorna False, si no está la clave dentro del diccionario retorna False. '''
    tipo_dato = tipo_dato.lower()
    if tipo_dato not in ["string", "entero", "flotante"]:
        print("Tipo de dato no reconocido")
        return False

    if clave not in heroe:
        print("La clave especificada no existe en el héroe")
        return False

    valor = heroe[clave]
    if tipo_dato == "string":
        heroe[clave] = sanitizar_string(valor)
    elif tipo_dato == "entero":
        heroe[clave] = sanitizar_entero(valor)
    elif tipo_dato == "flotante":
        heroe[clave] = sanitizar_flotante(valor)

    return True

#3.5.
def stark_normalizar_datos(lista_heroes: list):
    '''Recibe lista, la cual se itera y se sanitiza los valores de las siguientes claves:
    'altura', 'peso', 'color_ojos', 'color_pelo', 'fuerza' e'inteligencia'''
    if len(lista_heroes) > 0:
        for heroe in lista_heroes:
            sanitizar_dato(heroe,"altura","flotante")
            sanitizar_dato(heroe,"peso","flotante")
            sanitizar_dato(heroe,"color_ojos","string")
            sanitizar_dato(heroe,"color_pelo","string")
            sanitizar_dato(heroe,"fuerza","entero")
            sanitizar_dato(heroe,"inteligencia","string")
        print("\nDatos normalizados")
    else:
        print("Error: Lista de héroes vacía")

#4.1.
def generar_indice_nombre(lista_heroes: list)-> list | str:
    ''' Recibe lista de heroes y retorna lista donde cada elemento es cada palabra que componen el nombre de los personajes'''
    if len(lista_heroes) > 0:
        lista_elementos_nombre = []
        for heroe in lista_personajes:
            if type(heroe) == dict and "nombre" in heroe:
                palabras = re.findall('[a-zA-Z]+', heroe['nombre'])
                lista_elementos_nombre.extend(palabras)
        return lista_elementos_nombre
    else:
        return print("El origen de datos no contiene el formato correcto")

#4.2.
def stark_imprimir_indice_nombre(lista_heroes: list):
    '''Recibe lista y muestra cada palabra que compone el nombre separado por un guión'''
    indice_nombre = generar_indice_nombre(lista_heroes)
    cadena = "-"
    cadena = cadena.join(indice_nombre)
    return print(cadena)


#5.1.
def convertir_cm_a_mtrs(valor_cm):
    '''Recibe flotante en centimetros y retorna flotante en la unidad metros'''
    if type(valor_cm) == float and valor_cm > 0:
        traspaso_cm_a_mtrs = valor_cm / 100
        return traspaso_cm_a_mtrs
    else:
        return -1

#5.2.
def generar_separador(patron: str, largo: int, imprimir = True)-> str:
    ''' Recibe string y su largo, retorna un patron de esas caracteristicas. 
    Imprime por defecto, no lo hace si el tercer paramatro es False'''
    if len(patron) in range(1,3) and largo in range(1,236):
        separador = patron * largo
        if imprimir == True:
            print(separador)
        return separador
    else:
        return "N/A"

#5.3.
def generar_encabezado(titulo: str)-> str:
    '''Recibe titulo, convierte todas las letras en mayúsculas y devuelve titulo entre dos separadores'''
    titulo = titulo.upper()
    separador = generar_separador("*",100,False)
    
    return (f"{separador}\n{titulo}\n{separador}")

#5.4.
def imprimir_ficha_heroe(heroe: dict)-> str:
    '''Recibe heroe como diccionario e imprime sus datos en formato ficha'''
    altura = heroe['altura']
    altura = convertir_cm_a_mtrs(altura)
    
    print(f"{generar_encabezado('PRINCIPAL')}\n"
          f"    NOMBRE DEL HÉROE:             {heroe['nombre']} {heroe['iniciales']}\n"
          f"    IDENTIDAD SECRETA:            {heroe['identidad']}\n"
          f"    CONSULTORA:                   {heroe['empresa']}\n"
          f"    CÓDIGO DE HÉROE :             {heroe['codigo_heroe']}\n"
          f"{generar_encabezado('FISICO')}\n"
          f"    ALTURA :                      {altura:.2f} Mtrs.\n"
          f"    PESO :                        {heroe['peso']:.2f} Kg.\n"
          f"    FUERZA :                      {heroe['fuerza']} N\n"
          f"{generar_encabezado('SEÑAS PARTICULARES')}\n"
          f"    COLOR DE OJOS:                {heroe['color_ojos']}\n"
          f"    COLOR DE PELO:                {heroe['color_pelo']}")
    
#5.5.
def stark_navegar_fichas(lista_heroes: list):
    '''Recibe lista_heroes y permite navegar por las fichas de los heroes con las instrucciones:
     "1" para ir a la izquierda, "2" para ir a la derecha y "s" para salir '''
    indice_actual = 0
    cantidad_heroes = len(lista_heroes)
    while (True):
    
        heroe_actual = lista_heroes[indice_actual]
        imprimir_ficha_heroe(heroe_actual)

        print("\n[ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir\n")
        opcion_elegida = input("Seleccione una opción: ").strip().upper()

        if opcion_elegida == "1":
            indice_actual = indice_actual - 1
            if indice_actual < 0:
                indice_actual = cantidad_heroes - 1  
        elif opcion_elegida == "2":
            indice_actual = indice_actual + 1
            if indice_actual == cantidad_heroes:
                indice_actual = 0  
        elif opcion_elegida == "S":
            break


#6.1.
def imprimir_menu():
    '''Imprime menú'''
    print(f"\n1 - Imprimir la lista de nombres junto con sus iniciales\n"
          f"2 - Generar códigos de héroes\n"
          f"3 - Normalizar datos\n"
          f"4 - Imprimir índice de nombres\n"
          f"5 - Navegar fichas\n"
          f"S - Salir\n")


    generar_separador("_",100)  

#6.2.
def stark_menu_principal()-> str:
    '''No recibe parametros, imprime menú y pide al usuario que seleccione una opción'''
    imprimir_menu()
    opcion_elegida = input("Seleccione una opción: ").strip().upper()
    return opcion_elegida

#6.3.
def stark_marvel_app_3(lista_heroes: list):
    '''Recibe lista de heroes como parámetro y se encarga de ejecutar el programa'''
    while(True):
        opcion_elegida = stark_menu_principal()
        match(opcion_elegida) :    
                    case "1":
                        stark_imprimir_nombres_con_iniciales(lista_heroes)
                    case "2":
                        stark_generar_codigos_heroes(lista_heroes)
                    case "3":
                        stark_normalizar_datos(lista_heroes)
                    case "4":
                        stark_imprimir_indice_nombre(lista_heroes)
                    case "5":
                        stark_navegar_fichas(lista_heroes)
                    case "S":
                        break
                    case _:
                        print("opción incorrecta\n")
