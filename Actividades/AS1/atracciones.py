from abc import ABC, abstractmethod
import parametros as p


# Recuerda definir esta clase como abstracta!
class Atraccion:

    def __init__(self, nombre, capacidad):
        # No modificar
        self.nombre = nombre
        self.capacidad_maxima = capacidad
        self.fila = []

    def ingresar_persona(self, persona):
        # No modificar
        print(f"** {persona.nombre} ha entrado a la fila de {self.nombre}")
        self.fila.append(persona)
        persona.esperando = True

    def nueva_ronda(self):
        # No modificar
        personas_ingresadas = 0
        lista_personas = []
        while personas_ingresadas < self.capacidad_maxima and self.fila:
            lista_personas.append(self.fila.pop(0))

        self.iniciar_juego(lista_personas)

        for persona in lista_personas:
            persona.actuar()

    def iniciar_juego(self, personas):
        # No modificar
        for persona in personas:
            print(f"*** {persona.nombre} jugó esta ronda")
            persona.esperando = False
            self.efecto_atraccion(persona)
        print()

    @abstractmethod
    def efecto_atraccion(self, persona):
        # No modificar
        pass

    def __str__(self):
        return f"Atraccion {self.nombre}"


# Recuerda completar la herencia!
class AtraccionFamiliar:

    def __init__(self):
        # COMPLETAR
        pass

    def efecto_atraccion(self, persona):
        # COMPLETAR
        pass


# Recuerda completar la herencia!
class AtraccionAdrenalinica:

    def __init__(self):
        # COMPLETAR
        pass

    def efecto_atraccion(self, persona):
        # COMPLETAR
        pass


# Recuerda completar la herencia!
class AtraccionAcuatica:

    def __init__(self):
        # COMPLETAR
        pass

    def ingresar_persona(self, persona):
        # COMPLETAR
        pass


# Recuerda completar la herencia!
class MontanaAcuatica:

    def __init__(self):
        # COMPLETAR
        pass

    def iniciar_juego(self, personas):
        # COMPLETAR
        pass
