# Ejercicio 2:
# Pedir una edad. Informar si la persona es mayor de edad (más de 18 años),
# adolescente (entre 13 y 17 años) o niño (menor a 13 años).
print("Por favor ingrese su edad: ")
edad = input()
edad = int(edad)
if edad >= 18:
    grupo_etario = "mayor"
elif edad > 13 and edad < 17:
    grupo_etario = "adolescente"
else:
    grupo_etario = "niño"

print(f"Usted es {grupo_etario}")

