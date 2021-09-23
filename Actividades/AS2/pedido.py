from random import randint
from threading import Event


class Pedido:
    def __init__(self, id_, tienda, descripcion):
        self.id_ = id_
        self.tienda = tienda
        self.descripcion = descripcion
        self.entregado = False
        self.distancia_destino = randint(1, 10)
        self.evento_llego_repartidor = Event()
        self.evento_pedido_listo = Event()
