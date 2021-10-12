import sys
# from time import sleep  # DESCOMENTAR PARA THREAD
from PyQt5.QtCore import pyqtSignal, QTimer  # , QThread
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QVBoxLayout, QPushButton)

# ------------ DESCOMENTAR PARA THREAD ------------
'''
class ThreadBacan(QThread):
    def __init__(self, actualizar_label_signal, *args, **kwargs):
        # Entregar *args y **kwargs a la super clase es
        # importante por si queremos dar algun parametro
        # inicial de los que ya ofrece la clase QThread
        super().__init__(*args, **kwargs)
        # Le entregamos una senal que queremos que el Thread emita
        self.actualizar_label_signal = actualizar_label_signal

    def run(self):
        for _ in range(10):
            self.actualizar_label_signal.emit()
            sleep(0.5)
'''


class VentanaConThread(QWidget):
    actualizar_label_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.label_numero = QLabel("0", self)
        self.boton_numero = QPushButton("0", self)
        self.boton_loop = QPushButton("Iniciar Loop", self)

        self.layout_principal = QVBoxLayout(self)
        '''
        Creamos nuestro thread y le entregamos la señal
        para actualizar el label
        '''
        # ------------ DESCOMENTAR PARA THREAD ------------
        # self.thread_bacan = ThreadBacan(self.actualizar_label_signal)

        # O bien instanciamos un QTimer
        # ------------ DESCOMENTAR PARA TIMER ------------
        self.timer_epico = QTimer(self)

        self.init_gui()

    def init_gui(self):
        self.layout_principal.addWidget(self.label_numero)
        self.layout_principal.addStretch()
        self.layout_principal.addWidget(self.boton_numero)
        self.layout_principal.addWidget(self.boton_loop)

        self.boton_numero.clicked.connect(self.actualizar_boton)
        self.boton_loop.clicked.connect(self.iniciar_loop)
        self.actualizar_label_signal.connect(self.actualizar_label)

        self.show()

    def actualizar_label(self):
        numero_actual = int(self.label_numero.text())
        self.label_numero.setText(str(numero_actual + 1))

    def actualizar_boton(self):
        numero_actual = int(self.boton_numero.text())
        self.boton_numero.setText(str(numero_actual + 1))

    def iniciar_loop(self):
        # ------------ DESCOMENTAR PARA THREAD ------------
        # self.thread_bacan.start()

        '''
        Los timers emiten una senal cada vez que pasa una cantidad de tiempo
        especificada la cual puedes acceder para conectarla utilizando el
        atributo timeout.
        '''
        # ------------ DESCOMENTAR PARA TIMER ------------
        self.timer_epico.timeout.connect(self.actualizar_label)
        # Ojo: el tiempo se especifica en milisegundos!
        self.timer_epico.setInterval(1000)
        self.timer_epico.start()


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaConThread()
    sys.exit(app.exec_())
