import sys

from PyQt5.QtWidgets import QApplication

from backend.logica_login import LogicaLogin
from backend.logica_juego import LogicaJuego
from frontend.ventana_login import VentanaLogin
from frontend.ventana_juego import VentanaJuego
from parametros import RUTA_SPRITE_JUGADOR


if __name__ == '__main__':
    app = QApplication([])
    # Elementos gráficos (front-end)
    ventana_login = VentanaLogin()
    ventana_juego = VentanaJuego(RUTA_SPRITE_JUGADOR)
    # Elementos de lógica (back-end)
    logica_login = LogicaLogin()
    logica_juego = LogicaJuego()
    # Comunicación entre elementos
    ventana_login.senal_enviar_login.connect(logica_login.validar_login)
    logica_login.senal_resultado_login.connect(ventana_login.recibir_login)
    ventana_login.senal_segunda_ventana.connect(ventana_juego.mostrar_ventana)
    ventana_juego.senal_tecla_apretada.connect(logica_juego.procesar_tecla)

    sys.exit(app.exec_())
