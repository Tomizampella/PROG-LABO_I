# La división de higiene está trabajando en un control de stock para productos
# sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de
# contagio, de cada una debe obtener los siguientes datos:
# 1. El tipo (validar "barbijo", "jabón" o "alcohol")
# 2. El precio: (validar entre 100 y 300)
# 3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las
# 1000 unidades)
# 4. La marca y el Fabricante.
# Se debe informar lo siguiente:
# A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
# B. Del ítem con más unidades, el fabricante.
# C. Cuántas unidades de jabones hay en total.
lista_tipo = ["barbijo", "jabon", "barbijo", "jabon", "alcohol"]
lista_precio = [10,20,55,35,77]
lista_unidades = [8,9,78,2,11]
lista_marca = ["zara", "adidas", "nike", "puma", "lacoste"]
precio_barbijo_mas_caro = None
unidades_barbijo_mas_caro = None
marca_barbijo_mas_caro = None
item_mas_unidades = None
marca_item_mas_unidades = None
acumulador_jabones = 0
if len(lista_tipo) != 5:
    for _ in range(5):
        tipo = input("ingrese el tipo de producto de prevención: ")
        
        while tipo != "barbijo" and tipo != "jabon" and tipo != "alcohol":
            tipo = input("ingrese el tipo de producto de prevención correctamente: ")
        
        lista_tipo.append(tipo)

        precio = input("ingrese su precio: ")
        
        while precio.isalpha() or int(precio) < 100 or int(precio) > 300:
            precio = input("ingrese su precio correctamente: ")

        precio = int(precio)
        lista_precio.append(precio)

        unidades = input("ingrese la cantidad de  unidades: ")
        
        while unidades.isalpha() or int(unidades) < 0 or int(unidades) > 1000:
            unidades = input("ingrese la cantidad de unidades correctamente: ")

        unidades = int(unidades)
        lista_unidades.append(unidades)

        marca = input("ingrese la marca del producto de prevención: ")
        
        lista_marca.append(marca)

if len(lista_tipo) == 5:
    for indice in range(5):
        match lista_tipo[indice]:
            case "barbijo":
                if precio_barbijo_mas_caro == None or precio_barbijo_mas_caro < lista_precio[indice]:  #a
                    precio_barbijo_mas_caro = lista_precio[indice]
                    unidades_barbijo_mas_caro = lista_unidades[indice]
                    marca_barbijo_mas_caro = lista_marca[indice]
            case  "jabon":
                  acumulador_jabones = acumulador_jabones + lista_unidades[indice] #c
        
        if item_mas_unidades == None or item_mas_unidades < lista_unidades[indice]: #b
                    item_mas_unidades = lista_unidades[indice]
                    marca_item_mas_unidades = lista_marca[indice]
                    
# A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
# B. Del ítem con más unidades, el fabricante.
# C. Cuántas unidades de jabones hay en total.
print (f"Hay {unidades_barbijo_mas_caro} unidades del más caro de los barbijos y su fabricante es {marca_barbijo_mas_caro}")#A
print (f"Del ítem con más unidades, el fabricante es {marca_item_mas_unidades}")#B
print (f"Hay {acumulador_jabones} unidades de jabones hay en total")#C
