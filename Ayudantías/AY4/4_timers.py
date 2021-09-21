######################
# Importar threading #
import threading
######################


class Menu:
    def __init__(self, opciones):
        self.opciones = opciones

    def ejecutar(self):
        while True:
            for (llave, valor) in self.opciones.items():
                print(f"[{llave:2s}]. {valor}")
            accion = input("\nElige una opcion: ")
            if accion not in self.opciones.keys():
                print("\nOpcion inválida, ingresa un dígito de las opciones\n")
            else:
                return self.opciones[accion]


class Jugador:

    def __init__(self):
        super().__init__()
        self.mala_actitud = 0
        self.baneado = False

    def checkear_estado(self):
        if self.mala_actitud > 15:
            self.baneado = True
            # Timer para desbaneo
            timer = threading.Timer(5, self.desbanear)
            # Comenzar timer
            timer.start()

    def desbanear(self):
        self.baneado = False
        self.mala_actitud = min(self.mala_actitud/2, 14)


menu_inicio = Menu({"0": "Salir del programa", "1": "Jugar"})
menu_juego = Menu({"0": "Apotar al equipo", "1": "Flamear", "2": "Rendirse"})
jugador = Jugador()
while True:
    print("\n---------------------------------")
    print("DCCompetencia poco sana- El juego")
    print("---------------------------------\n")
    accion_inicio = menu_inicio.ejecutar()
    if accion_inicio == "Salir del programa":
        break
    else:
        # Revisamos baneo del jugador
        if jugador.baneado:
            print("\n-----------------------------------------\n")
            print("No puedes jugar por banneo, lo sentimos")
        else:
            turnos_restantes = 4
            while turnos_restantes > 0:
                print("\n--------------------------------")
                print("            Menu juego")
                print("--------------------------------\n")
                print(f"Turnos restantes {turnos_restantes}")
                accion_juego = menu_juego.ejecutar()
                if accion_juego == "Aportar al equipo":
                    jugador.mala_actitud -= 4
                elif accion_juego == "Flamear":
                    jugador.mala_actitud += 3
                elif accion_juego == "Rendirse":
                    jugador.mala_actitud += 7
                    break
                turnos_restantes -= 1
            # Checkeamos si merece banneo temporal
            jugador.checkear_estado()
