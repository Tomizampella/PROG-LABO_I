# Ejercicio 9:
# Dadas las siguientes listas:
# edades = [25,36,18,23,45]
# nombre = ["Juan","Ana","Sol","Mario","Sonia"]
# y considerando que la posición en la lista corresponde a la misma persona,
# mostar el nombre de la persona más joven
edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]
edad_mas_joven = None
nombre_mas_joven = None
for indice in range(len(nombre)):
    if edad_mas_joven == None or edad_mas_joven > edades[indice]: #B
            edad_mas_joven = edades[indice]
            nombre_mas_joven = nombre[indice]

print (f"De esta lista de numeros {nombre}, el más joven es {nombre_mas_joven}")
                