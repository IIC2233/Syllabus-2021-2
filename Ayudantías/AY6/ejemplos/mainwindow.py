import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QDockWidget)
from PyQt5.QtWidgets import QLabel

"""
Este ejemplo ilustra graficamente las partes que conforman una MainWindow
y su proposito es meramente expositivo. Si te interesa implementarla en
tu trabajo, te recomendamos referirte a la documentacion de Qt.
"""


class VentanaEjemplo(QLabel):
    """
    Label personalizada con un color un texto para indicar
    su posicion en la ventana.
    """
    def __init__(self, color, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Definimos por medio de stylesheets su color y un borde que
        # muestre los limites de la Widget.
        self.setStyleSheet(f'background-color: {color};'
                           ' border: 3px solid black')


class DockEjemplo(QDockWidget):
    """
    Widget personalizada para usar en los docks de la ventana principal.
    Tiene la opcion de desactivar las funcionalidades especiales de QDockWidget.
    Tambien define un color y borde para identificarlo.
    Importante, QDockWidget es un contenedor y necesita definir
    una widget a mostrar.
    """
    def __init__(self, color, texto, features_flag, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet(f'background-color: {color};'
                           ' border: 3px solid black')
        # Esta es la widget que se va a mostrar dentro del espacio del dock.
        self.label_texto = QLabel(texto, self)
        if not features_flag:
            # Si es que se entrega False, desactivamos las funcionalidades
            # especiales del QDockWidget.
            self.setFeatures(QDockWidget.NoDockWidgetFeatures)
            self.setTitleBarWidget(QWidget())
        self.setWidget(self.label_texto)


class VentanaCuatica(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 150, 1280, 720)
        self.setWindowTitle('La ventana mas cuatica')
        # Ahora, creamos las ventanas para mostrar con colores
        # cada parte de QMainWindow.
        self.ventana_central = VentanaEjemplo('red', 'CENTRO', self)
        self.ventana_superior = DockEjemplo('blue', 'DOCK SUPERIOR',
                                            False, self)
        self.ventana_derecha = DockEjemplo('cyan', 'DOCK DERECHO',
                                           True, self)
        self.ventana_izquierda = DockEjemplo('blue', 'DOCK IZQUIERDO',
                                             False, self)

        self.init_gui()

    def init_gui(self):
        # Definiendo quien utiliza el espacio al centro
        self.setCentralWidget(self.ventana_central)
        # Definiendo las widgets laterales
        self.addDockWidget(Qt.LeftDockWidgetArea, self.ventana_izquierda)
        self.addDockWidget(Qt.TopDockWidgetArea, self.ventana_superior)
        self.addDockWidget(Qt.RightDockWidgetArea, self.ventana_derecha)
        # Como crear una barra de herramientas
        self.herramientas = self.addToolBar('Ventana')
        self.herramientas.addAction('Accion 1')
        self.herramientas.addAction('Accion 2')
        self.herramientas.addAction('Accion 3')
        # Como crear una barra de menu
        menubar = self.menuBar()
        contexto_1 = menubar.addMenu("Contexto 1")
        contexto_1.addAction('Contexto 1 - Opcion 1')
        contexto_1.addAction('Contexto 1 - Opcion 2')
        contexto_1.addAction('Contexto 1 - Opcion 3')

        contexto_2 = menubar.addMenu("Contexto 2")
        contexto_2.addAction('Contexto 2 - Opcion 1')
        contexto_2.addAction('Contexto 2 - Opcion 2')
        contexto_2.addAction('Contexto 2 - Opcion 3')
        # Como utilizar la barra de estado
        self.statusBar().showMessage('Esta es la barra de estado :O')

        self.show()


if __name__ == '__main__':
    app = QApplication([])
    form = VentanaCuatica()

    sys.exit(app.exec_())
