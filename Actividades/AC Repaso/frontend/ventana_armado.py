from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel, QWidget
from PyQt5.QtGui import QPixmap, QFont
from parametros import (
    SPRITES_INGREDIENTES, PATH_FONDO_ARMADO, POSICION_HAMBURGUESAS,
    POSICION_INGREDIENTES_ARRIBA, POSICION_INGREDIENTES_ABAJO,
    TAMANO_INGREDINTES
)


class Ingrediente(QLabel):

    id = 0
    senal_ingrediente_agregado = pyqtSignal(str, int)

    def __init__(self, tipo, parent=None, clickeable=True, id=None):
        super().__init__(parent)
        if id is not None:
            self.id = id
            Ingrediente.id = id + 1
        self.tipo = tipo
        self.clickeable = clickeable
        self.senal_ingrediente_agregado.connect(
            parent.pedir_agregar_ingrediente_a_hamburguesa
        )
        pixmap = QPixmap(f'./frontend/assets/sprites/{tipo}.png')
        self.setFixedSize(pixmap.size())
        self.setPixmap(pixmap)

    def mousePressEvent(self, event):
        # Completar
        pass


class VentanaArmado(QWidget):

    senal_agregar_ingrediente = pyqtSignal(str)
    senal_agregar_hamburguesa = pyqtSignal(int)
    senal_finalizar_sandwich = pyqtSignal()

    def __init__(self, ventana_anterior, parent=None):
        super().__init__(parent)
        self.ventana_anterior = ventana_anterior
        self.move(200, 200)
        self.setWindowTitle("DCChef")
        self.background = QLabel(self)
        pixmap = QPixmap(PATH_FONDO_ARMADO)
        self.setFixedSize(pixmap.size())
        self.background.setPixmap(pixmap)
        self.mensaje_explicacion = QLabel(self)
        self.mensaje_explicacion.setGeometry(80, 50, 750, 120)
        self.mensaje_explicacion.setWordWrap(True)
        self.mensaje_explicacion.setFont(QFont('Arial', 20))
        self.posicion_siguiente_ingrediente = [280, 605]
        self.hamburguesas = {}

    def pedir_agregar_ingrediente_a_hamburguesa(self, tipo, id):
        if 'hamburguesa' in tipo:
            self.senal_agregar_hamburguesa.emit(id)
        elif 'pan_superior' in tipo:
            self.senal_agregar_ingrediente.emit(tipo)
            self.senal_finalizar_sandwich.emit()
        else:
            tipo = tipo.replace('_botella', '')
            self.senal_agregar_ingrediente.emit(tipo)

    def mostrar_resultado(self, texto):
        self.mensaje_explicacion.setText(texto)

    def comenzo_armado(self, info_pedido):
        self.show()
        self.ventana_anterior.hide()
        self.poner_ingredientes(info_pedido['hamburguesas'])
        self.mensaje_explicacion.setText(info_pedido['pedido'])
        pan_inferior = Ingrediente('pan_inferior', self, clickeable=False)
        self.agregar_label_a_hamburguesa_preparada(pan_inferior)

    def agregar_ingrediente_a_hamburguesa(self, tipo, id):
        if tipo == 'hamburguesa':
            label = self.hamburguesas[id]
        else:
            label = Ingrediente(tipo, self, False)
        self.agregar_label_a_hamburguesa_preparada(label)

    def agregar_label_a_hamburguesa_preparada(self, label):
        x = self.posicion_siguiente_ingrediente[0] - label.width() / 2
        y = self.posicion_siguiente_ingrediente[1] - label.height() / 2
        label.move(x, y)
        label.raise_()
        label.show()
        self.posicion_siguiente_ingrediente[1] -= TAMANO_INGREDINTES[1]//2

    def poner_ingredientes(self, hamburguesas):
        # Completar
        pass
