from data_stark import lista_personajes
from stark_biblioteca import *

print(stark_normalizar_datos(lista_personajes))

heroes_por_tipo_inteligencia = {}

for heroe in lista_personajes:
        tipo_inteligencia = heroe["inteligencia"]

        if tipo_inteligencia not in heroes_por_tipo_inteligencia:
            heroes_por_tipo_inteligencia[tipo_inteligencia] = []

        heroes_por_tipo_inteligencia[tipo_inteligencia].append(heroe["nombre"])

for inteligencia in heroes_por_tipo_inteligencia:
      heroes = heroes_por_tipo_inteligencia[inteligencia]
      mensaje = print(f"Tipo inteligencia {inteligencia} : {heroes}")
        # for heroes in inteligencia:
        #     mensaje = print(f"Tipo inteligencia {inteligencia} : {heroes}")


print (mensaje)

'''
for clave in mi_diccionario:
    valor = mi_diccionario[clave]
    print(f'Clave: {clave}, Valor: {valor}')'''