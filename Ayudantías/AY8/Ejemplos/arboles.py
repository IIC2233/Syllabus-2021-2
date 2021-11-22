# Ahora ejemplifacremos los árboles
from string import ascii_lowercase
from random import choices, choice


class Arbol:
    id_nodo = 0

    def __init__(self, valor, padre=None):
        self.id_ = Arbol.id_nodo
        Arbol.id_nodo += 1
        self.valor = valor
        self.padre = padre
        self.hijos = set()

    def obtener_nodo(self, id_nodo):
        if self.id_ == id_nodo:
            return self
        for hijo in self.hijos:
            nodo = hijo.obtener_nodo(id_nodo)
            if nodo is not None:
                return nodo

    def agregar_nodo(self, valor, id_padre):
        print(f"agregando valor {valor} en {id_padre}")
        nodo_padre = self.obtener_nodo(id_padre)
        if nodo_padre is None:
            return
        nuevo_nodo = Arbol(valor, nodo_padre)
        nodo_padre.hijos.add(nuevo_nodo)

    def insertar_nodo(self, valor, id_hijo):
        nodo_a_reemplazar = self.obtener_nodo(id_hijo)
        if nodo_a_reemplazar is None:
            return
        nodo_padre = nodo_a_reemplazar.padre
        nodo_padre.hijos.remove(nodo_a_reemplazar)
        nuevo_nodo = Arbol(valor, nodo_padre)
        nodo_padre.hijos.add(nuevo_nodo)
        nuevo_nodo.hijos.add(nodo_a_reemplazar)

    def __str__(self):
        return f"{self.id_} -> {self.valor}"


def print_arbol(arbol, indent=0):
    texto = "|  " * indent
    texto += f"id: {arbol.id_}, valor: {arbol.valor}"
    texto += ', nodo hoja' if len(arbol.hijos) == 0 else ''
    print(texto)
    for hijo in arbol.hijos:
        print_arbol(hijo, indent + 1)


# Ahora poblaremos el arbol de secuencias de palabras aleatorias

arbol = Arbol("Soy el Nodo Inicial")
for _ in range(15):
    texto = ''.join(choices(ascii_lowercase, k=6))
    id_padre = choice(range(Arbol.id_nodo))
    arbol.agregar_nodo(texto, id_padre)

print_arbol(arbol)



