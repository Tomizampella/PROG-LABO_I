# CLASE 1
# Ejercicio 1:
# Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su
# sueldo para esa persona.
print("Por favor ingrese su nombre: ")
nombre = input()
print("Por favor ingrese su sueldo: ")
sueldo = input()
sueldo = int(sueldo)
incremento_10 = sueldo * 0.1
sueldo_incrementado_10 = sueldo + incremento_10
print(f"Su sueldo con 10% de incremento le queda en {sueldo_incrementado_10}")
