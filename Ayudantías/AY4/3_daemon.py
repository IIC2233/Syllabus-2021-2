######################
# Importar threading #
import threading
import time


class Computador:

    def __init__(self):
        self.programas = []

    def correr_programas(self):
        # Correr threads
        for programa in self.programas:
            programa.start()

    def apagar(self):
        print("Apagando ... en 8 segundos")
        time.sleep(8)
        print("Ya debería estar apagado")


class Programa(threading.Thread):

    # Clase que hereda de Thread
    def __init__(self, nombre, daemon, tiempo_reporte):
        super().__init__()
        self.nombre = nombre
        # Atributo deamon se recibe como parámetro
        self.daemon = daemon
        self.tiempo_reporte = tiempo_reporte

    def run(self):
        # Ciclo infinito de felicidad
        while True:
            time.sleep(self.tiempo_reporte)
            print(f"Soy un programa de {self.nombre} feliz")


computador = Computador()
# Creación de threads de programas
word = Programa("W0rd", daemon=False, tiempo_reporte=5)
spotify = Programa("Sp0t1fy", daemon=False, tiempo_reporte=3)
chorme = Programa("G00gl3 Ch0rm3", daemon=False, tiempo_reporte=7)
computador.programas.extend([word, spotify, chorme])


# Correr y apagar para ver daemon
computador.correr_programas()
computador.apagar()
