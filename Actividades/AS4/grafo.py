from collections import deque


class NodoGrafo:
    def __init__(self, usuario):
        # No modificar
        self.usuario = usuario
        self.amistades = None

    def formar_amistad(self, nueva_amistad):
        # Completar
        pass

    def eliminar_amistad(self, ex_amistad):
        # Completar
        pass


def recomendar_amistades(nodo_inicial, profundidad):
    """
    Recibe un NodoGrafo inicial y una profundidad de busqueda, retorna una
    lista de nodos NodoGrafo recomendados como amistad a esa profundidad.
    """
    # Debes modificarlo


def busqueda_famosos(nodo_inicial, visitados=None, distancia_min=80):
    """
    [BONUS]
    Recibe un NodoGrafo y busca en la red social al famoso mas
    cercano, retorna la distancia y el nodo del grafo que contiene
    a el usuario famoso cercano al que se encuentra.
    """
    # Completar para el bonus
