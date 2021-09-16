# NO DEBES MODIFICAR ESTE ARCHIVO

from invitades import Invitade


def cargar_invitades(nombre_archivo):
    # Esta función retorna un dict
    with open(nombre_archivo, "rt", encoding="utf-8") as archivo:
        next(archivo)
        texto = archivo.readlines()

    diccionario_invitades = {}
    for linea in texto:
        nombre, edad, pase, temp, tos, dolor_cabeza, mail = linea.split(',')
        if pase == "true":
            pase = True
        elif pase == "false":
            pase = False
        tos = (tos == 'true')
        dolor_cabeza = (tos == 'true')
        invitade = Invitade(
            nombre, int(edad), pase, float(temp), tos, dolor_cabeza, mail
        )
        diccionario_invitades[invitade.nombre] = invitade

    return diccionario_invitades


def cargar_total_asistentes(nombre_archivo):
    # Esta función retorna un list
    with open(nombre_archivo, 'rt', encoding="utf-8") as archivo:
        nombres = archivo.readlines()

    return [nombre.strip() for nombre in nombres]
