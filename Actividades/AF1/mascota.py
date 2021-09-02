import random
import parametros as p

class Mascota:
    def __init__(self, nombre, raza, dueno,
                 saciedad, entretencion):
        self.nombre = nombre
        self.raza = raza
        self.dueno = dueno
        
        # Los siguientes valores están en %.
        self._saciedad = saciedad
        self._entretencion = entretencion

    # COMPLETAR
    def saciedad(self):
        pass

    # COMPLETAR
    def entretencion(self):
        pass

    @property
    def satisfaccion(self):
        return (self.saciedad//2 + self.entretencion//2)
    
    def comer(self, comida):
        # COMPLETAR
        pass

    def pasear(self):
        self.entretencion += p.ENTRETENCION_PASEAR
        self.saciedad += p.SACIEDAD_PASEAR
    
    def __str__(self):
        # COMPLETAR
        pass


class Perro:
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        pass
    
    def saludar(self):
        # COMPLETAR
        pass
        

class Gato:
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        pass

    def saludar(self):
        # COMPLETAR
        pass

class Conejo:
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        pass

    def saludar(self):
        # COMPLETAR
        pass
