import sys
from parametros import HOST, PORT
from servidor import Servidor


if __name__ == "__main__":
    servidor = Servidor(HOST, PORT)

    try:
        while True:
            input("[Presione Ctrl+C para cerrar el servidor]")
    except KeyboardInterrupt:
        print("Cerrando servidor...")
        servidor.socket_servidor.close()
        sys.exit()
