import json
import socket
import threading

import menus
from archivos import iniciar_sistema, leer_data_local, guardar_archivo


class Cliente:

    def __init__(self, host, port):
        iniciar_sistema()
        self.a_descargar = None
        self.descarga_actual = bytearray()
        self.ruta_descarga_actual = None
        self.host = host
        self.port = port
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.evento_prints = threading.Event()
        self.evento_prints.set()

        try:
            self.conectar_al_servidor()
            self.escuchar()
            self.recibir_input()
        except ConnectionError:
            self.salir()

    def conectar_al_servidor(self):
        # Completar
        pass

    def escuchar(self):
        # Completar
        pass

    def thread_escuchar(self):
        # Completar
        pass

    def enviar(self, msg):
        # Completar
        pass

    def recibir_input(self):
        # Inicia el thread que se encarga de manejar el input
        thread = threading.Thread(target=self.thread_recibir_input, daemon=True)
        thread.start()

    def manejar_comando(self, recibido):
        """
        Función que se llama al recibir un comando por parte del servidor.
        Se encarga de extraer los argumentos del mensaje y llamar a los
        métodos correspondientes.
        """
        # Extraemos el comando
        comando = recibido.get("comando")
        print()
        print("="*40)
        # Utilizamos if/elif/else para llamar al comando pertinente
        if comando == "explorar":
            self.explorar_archivos(recibido["argumentos"])

        elif comando == "almacenamiento":
            msg = recibido["argumentos"].get("contenido")
            print("Almacenamiento ocupado".center(40), '\n' + '=' * 40 + '\n')
            print(msg, '\n')

        elif comando == "archivo":
            print("Guardando archivo")
            self.descarga_actual = bytearray()
            self.ruta_descarga_actual = recibido["argumentos"]["ruta"]

        elif comando == "chunk":
            parametros = recibido["argumentos"]
            chunk, largo = parametros["contenido"], parametros.get("largo", 0)
            chunk = bytes.fromhex(chunk)
            chunk = chunk[:largo]  # eliminamos el padding
            self.descarga_actual.extend(chunk)
            if largo < 8000:
                # El ultimo chunk será menor a 8000
                guardar_archivo(
                    self.descarga_actual, self.ruta_descarga_actual
                )
                self.descarga_actual = bytearray()

        elif comando == "exito":
            print("Operación realizada con éxito")

        elif comando == "explorar_descargar":
            self.explorar_archivos(recibido["argumentos"], True)

        elif comando == "error":
            print("Error en la operacion")
            print(recibido["argumentos"]["mensaje"])

        # Si no estamos en proceso de descarga, le permitimos al cliente
        # continuar con el programa
        if comando != 'archivo':
            if comando != 'chunk' or not self.descarga_actual:
                self.evento_prints.set()

    def thread_recibir_input(self):
        """
        Captura el input del usuario.

        Lee mensajes desde el terminal y después se pasan a `self.enviar()`.
        """
        self.evento_prints.wait()
        opcion = menus.menu_inicio()
        msg = {"comando": opcion, "argumentos": dict()}

        if opcion == "salir":
            return self.salir()

        elif opcion == "subir":
            archivo, tipo, nombre = menus.menu_subida()
            if archivo:
                msg["argumentos"] = {
                    "contenido": archivo.hex(),
                    "tipo": tipo,
                    "nombre": nombre
                }

        elif opcion == "descargar":
            solicitud_descarga = {
                "comando": "explorar_descargar",
            }
            self.enviar(solicitud_descarga)

            # Esperamos que el cliente elija el archivo a descargar
            self.evento_prints.wait()
            tipo_a_descargar, nombre_a_descargar = self.a_descargar
            if tipo_a_descargar != 'Volver':
                msg["argumentos"] = {
                    "tipo": tipo_a_descargar,
                    "nombre": nombre_a_descargar
                }
        sin_argumento = ["explorar", "almacenamiento"]
        if msg["argumentos"] or msg["comando"] in sin_argumento:
            self.enviar(msg)
        self.recibir_input()

    @staticmethod
    def codificar_mensaje(mensaje):
        """
        Serializa el mensaje a enviar a un json.
        """
        try:
            mensaje_json = json.dumps(mensaje)
            mensaje_bytes = mensaje_json.encode()
            return mensaje_bytes
        except json.JSONDecodeError:
            print('No se pudo codificar el mensaje.')

    @staticmethod
    def decodificar_mensaje(msg_bytes):
        """
        Deserializa los bytes recibidos, devolviendo un diccionario a partir
        del json procesado.
        """
        try:
            mensaje = json.loads(msg_bytes)
            return mensaje
        except json.JSONDecodeError:
            print('No se pudo decodificar el mensaje.')
            return dict()

    def salir(self):
        print("Conexión terminada.")
        self.socket_cliente.close()
        exit()

    def explorar_archivos(self, recibido, descargar=False):
        """
        Función que imprime los archivos recibidos del servidor, cuando
        se quiere ver los archivos en la nube o descargar alguno
        """
        if not descargar:
            print("Archivos".center(40))
            print("="*40)
            print()
        data = recibido.get("contenido")
        # En el caso que se esté explorando para descargar, abrimos
        # el menu correspondiente
        if descargar:
            self.a_descargar = menus.menu_descarga(recibido)
        else:
            local = leer_data_local()
            for seccion in data:
                ast = (30 - len(seccion)) // 2
                texto = "*"*ast + f"   {seccion.capitalize()}   " + "*"*ast
                print(texto.center(40))
                print()
                dir_ = data[seccion]
                for nombre in dir_:
                    tick = "[ ]"
                    if nombre in local[seccion]:
                        tick = "[*]"
                    espacio = " "*(30-len(nombre))
                    print(f'  - {nombre}{espacio}{tick}')
                print()
