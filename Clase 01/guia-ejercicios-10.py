# Ejercicio 10:
# Pedir al usuario que ingrese los datos de 5 alumnos y guardarlos en sus
# respectivas listas. Validar el ingreso de datos según su criterio.
# Datos:
# nombre, sexo (f/m), nota (validar).
# Una vez cargados los datos:
# Mostrar el nombre del hombre con nota más baja
# Mostrar el promedio de notas de las mujeres
# Ejemplo:
lista_nombres = ["Juan","Pedro","Sol","Paco","Ana"]
lista_sexo = ["m","m","f","m","f"]
lista_notas = [6,8,10,8,5]
nota_mas_baja = None
nombre_mas_baja = None
contador_mujeres = 0
acumulador_nota_mujeres = 0

if len(lista_nombres) != 5:
    for _ in range(5):
        nombre = input("ingrese su nombre: ")
        
        while nombre.isdigit():
            nombre = input("ingrese su nombre correctamente: ")
        
        lista_nombres.append(nombre)

        sexo = input("ingrese su sexo: ")
        
        while sexo != "f" and sexo != "m":
            sexo = input("ingrese su sexo correctamente: ")
        
        lista_sexo.append(sexo)

        nota = input("ingrese su nota: ")
        
        while nota.isalpha():
            nota = input("ingrese su nota correctamente: ")

        nota = int(nota)
        lista_notas.append(nota)

else:
    for indice in range(5):
        
        match (lista_sexo[indice]):
            case "m":
                if nota_mas_baja == None or nota_mas_baja > lista_notas[indice]: 
                    nota_mas_baja = lista_notas[indice]
                    nombre_mas_baja = lista_nombres[indice]
            
            case "f":
                contador_mujeres = contador_mujeres + 1
                acumulador_nota_mujeres = acumulador_nota_mujeres + lista_notas[indice]
            
    
    promedio_nota_mujeres = acumulador_nota_mujeres / contador_mujeres
   
    print (f"El nombre del hombre con nota más baja es {nombre_mas_baja}")
    print (f"El promedio de notas de las mujeres es {promedio_nota_mujeres}" )