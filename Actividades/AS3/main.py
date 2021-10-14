import sys

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication

import parametros as p
from backend.logica_inicio import LogicaInicio
from backend.logica_juego import LogicaJuego, DCCobra
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_juego import VentanaJuego


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])

    # Instanciación de ventanas
    tamano_ventana = QRect(*p.WINDOW_SIZE_ARGS)
    ventana_inicio = VentanaInicio(tamano_ventana)
    ventana_juego = VentanaJuego()

    # Instanciación de lógica
    logica_inicio = LogicaInicio()
    cobra = DCCobra()
    logica_juego = LogicaJuego(cobra)

    # ~~ Conexiones de señales ~~

    # Ventana Inicio
    # COMPLETAR

    ventana_inicio.senal_enviar_login.connect(
        logica_inicio.comprobar_contrasena
    )

    # Ventana Juego
    # Atención: Descomenta las siguientes señales al comenzar la parte 2.

    # ventana_juego.senal_iniciar_juego.connect(
    #     logica_juego.iniciar_juego
    # )
    # ventana_juego.senal_tecla.connect(
    #     cobra.cambiar_direccion
    # )
    # ventana_juego.senal_tecla.connect(cobra.cambiar_direccion)
    # logica_juego.senal_actualizar.connect(
    #     ventana_juego.actualizar
    # )
    # logica_juego.senal_perder.connect(
    #     ventana_juego.fin_del_juego
    # )

    ventana_inicio.mostrar()
    app.exec()
