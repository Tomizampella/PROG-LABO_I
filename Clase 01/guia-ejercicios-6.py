# CLASE 2
# Ejercicio 6:
# Utilizar For
# Dada la siguiente lista:
# [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
# mostrar el mayor.
lista_numero = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
numero_mayor = None
for indice in range(len(lista_numero)):
    if numero_mayor == None or numero_mayor < lista_numero[indice]:
                numero_mayor = lista_numero[indice]

print (f"De esta lista de numeros {lista_numero}, el mayor es {numero_mayor}")
                