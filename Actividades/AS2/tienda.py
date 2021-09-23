from threading import Thread, Lock
from time import sleep
from random import randint


class Tienda:
    def __init__(self, nombre):
        # NO MODIFICAR
        super().__init__()
        self.nombre = nombre
        self.cola_pedidos = []
        self.abierta = True
        # COMPLETAR DESDE AQUI

    def ingresar_pedido(self, pedido, shopper):
        # Completar
        pass

    def preparar_pedido(self, pedido):
        # Completar
        pass

    def run(self):
        # Completar
        pass
