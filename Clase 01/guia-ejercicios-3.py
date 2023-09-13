# Ejercicio 3:
# Ingresar 5 números enteros, distintos de cero.
# Informar:
# a. Cantidad de pares e impares.
# b. El menor número ingresado.
# c. De los pares el mayor número ingresado.
# d. Suma de los positivos.
# e. Producto de los negativos.
lista_numeros_ingresados = []
lista_numeros_pares = []
lista_numeros_impares = []
acumulador_positivos = 0
acumulador_negativos = 0
numero_menor = None
numero_mayor_pares = None
for _ in range(5):

    numero_ingresado = input("ingrese un numero: ")
    
    while numero_ingresado.isalpha():
        numero_ingresado = input("ingrese un numero correctamente: ")

    numero_ingresado = int(numero_ingresado)
    lista_numeros_ingresados.append(numero_ingresado)

if len(lista_numeros_ingresados) == 5:
    for indice in range(len(lista_numeros_ingresados)):
        
        if (lista_numeros_ingresados[indice] % 2) == 0:#A
            lista_numeros_pares.append(lista_numeros_ingresados[indice])
            if numero_mayor_pares == None or numero_mayor_pares < lista_numeros_ingresados[indice]: #C
                numero_mayor_pares = lista_numeros_ingresados[indice]
        else:
            lista_numeros_impares.append(lista_numeros_ingresados[indice])
        

        
        if numero_menor == None or numero_menor > lista_numeros_ingresados[indice]: #B
            numero_menor = lista_numeros_ingresados[indice]

        if lista_numeros_ingresados[indice] > 0:
            acumulador_positivos = acumulador_positivos + lista_numeros_ingresados[indice]#D
        
        if lista_numeros_ingresados[indice] < 0:
            acumulador_negativos = acumulador_negativos + lista_numeros_ingresados[indice]#E
        
print(f"La Cantidad de numeros pares es {lista_numeros_pares} y la cantidad de numeros impares es {lista_numeros_impares}") #A 
print(f"El menor número ingresado es {numero_menor}") #B  
print(f"De los pares el mayor número ingresado es {numero_mayor_pares}") #C  
print(f"La suma de los positivos es {acumulador_positivos}") #D  
print(f"El producto de los negativos es {acumulador_negativos}") #E