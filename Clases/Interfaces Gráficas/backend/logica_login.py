from PyQt5.QtCore import QObject, pyqtSignal


class LogicaLogin(QObject):

    senal_resultado_login = pyqtSignal(bool)

    def __init__(self):
        super().__init__()

    def validar_login(self, username):
        resultado = username.isalnum()
        self.senal_resultado_login.emit(resultado)
