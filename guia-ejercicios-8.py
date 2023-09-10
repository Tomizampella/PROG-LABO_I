# Ejercicio 8:
# Dada la siguiente lista:
# [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
# mostrar el número repetido
lista_numero = [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
contador = 0
numero_repetido = None
for numero in lista_numero:
        contador = 0
        for dato in lista_numero:
            if numero == dato :
                contador = contador + 1 
                if contador == 2:
                    numero_repetido = numero
                    break
        


print(f"El numero repetido es {numero_repetido}")