from random import uniform, choice
from os import path
from parametros import PATH_REGALOS


class NodoAmigoSecreto:
    def __init__(self, usuario, siguiente=None):
        # No modificar
        self.usuario = usuario
        self.siguiente = siguiente or self
        self.regalo_entregado = False

    def insertar_amigo_secreto(self, nuevo_nodo, posicion,
                               posicion_actual=0):
        """
        Insertar un nuevo NodoAmigoSecreto en la posicion.
        :param nuevo_nodo: instancia de Usuario que debe ser
            insertada a la lista ligada.
        :param posicion: posición anterior al nuevo usuario. La posición
        puede ser mayor al tamaño de la lista, en cuyo caso se continuará
        dando vueltas hasta alcanzar el índice pedido.
        :param posicion_actual: Posición en la lista actual.
        """
        # Completar
        pass

    def entregar_regalos(self):
        # No modificar
        if self.regalo_entregado:
            print("Hemos dado toda la vuelta! "
                  "Daremos fin a este amigo secreto.")
            return
        print(f"¡{self} se prepara para entregar su "
              f"regalo a {self.siguiente}!")
        regalo, probabilidad = escoger_regalo()
        print(f"El regalo es.... ¡{regalo}!")
        if uniform(0, 1) < probabilidad:
            print(f"A {self.siguiente} le encantó el regalo!\n")
        else:
            print(f"A {self.siguiente} no le gustó mucho el regalo.\n"
                  f"Ya habrá otra oportunidad :(")
        self.regalo_entregado = True
        self.siguiente.entregar_regalos()

    def __str__(self):
        return f"Amigo Secreto {self.usuario}"


def escoger_regalo():
    # No modificar
    path_regalos = path.join(*PATH_REGALOS)
    with open(path_regalos, 'rt', encoding='utf-8') as file:
        regalos = [line.strip().split(',') for line in file]
    regalo = choice(list(regalos))
    return regalo[0], float(regalo[1])
