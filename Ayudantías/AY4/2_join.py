
######################
# Importar threading #
import threading
######################
import time
import random


class Software:

    def __init__(self, nombre, lineas_programa):
        self.nombre = nombre
        self.lineas_programa = lineas_programa
        self.lineas_escritas = 0
        self.queda_plazo = True

    def avance(self, progreso):
        if self.lineas_programa < self.lineas_escritas + progreso:
            self.lineas_escritas = self.lineas_programa
        else:
            self.lineas_escritas += progreso

    def lineas_restantes(self):
        return self.lineas_programa - self.lineas_escritas


class Jefe:

    def __init__(self):
        self.ingeniero = None

    def revisar_avance(self, software):
        lineas_min = 0.5*software.lineas_programa
        if software.lineas_escritas < lineas_min:
            software.queda_plazo = False
            time.sleep(1)
            print("No fast code no gain :|")
            print(f"{self.ingeniero.name} estas despedido")
        elif software.lineas_escritas == software.lineas_programa:
            print("Terminaron el proyecto!")
        else:
            time.sleep(1)
            print(f"Cuidadito {self.ingeniero.name}...")
            print(" Avanzaste, pero no terminaste asi que apúrate")


# Función target de thread
def programar(software):
    i = 0
    while software.lineas_restantes() > 0 and software.queda_plazo:
        lineas_escritas = random.randint(10, 20)
        time.sleep(1)
        software.avance(lineas_escritas)
        print(f"Día {i}: Escribí {lineas_escritas}, " +
              f"quedan {software.lineas_restantes()} líneas")
        i += 1


proyecto_software = Software("DCCiber Sustos", 150)
jefe = Jefe()
print(f"Iniciando {proyecto_software.nombre}")

#######################
# Thread de ingeniero #
jefe.ingeniero = threading.Thread(name="Wasowski",
                                  target=programar,
                                  args=(proyecto_software,))

#######################
# Iniciamos el thread #
jefe.ingeniero.start()

########################
# Uso de join(timeout) #
plazo_proyecto = 4
jefe.ingeniero.join(plazo_proyecto)

######################
# Revisión de estado #
jefe.revisar_avance(proyecto_software)
