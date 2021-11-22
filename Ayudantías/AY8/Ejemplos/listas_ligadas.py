# A continuación veremos un ejemplo básico de una lista ligada
# No es necesario crear una clase especial para lista!
# Solo una clase para los nodos
from os import path
import json


class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

    def append(self, valor):
        if self.siguiente is None:
            self.siguiente = Nodo(valor)
        else:
            self.siguiente.append(valor)

    def conseguir_valor(self, posicion, posicion_actual=0):
        if posicion == posicion_actual:
            return self.valor
        return self.siguiente.conseguir_valor(posicion, posicion_actual + 1)

    def insertar_nodo(self, valor, posicion, posicion_actual=0):
        if posicion == posicion_actual:
            siguiente = self.siguiente
            self.siguiente = Nodo(valor, siguiente)
        else:
            self.siguiente.insertar_nodo(valor, posicion,
                                         posicion_actual + 1)

    def __str__(self):
        return f"Head: Nodo con valor {self.valor}\n" \
               f"Nodo siguiente: {self.siguiente}"


lista_ligada = Nodo("Hola soy un nodo")
lista_ligada.append("Hola soy un nuevo nodo")
respuesta = "placeholder"
while respuesta != "0":
    respuesta = input("Inventa nodos!\n"
                      "0 para terminar: ")
    lista_ligada.append(respuesta)

print(lista_ligada.conseguir_valor(1))
lista_ligada.insertar_nodo("Me colé jeje", 2)
print(lista_ligada)


# Una lista ligada algo más difícil...

# Esta vez, los nodos guardarán una clase más compleja que un str
# Inventaremos una lista ligada cerrada que recorre los días de una semana

class DiaSemana:
    def __init__(self, nombre, despertador):
        self.nombre = nombre
        self.despertador = despertador

    def sonar_alarma(self):
        print(f"Hoy es {self}! La alarma sonará a las "
              f"{self.despertador}")

    def __str__(self):
        return self.nombre


# Crearemos además una clase especial

class ListaLigada:
    def __init__(self):
        self.head = None

    def append(self, valor):
        if self.head is None:
            self.head = Nodo(valor)
        self.head.append(valor)

    def activar_despertadores(self):
        nodo = self.head
        while nodo is not None:
            nodo.valor.sonar_alarma()
            nodo = nodo.siguiente


# Desafío: hacer que se trate de una lista ligada cerrada!
# Es decir, que el último nodo conecte con el primero

path = path.join('Ejemplos', 'archivos', 'data.json')
with open(path, encoding='utf-8') as file:
    dias = json.load(file)['DIAS']

lista_ligada = ListaLigada()
for nombre_dia, hora_despertador in dias:
    dia = DiaSemana(nombre_dia, hora_despertador)
    lista_ligada.append(dia)

lista_ligada.activar_despertadores()
