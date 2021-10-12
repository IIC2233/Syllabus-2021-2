from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout,
    QLabel, QLineEdit, QPushButton,
)


class VentanaLogin(QWidget):

    senal_enviar_login = pyqtSignal(str)
    senal_segunda_ventana = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Log in")
        self.setGeometry(200, 200, 400, 150)

        # Elementos gráficos y posicionamiento
        self.username_label = QLabel("Username:", self)
        self.username_input = QLineEdit("", self)
        self.ingresar_button = QPushButton("Ingresar", self)

        hbox_top = QHBoxLayout()
        hbox_top.addStretch(1)
        hbox_top.addWidget(self.username_label)
        hbox_top.addWidget(self.username_input)
        hbox_top.addStretch(1)

        hbox_bottom = QHBoxLayout()
        hbox_bottom.addStretch(3)
        hbox_bottom.addWidget(self.ingresar_button)
        hbox_bottom.addStretch(3)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox_top)
        vbox.addLayout(hbox_bottom)
        vbox.addStretch(1)

        # Eventos y señales
        self.ingresar_button.clicked.connect(self.enviar_login)

        self.setLayout(vbox)

        self.show()

    def enviar_login(self):
        username = self.username_input.text()
        self.senal_enviar_login.emit(username)

    def recibir_login(self, resultado_login):
        if resultado_login:
            self.senal_segunda_ventana.emit()
            self.hide()
