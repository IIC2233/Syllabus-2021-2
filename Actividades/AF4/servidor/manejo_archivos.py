import os
from os.path import join, isfile
from parametros import (
    RUTA_DATOS, RAIZ_ARCHIVOS, CAPACIDAD_MAXIMA,
    FORMATOS, IGNORADOS,
)


def iniciar_sistema():
    # Vemos que exista la ruta raiz
    os.makedirs(RAIZ_ARCHIVOS, exist_ok=True)
    for ruta in RUTA_DATOS.values():
        os.makedirs(ruta, exist_ok=True)


def leer_unidad():
    """
    Lee la información en la carpeta data y devuelve un
    diccionario con los archivos
    """
    data = {}
    for seccion, ruta in RUTA_DATOS.items():
        dir_ = listdir_filtrado(ruta)
        data[seccion] = dir_
    return data


def leer_archivo(ruta):
    """
    Lee y devuelve los bytes del archivo en la ruta
    """
    with open(ruta, 'rb') as archivo:
        bytes_ = archivo.read()
    return bytes_


def guardar_archivo(bytes_, tipo, nombre):
    """
    bytes_: bytes a escribir en el archivo
    tipo: tipo de archivo (foto, gif o sonido, determina la extension)
    nombre: nombre del archivo (asi se va a llamar en la carpeta)

    Retorna True si la acción fue exitosa, False en caso contrario
    """

    ruta = join(RAIZ_ARCHIVOS, tipo, f'{nombre}.{FORMATOS[tipo]}')
    # El archivo ya existe, por lo que no se puede guardar.
    if isfile(ruta):
        return False
    with open(ruta, 'wb') as archivo:
        archivo.write(bytes_)
    return True


def almacenamiento_utilizado(data):
    """
    Calcula y devuelve el peso total de la data contenida en data
    """
    bytes_totales = 0
    for seccion, rutas in data.items():
        for nombre in rutas:
            ruta = join(RAIZ_ARCHIVOS, seccion, nombre)
            bytes_archivo = leer_archivo(ruta)
            bytes_totales += len(bytes_archivo)
    msg = (
        f' ** Uso actual: {bytes_totales//1000} /'
        f' {CAPACIDAD_MAXIMA//1000} kb'
    )
    return msg


def listdir_filtrado(ruta):
    """
    Cumple el mismo proposito que el metodo 'listdir', filtrando aquellos
    archivos que no queremos que se cuenten como parte de data.
    """
    dir_ = []
    for archivo in os.listdir(ruta):
        if (archivo in IGNORADOS) or (archivo in dir_):
            continue
        dir_.append(archivo)
    return dir_
