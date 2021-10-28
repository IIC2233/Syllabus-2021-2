from PyQt5.QtCore import QObject, QThread, pyqtSignal
from random import randint, sample, random, shuffle
from parametros import (
    TIEMPOS_COCCION, INGREDIENTES_POSIBLES, MAXIMO_INGREDIENTES
)
from time import sleep


class Hamburguesa(QThread):
    id = 1

    def __init__(self, senal_coccion):
        super().__init__()
        self.id = Hamburguesa.id
        Hamburguesa.id += 1
        self.coccion_actual = 1
        self.senal_coccion = senal_coccion
        self.usuario_saco = False

    def avanzar_coccion(self, tiempo):
        # Completar
        pass

    def run(self):
        # Completar
        pass


class DCChef(QObject):

    senal_hamburguesa_agregada = pyqtSignal(int, int)
    senal_coccion_hamburguesa = pyqtSignal(int, int)
    senal_hamburguesa_botada = pyqtSignal(int)
    senal_pedido_generado = pyqtSignal()
    senal_hamburguesa_termino_cocerse = pyqtSignal(int)
    senal_ingrediente_agregado = pyqtSignal(str, int)
    senal_comenzo_armado = pyqtSignal(dict)
    senal_ingrediente_anadido_sandwich = pyqtSignal(str, int)
    senal_informar_resultado = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.ingredientes_pedido = None
        self.ingredientes_actual = []
        self.ingredientes_posibles = INGREDIENTES_POSIBLES
        self.hamburguesas_parrilla = []
        self.hamburguesas_cocidas = []

    def generar_pedido(self):
        n_ingredientes = randint(1, MAXIMO_INGREDIENTES)
        ingredientes = sample(self.ingredientes_posibles, n_ingredientes)
        ingredientes.append('hamburguesa')
        if random() <= 0.5:
            ingredientes.append('hamburguesa')
        shuffle(ingredientes)
        self.ingredientes_pedido = ingredientes
        self.senal_pedido_generado.emit()

    def agregar_ingrediente_sandwich(self, ingrediente):
        if ingrediente != 'pan_superior':
            self.ingredientes_actual.append(ingrediente)
        self.senal_ingrediente_anadido_sandwich.emit(ingrediente, -1)

    def finalizar_juego(self):
        if self.ingredientes_actual != self.ingredientes_pedido:
            texto = 'Nunca vi alguien tan malo'
        else:
            texto = 'Felicidades! Ganaste!'
        self.senal_informar_resultado.emit(texto)

    def sacar_hamburguesa(self, id):
        for hamburguesa in self.hamburguesas_parrilla:
            if hamburguesa.id == id:
                hamburguesa.usuario_saco = True
                return hamburguesa

    def terminar_cocer_hamburguesa(self, id):
        hamburguesa = self.sacar_hamburguesa(id)
        self.hamburguesas_cocidas.append(hamburguesa)
        self.hamburguesas_parrilla = list(
            filter(lambda x: x.id != id, self.hamburguesas_parrilla)
        )
        self.senal_hamburguesa_termino_cocerse.emit(id)

    def botar_hamburguesa(self, id):
        self.sacar_hamburguesa(id)
        self.hamburguesas_parrilla = list(
            filter(lambda x: x.id != id, self.hamburguesas_parrilla)
        )
        self.senal_hamburguesa_botada.emit(id)

    def obtener_hamburguesa_cocida(self, id):
        for hamburguesa in self.hamburguesas_cocidas:
            if hamburguesa.id == id:
                return hamburguesa
        return None

    def agregar_hamburguesa_sandwich(self, id):
        hamburguesa = self.obtener_hamburguesa_cocida(id)
        if hamburguesa is not None:
            self.hamburguesas_cocidas = list(
                filter(lambda x: x != hamburguesa, self.hamburguesas_cocidas)
            )
            self.ingredientes_actual.append('hamburguesa')
            self.senal_ingrediente_anadido_sandwich.emit('hamburguesa', id)

    def agregar_hamburguesa_parrilla(self):
        # Completar
        pass

    def empezar_armado(self):
        # Completar
        pass


if __name__ == '__main__':
    chef = DCChef()
    chef.generar_pedido()
    chef.agregar_ingrediente('hamburguesa')
    chef.agregar_ingrediente('pepinillo')
    chef.agregar_ingrediente('queso')
    breakpoint()
