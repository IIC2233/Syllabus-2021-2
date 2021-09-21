from threading import Event, Thread, Lock  # Timer
from queue import Queue
from time import sleep


class Colonia(Thread):

    def __init__(self, jardin):
        super().__init__()
        self.polen = Queue()
        self.miel = Queue()
        self.jardin = jardin

        self.senal_inicio_trabajo = Event()

        self.obreras = [Abeja(self, jardin) for _ in range(4)]

    def run(self):
        print('\nBienvenido a la DCColonia!')
        print('Iniciando día...\n')
        sleep(5)

        self.iniciar_dia()
        self.criar_abeja()

        # ¿Cómo les comunicamos a las abejas que deben
        # comenzar a trabajar?
        # self.senal_inicio_trabajo

        while True:
            if input() == 'end':
                break
            """
            El thread de la colonia se quedará esperando
            instrucciones por consola. Terminará si recibe
            "end" como input.
            """
        self.imprimir_estado()
        print('✖ Fin thread colonia')

    def iniciar_dia(self):
        # COMPLETAR
        """
        Este método recorre self.obreras e inicia todos
        los threads.
        """
        pass

    def criar_abeja(self):
        # COMPLETAR
        """
        Este método crea una nueva instancia de Abeja
        cada cierto tiempo, con un objeto Timer.
        """
        pass

    def imprimir_estado(self):
        print('\n' + '----'*5)
        print('Estado DCColonia')
        print(f'Número de abejas: {len(self.obreras)}')
        print(f'Unidades de miel: {self.miel.qsize()}')
        print('---'*6)


class Abeja(Thread):

    counter = 0
    lock_abertura = Lock()

    def __init__(self, colonia, jardin):
        super().__init__()
        self.id = Abeja.counter
        Abeja.counter += 1
        self.polen = Queue()
        self.colonia = colonia
        self.jardin = jardin

        # ¿Daemon?, ¿Sí o no?, ¿Por qué?
        # self.daemon =

    def __str__(self):
        n = self.id
        return f'Abeja {n}'

    def run(self):
        print(f'✚ {self} ha nacido')

        # ¿Cómo esperamos a que la colonia nos de la señal
        # de que se debe comenzar a trabajar?
        # self.colonia.senal_inicio_trabajo

        while True:
            self.salir_colonia()
            self.volar_al_jardin()
            self.recolectar_polen()
            self.volar_a_la_colonia()
            self.entrar_colonia()
            self.producir_miel()

    def salir_colonia(self):
        # ¿Cómo nos aseguramos que pase solo una abeja
        # a la vez por la abertura de la colonia?
        pass

    def volar_al_jardin(self):
        sleep(5)
        print(f'❀ {self} llegó al jardín')

    def volar_a_la_colonia(self):
        sleep(5 * self.polen.qsize())
        print(f'▣ {self} regresó a la colonia')

    def recolectar_polen(self):
        sleep(5)

        # ¿Cómo sacamos una unidad de polen del jardín
        # y se la entregamos a una abeja?
        # self.polen

        print(f'▧ {self} recolectó {self.polen.qsize()} polen, y se devuelve')

    def entrar_colonia(self):
        # COMPLETAR
        pass

    def producir_miel(self):
        self.colonia.polen.get()
        sleep(10)
        self.colonia.miel.put('unidad_miel')
        print(f'♨ {self} ha producido una unidad de miel')


class Jardin(Thread):

    def __init__(self):
        super().__init__()
        self.daemon = True
        self.polen = Queue()

    def run(self):
        while True:
            sleep(1)
            self.polen.put('unidad_polen')


if __name__ == '__main__':

    jardin = Jardin()
    colonia = Colonia(jardin)
    jardin.start()
    colonia.start()
