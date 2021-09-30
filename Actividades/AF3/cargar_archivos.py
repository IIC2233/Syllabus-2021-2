from parametros import RUTA_PELICULAS, RUTA_USUARIOS
from pelicula import Pelicula
from usuario import Usuario


def cargar_peliculas():
    """
    Generador que entrega una secuencia de objetos de la clase Pelicula
    """
    with open(RUTA_PELICULAS, "rt", encoding="utf-8") as archivo:
        archivo.readline()
        for linea in archivo:
            nombre, deportes, arte, ciencia_ficcion, fantasia, comedia, \
                accion, actores = linea.strip().split(",")
            rankings = {
                "Deportes": int(deportes),
                "Arte": int(arte),
                "Ciencia Ficción": int(ciencia_ficcion),
                "Fantasía": int(fantasia),
                "Comedia": int(comedia),
                "Acción": int(accion),
            }
            actores = tuple(actor for actor in actores.split(";"))
            yield Pelicula(nombre, rankings, actores)


def cargar_usuarios():
    """
    Generador que entrega una secuencia de objetos de la clase Usuario
    """
    with open(RUTA_USUARIOS, "r", encoding="utf-8") as archivo:
        archivo.readline()
        for user in archivo:
            nombre, deportes, arte, ciencia_ficcion, fantasia, comedia,   \
                accion, actor_prohibido = user.strip().split(",")
            preferencias = {
                "Deportes": float(deportes),
                "Arte": float(arte),
                "Ciencia Ficción": float(ciencia_ficcion),
                "Fantasía": float(fantasia),
                "Comedia": float(comedia),
                "Acción": float(accion),
            }
            yield Usuario(nombre, preferencias, actor_prohibido)
