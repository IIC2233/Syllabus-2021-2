from collections import defaultdict
from functools import reduce
from random import uniform

import parametros as p
from lista_reproduccion import ListaReproduccion
from parametros import LARGO_LISTA_REPRODUCCION


class Usuario:

    def __init__(self, nombre, preferencias, actor_prohibido):
        self.nombre = nombre
        self.preferencias = preferencias
        self.actor_prohibido = actor_prohibido
        self.listas_reproduccion = {}
        self.afinidades = defaultdict(int)

    @property
    def peliculas_favoritas(self):
        return set(self.afinidades)

    def ver_videos(self, nombre_lista):
        # Debes completar esta función
        pass

    def calcular_afinidad(self, pelicula):
        afinidad = 0
        for categoria in p.CATEGORIAS:
            afinidad += (
                pelicula.rankings[categoria] * self.preferencias[categoria]
            )
        if p.CATEGORIAS:
            afinidad /= len(p.CATEGORIAS)
        else:
            afinidad = 0
        # Guardamos la afinidad para despues!
        self.afinidades[pelicula.nombre] = afinidad
        return afinidad

    def calificar_pelicula(self, pelicula):
        # Una calificacion mayor hará menos probable
        # que le guste el video al usuario
        afinidad = self.afinidades[pelicula.nombre]
        calificacion = uniform(0, 5) * uniform(1, 5)
        return calificacion < afinidad

    def crear_lista(self, mapeo_videos, nombre_lista):
        peliculas_favoritas = self.encontrar_peliculas_preferidas(mapeo_videos)
        lista_reproduccion_creada = ListaReproduccion(
            set(peliculas_favoritas), self.nombre, nombre_lista,
        )
        self.listas_reproduccion[nombre_lista] = lista_reproduccion_creada

    @staticmethod
    def encontrar_peliculas_preferidas(mapeo_peliculas):
        peliculas_favoritas = set()
        for pelicula in mapeo_peliculas:
            if len(peliculas_favoritas) < LARGO_LISTA_REPRODUCCION:
                peliculas_favoritas.add(pelicula)
            else:
                pelicula_menos_afin = min(
                    peliculas_favoritas,
                    key=lambda x: x[1],
                )
                if pelicula[1] > pelicula_menos_afin[1]:
                    peliculas_favoritas.add(pelicula)
                    peliculas_favoritas.remove(pelicula_menos_afin)
        return peliculas_favoritas

    def limpiar_listas(self):
        self.listas_reproduccion = {}

    def print_stats(self):
        str_preferencia_categoria = " ".join(
            f"{nombre.upper(): ^15s}" for nombre in self.preferencias
        )
        str_preferencia_valor = " ".join(
            f"{valor: ^15.2f}" for valor in self.preferencias.values()
        )
        print(f"Nombre: {self.nombre}\n"
              f"Actor Prohibido: {self.actor_prohibido}\n"
              f"{str_preferencia_categoria}\n"
              f"{str_preferencia_valor}\n")

    def __add__(self, other):
        union_peliculas = self.peliculas_favoritas | other.peliculas_favoritas
        afinidad_comun = reduce(
            lambda x, y: x + self.afinidades[y] * other.afinidades[y],
            union_peliculas,
            0,
        )
        return int(afinidad_comun)

    def __repr__(self):
        return self.nombre
