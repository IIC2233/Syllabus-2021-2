class Parque:

    def __init__(self, personas, atracciones):
        # No modificar
        self.personas = personas
        self.atracciones = atracciones

    def distribuir_personas(self):
        # COMPLETAR
        pass

    def simular_hora(self, hora):
        # No modificar
        print("---------------------------------")
        print(F"| INICIANDO SIMULACIÓN DE HORA {hora}|")
        print("---------------------------------")
        print()
        print("* Distribuyendo personas en los juegos")
        print()
        self.distribuir_personas()
        print()
        print("* Simulando juegos")
        print()
        n_atracciones = len(self.atracciones.values())
        counter = 1
        for atraccion in self.atracciones.values():
            print(f"\rNueva ronda de: ", end='')
            atraccion.nueva_ronda()
            print(f"Atracciones listas: {counter} de {n_atracciones}!\n")
            counter += 1

    def revisar_termino(self):
        # No modificar
        for persona in self.personas:
            if persona.juegos:
                return False
        return True

    def iniciar_dia(self):
        # No modificar
        termino = False
        horas = 0
        while not termino:
            self.simular_hora(horas)
            termino = self.revisar_termino()
            horas += 1
        print(f"El parque cerró luego de funcionar {horas} horas.")

    def __str__(self):
        texto = "\n" + "Personas".center(50) + "\n" + ("-" * 50) + "\n"
        for persona in self.personas:
            texto += f"* {persona}\n"
        texto += "\n" + "Atracciones".center(50) + "\n" + ("-" * 50) + "\n"
        for atraccion in self.atracciones.keys():
            texto += f"* {atraccion}\n"
        return texto
