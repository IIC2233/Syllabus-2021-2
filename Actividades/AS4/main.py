from cargar_usuarios import cargar_usuarios
from dccelebrity import DCCelebrity

if __name__ == "__main__":
    dccelebrity = DCCelebrity()
    dccelebrity.crear_red(cargar_usuarios())
    dccelebrity.run()
