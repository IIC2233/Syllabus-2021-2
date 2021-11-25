from parametros import PROFUNDIDAD, ORDEN_FAMA
from usuario import Usuario
from lista_ligada import NodoAmigoSecreto
from arbol import ArbolBinario, NodoFama
from grafo import (NodoGrafo, recomendar_amistades, busqueda_famosos)


class DCCelebrity:
    def __init__(self):
        self.lista_ligada = None
        self.arbol = ArbolBinario()
        self.nodos_grafo = {}

    def crear_red(self, info_usuarios):
        dict_usuarios = {
            nombre: Usuario(nombre, atributos["correo"], atributos["fama"])
            for nombre, atributos in info_usuarios.items()
        }

        # Crear lista
        usuarios = iter(dict_usuarios.values())
        self.lista_ligada = NodoAmigoSecreto(next(usuarios))
        usuarios_recorridos = 0
        for usuario in usuarios:
            self.lista_ligada.insertar_amigo_secreto(usuario,
                                                     usuarios_recorridos)
            usuarios_recorridos += 1

        # Crear arbol
        nodos_fama = [NodoFama(usuario) for _, usuario in dict_usuarios.items()]
        nodos_ordenados = sorted(nodos_fama,
                                 key=lambda x: ORDEN_FAMA.index(x.usuario.fama))
        self.arbol.crear_arbol(nodos_ordenados)

        # Crear nodos grafo
        self.nodos_grafo = {
            nombre: NodoGrafo(dict_usuarios[nombre])
            for nombre in info_usuarios.keys()
        }
        # Crear amistades
        for nombre, atributos in info_usuarios.items():
            amistades = [
                self.nodos_grafo[nombre_amistad]
                for nombre_amistad in atributos["amistades"]
            ]
            self.nodos_grafo[nombre].amistades = amistades

    def run(self):
        print("Bienvenid@ a DCCelebrity!\n ")
        running = True
        nodo_grafo, usuario = None, None
        while running:
            if usuario is None:
                self.print_usuarios(self.nodos_grafo.values())
                nombre = input("Introduce tu nombre para ingresar, "
                               "o 0 para salir: ")
                if nombre == '0':
                    running = False
                elif nombre in self.nodos_grafo:
                    nodo_grafo = self.nodos_grafo[nombre]
                    usuario = nodo_grafo.usuario
                else:
                    print("Este nombre no se encuentra en la base de datos!")
                continue

            acciones_validas = self.acciones_validas(usuario.es_famoso)
            accion = self.recibir_accion(acciones_validas)
            if accion == 'Volver':
                usuario = None

            elif accion == 'Ver Amistades':
                print(f"Usuario {usuario.nombre} "
                      "tiene las siguientes amistades:")
                for num, amistad in enumerate(nodo_grafo.amistades):
                    print(f"{num}.- {amistad.usuario}")

            elif accion == 'Resumen DCCelebrity':
                self.arbol.print_arbol()

            elif accion == 'Recomendar Amistad':
                print(f"Amistades recomendadas para {usuario.nombre}:")
                amistades = recomendar_amistades(nodo_grafo, PROFUNDIDAD)
                self.print_usuarios(amistades, ignorar_nombre=usuario.nombre)

            elif accion == 'Agregar Amistad':
                self.print_usuarios(self.nodos_grafo.values(),
                                    ignorar_nombre=usuario.nombre)
                nombre = input("Introduce el nombre del "
                               "usuario a agregar: ")
                if nombre in self.nodos_grafo and nombre != usuario.nombre:
                    nodo_agregar = self.nodos_grafo[nombre]
                    nodo_grafo.formar_amistad(nodo_agregar)
                else:
                    print("Nombre inválido")

            elif accion == 'Iniciar Amigo Secreto':
                self.lista_ligada.entregar_regalos()

            elif accion == 'Eliminar Amistad':
                self.print_usuarios(nodo_grafo.amistades)
                nombre = input("Introduce el nombre de la "
                               "amistad que queires eliminar: ")
                if nombre in self.nodos_grafo and nombre != usuario.nombre:
                    nodo_eliminar = self.nodos_grafo[nombre]
                    nodo_grafo.eliminar_amistad(nodo_eliminar)
                else:
                    print("Nombre inválido")

            elif accion == 'Buscar usuario por nivel de fama':
                fama = input("Introduce el nivel de fama para la búsqueda: ")
                if fama.isnumeric():
                    fama = int(fama)
                    usuario_buscado = self.arbol.buscar_nodo(fama)
                    if usuario_buscado is None:
                        print("No hay usuario con esa fama")
                    else:
                        self.print_usuarios([usuario_buscado])
                else:
                    print("Input inválido")
            elif accion == 'Encontrar Famoso más Cercano [BONUS]':
                distancia, famoso = busqueda_famosos(nodo_grafo)
                if famoso:
                    print(f"* Distancia: {str(distancia): ^32s}"
                          + f"|{famoso.usuario.nombre: ^32s} *")
                else:
                    print("El usuario no está conectado a ningún famoso :c")
        print("Hasta luego!")

    @staticmethod
    def print_usuarios(nodos_grafos, ignorar_nombre=""):
        nodos_filtrados = filter(
            lambda x: x.usuario.nombre != ignorar_nombre,
            nodos_grafos
        )
        new_column = False
        print(f"* {'NOMBRE': ^32s}|{'CORREO': ^40s} *"
              f"* {'NOMBRE': ^32s}|{'CORREO': ^40s} *")
        for nodo in nodos_filtrados:
            end = '\n' if new_column else ''
            print(f"* {nodo.usuario.nombre: ^32s}|"
                  f" {nodo.usuario.correo: ^40s} *",
                  end=end)
            new_column = not new_column
        print()

    def recibir_accion(self, acciones: dict):
        print("¿Qué accion deseas hacer?")
        accion = None
        while accion is None:
            self.pretty_print_acciones(acciones)
            respuesta = input('Ingresa el número correspondiente: ')
            if respuesta in acciones:
                return acciones[respuesta]

    @staticmethod
    def acciones_validas(famoso: bool):
        acciones = ['Volver', 'Ver Amistades',
                    'Resumen DCCelebrity',
                    'Buscar usuario por nivel de fama',
                    'Recomendar Amistad',
                    'Iniciar Amigo Secreto']
        if famoso:
            acciones += ['Agregar Amistad', 'Eliminar Amistad']
        else:
            acciones += ['Encontrar Famoso más Cercano [BONUS]']
        return {str(num): accion for num, accion in
                enumerate(acciones, start=0)}

    @staticmethod
    def pretty_print_acciones(acciones: dict):
        for numero, accion in acciones.items():
            print(f" {numero: >3s}.- {accion}")
