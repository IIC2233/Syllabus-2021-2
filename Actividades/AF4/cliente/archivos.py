import os

from parametros import (
    RUTA_DATOS, IGNORADOS, RAIZ_ARCHIVOS, RUTA_TITULO,
)


def leer_data_local():
    """
    Lee los contenidos del directorio 'data' y devuelve un diccionario
    con sus contenidos.
    """
    data = {}
    for seccion, ruta in RUTA_DATOS.items():
        dir_ = listdir_filtrado(ruta)
        data[seccion] = dir_
    return data


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


def archivo_a_bytes(ruta):
    """
    Devuelve los bytes de un archivo en data
    """
    with open(ruta, 'rb') as archivo:
        return archivo.read()


def guardar_archivo(bytes_, ruta):
    """
    Escribe un conjunto de bytes al disco.
    """
    with open(ruta, 'wb') as archivo:
        archivo.write(bytes_)
    return True


def iniciar_sistema():
    """
    Realiza las operaciones iniciales necesarias para partir el cliente.
    """
    # Revisamos que la carpeta data exista
    os.makedirs(RAIZ_ARCHIVOS, exist_ok=True)
    # Aseguramos que existan las subcarpetas de archivos
    for ruta in RUTA_DATOS.values():
        os.makedirs(ruta, exist_ok=True)
    # Imprimimos el logo inicial
    with open(RUTA_TITULO, "r", encoding="UTF-8") as archivo:
        print(archivo.read())
        print("------ Consola ------")
