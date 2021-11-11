import socket
from cliente import Cliente


if __name__ == "__main__":
    HOST = socket.gethostname()  # "localhost"
    PORT = 47365

    CLIENTE = Cliente(HOST, PORT)
