from pokemon import (obtener_info_habilidad, obtener_pokemones,
                     obtener_pokemon_mas_alto, obtener_pokemon_mas_rapido,
                     obtener_mejores_atacantes, obtener_pokemones_por_tipo)
from api_curso import info_api_curso


token = ""  # Ingresar tu API Token personal aquí

info_curso = info_api_curso(token)

if not info_curso:
    print("No se pudo obtener la información de la API del curso")
    exit()

url = info_curso["ability"]["url"]
info_habilidad = obtener_info_habilidad(url)
pokemones = obtener_pokemones(info_habilidad["pokemon"])

mas_alto = obtener_pokemon_mas_alto(pokemones)
mas_rapido = obtener_pokemon_mas_rapido(pokemones)
mejores_atacantes = obtener_mejores_atacantes(pokemones)
pokemones_por_tipo = obtener_pokemones_por_tipo(pokemones)

print("Mas alto", mas_alto)
print("Mas rapido", mas_rapido)
print("Mejores atacantes", mejores_atacantes)
print("Pokemones por tipo", pokemones_por_tipo)
