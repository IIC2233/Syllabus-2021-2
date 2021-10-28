from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication
from parametros import (
    PATH_PARRILLA, PATH_HAMBURGUESA, POSICION_HAMBURGUESA_ABAJO,
    POSICION_HAMBURGUESA_ARRIBA, CLICK_AREA_AGREGAR, CLICK_AREA_BOTAR,
    CLICK_AREA_SACAR
)
import sys


class Hamburguesa(QLabel):

    senal_seleccionar_hamburguesa = pyqtSignal(int)

    def __init__(self, id, coccion, parent):
        super().__init__(parent)
        self.id = id
        self.coccion = coccion
        self.en_estante = False
        self.senal_seleccionar_hamburguesa.connect(
            parent.seleccionar_hamburguesa
        )
        self.show()

    def coccion(self):
        # Completar Property
        pass

    def mousePressEvent(self, event):
        # Completar
        pass


class VentanaCoccion(QWidget):

    senal_agregar_hamburguesa = pyqtSignal()
    senal_aumento_coccion = pyqtSignal(int, int)
    senal_botar_hamburguesa = pyqtSignal(int)
    senal_sacar_hamburguesa = pyqtSignal(int)
    senal_pasar_armado = pyqtSignal()

    def __init__(self, ventana_anterior, parent=None):
        super().__init__(parent)
        self.ventana_anterior = ventana_anterior
        self.move(200, 200)
        self.setWindowTitle("DCChef")
        self.background = QLabel(self)
        pixmap = QPixmap(PATH_PARRILLA)
        self.background.setPixmap(pixmap)
        self.setFixedSize(pixmap.size())
        self.hamburguesas = [None, None]
        self.mensaje_explicacion = QLabel(self)
        self.mensaje_explicacion.setGeometry(200, 50, 600, 60)
        self.mensaje_explicacion.setFont(QFont('Arial', 20))
        self.mensaje_explicacion.setWordWrap(True)
        self.hamburguesa_seleccionada = None
        self.hamburguesas_cocidas = []
        self.fuente_hamburguesas = QLabel(self)
        pixmap = QPixmap(PATH_HAMBURGUESA)
        self.fuente_hamburguesas.setPixmap(pixmap)
        self.fuente_hamburguesas.setFixedSize(pixmap.size())
        self.fuente_hamburguesas.move(30, 540)
        self.boton_pasar_armado = QPushButton("Armar pedido", self)
        self.boton_pasar_armado.setGeometry(400, 600, 150, 80)
        self.boton_pasar_armado.clicked.connect(self.pasar_armado)

    def pasar_armado(self):
        self.senal_pasar_armado.emit()

    @property
    def hamburguesa_seleccionada(self):
        return self._hamburguesa_seleccionada

    @hamburguesa_seleccionada.setter
    def hamburguesa_seleccionada(self, value):
        self._hamburguesa_seleccionada = value
        if value is None:
            self.mensaje_explicacion.setText(
                "No hay hamburguesas seleccionadas"
            )
        elif value == self.hamburguesas[1]:
            self.mensaje_explicacion.setText(
                "Está seleccionada la hamburguesa de abajo"
            )
        elif value == self.hamburguesas[0]:
            self.mensaje_explicacion.setText(
                "Está seleccionada la hamburguesa de arriba"
            )

    def cocer_hamburguesa(self, id, coccion):
        hamburguesa = self.obtener_hamburguesa(id)
        hamburguesa.coccion = coccion

    def obtener_hamburguesa(self, id):
        hamburguesas = list(filter(lambda x: x is not None, self.hamburguesas))
        for hamburguesa in hamburguesas:
            if hamburguesa.id == id:
                return hamburguesa
        return None

    def seleccionar_hamburguesa(self, id):
        hamburguesa = self.obtener_hamburguesa(id)
        self.hamburguesa_seleccionada = hamburguesa

    def terminar_cocer(self, id):
        hamburguesa = self.obtener_hamburguesa(id)
        y_position = 541 - 20*len(self.hamburguesas_cocidas)
        hamburguesa.move(798, y_position)
        hamburguesa.en_estante = True
        self.vaciar_espacio_parrilla(hamburguesa)
        self.hamburguesas_cocidas.append(hamburguesa)
        hamburguesa.raise_()
        self.hamburguesa_seleccionada = None

    def pedido_generado(self):
        self.show()
        self.ventana_anterior.hide()

    def vaciar_espacio_parrilla(self, hamburguesa):
        if self.hamburguesas[0] == hamburguesa:
            self.hamburguesas[0] = None
        elif self.hamburguesas[1] == hamburguesa:
            self.hamburguesas[1] = None

    def procesar_click_area(self, area, x, y):
        dentro_x = area[0][0] <= x <= area[0][1]
        dentro_y = area[1][0] <= y <= area[1][1]

        return dentro_x and dentro_y

    def procesar_click(self, x, y):
        # Completar
        pass

    def mousePressEvent(self, event):
        # Completar
        pass

    def agregar_hamburguesa(self, id, coccion):
        # Completar
        pass

    def eliminar_hamburguesa(self, id):
        # Completar
        pass


if __name__ == '__main__':
    app = QApplication([])
    login = VentanaCoccion()
    sys.exit(app.exec_())
