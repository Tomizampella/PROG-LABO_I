# Ejercicio 5:
# Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
# por cada estadía como base, se pide el ingreso de una estación del
# año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
# Plata/Córdoba) para vacacionar para poder calcular el precio final:
# -en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene undescuento del 10% Mar del Plata tiene un descuento del 20%
# -en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene un aumento del 10% Mar del Plata tiene un aumento del 20%
# -en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene elprecio sin descuento.
# Validar el ingreso de datos

estadia_base = 15000

estacion_ingresada = input("ingrese la estación del año: ") 
while estacion_ingresada != "Invierno" and estacion_ingresada != "Verano" and estacion_ingresada != "Otoño" and estacion_ingresada != "Primavera":
    estacion_ingresada = input("ingrese la estación del año correctamente: ")

localidad_ingresada = input("ingrese la localidad: ") 
while localidad_ingresada != "Bariloche" and localidad_ingresada != "Cataratas" and localidad_ingresada != "Mar del Plata" and localidad_ingresada != "Cordoba":
    localidad_ingresada = input("ingrese la localidad correctamente: ")

match (estacion_ingresada):
            case ("Invierno"):
                match (localidad_ingresada):
                    case ("Bariloche"):
                        operacion = 1.2
                    case ("Cataratas" | "Cordoba"):
                        operacion =  0.9
                    case ("Mar del Plata"):
                        operacion = 0.8
            case("Verano"):
                match (localidad_ingresada):
                    case ("Bariloche"):
                        operacion = 0.8
                    case ("Cataratas" | "Cordoba"):
                        operacion =  1.1
                    case ("Mar del Plata"):
                        operacion = 1.2
            case("Otoño" | "Primavera"):
                match (localidad_ingresada):
                    case ("Bariloche" | "Cataratas"| "Mar del Plata"):
                        operacion = 1.1
                    case _:
                          operacion = 1
                        
tarifa_final = estadia_base * operacion
print(f"Usted va a viajar a {localidad_ingresada} en {estacion_ingresada} con un costo final de ${tarifa_final}")

