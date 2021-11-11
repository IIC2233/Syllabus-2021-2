import socket
from os.path import join


HOST = socket.gethostname()
PORT = 47365

RAIZ_ARCHIVOS = 'data'
RUTA_DATOS = {
    'fotos': join(RAIZ_ARCHIVOS, 'fotos'),
    'gifs': join(RAIZ_ARCHIVOS, 'gifs'),
    'sonidos': join(RAIZ_ARCHIVOS, 'sonidos'),
}

CAPACIDAD_MAXIMA = 4*(10**9)

FORMATOS = {
    'fotos': 'png',
    'gifs': 'gif',
    'sonidos': 'wav'
}

IGNORADOS = {
    '.gitkeep',
    '.DS_Store'
}
