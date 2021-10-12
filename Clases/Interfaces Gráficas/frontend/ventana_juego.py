from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel


class VentanaJuego(QMainWindow):

    senal_tecla_apretada = pyqtSignal(int)

    def __init__(self, ruta_sprite_jugador):
        super().__init__()
        self.setGeometry(100, 100, 600, 600)

        # Elementos gráficos
        self.label_jugador = QLabel(self)
        pixmap = QPixmap(ruta_sprite_jugador)
        self.label_jugador.setPixmap(pixmap)
        self.label_jugador.setGeometry(30, 30, 30, 80)
        self.label_jugador.setScaledContents(True)

    def mostrar_ventana(self):
        self.show()

    def keyPressEvent(self, event):
        key = event.key()
        self.senal_tecla_apretada.emit(key)
