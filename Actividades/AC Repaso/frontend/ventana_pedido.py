from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget
from PyQt5.QtGui import QPixmap
from parametros import (PATH_FONDO_INICIO)


class VentanaPedido(QWidget):

    senal_generar_pedido = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        # Posición y título de ventana
        self.move(200, 200)
        self.setWindowTitle("DCChef")

        # Se le pone imagen de fondo,
        # Ajustamos para que la ventana tenga el tamaño del fondo
        self.background = QLabel(self)
        pixmap = QPixmap(PATH_FONDO_INICIO)
        self.background.setPixmap(pixmap)
        self.setFixedSize(pixmap.size())

        # COMPLETAR
        # Preparamos el botón para avanzar a la siguiente ventana

    def pedir_generar_pedido(self):
        # Completar
        pass
