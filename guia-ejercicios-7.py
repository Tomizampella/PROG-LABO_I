# Ejercicio 7:
# Dada la siguiente lista:
# [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
# mostrar solo los números pares.
lista_numero = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
lista_pares = []
for indice in range(len(lista_numero)):
    if (lista_numero[indice] % 2) == 0:
        lista_pares.append(lista_numero[indice])

print (f"De esta lista de numeros {lista_numero}, los números pares son: {lista_pares}")
                