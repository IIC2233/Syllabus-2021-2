from os.path import join


RUTA_TITULO = join('ascii', 'titulo.txt')

RAIZ_ARCHIVOS = 'data'

RUTA_DATOS = {
    'fotos': join(RAIZ_ARCHIVOS, 'fotos'),
    'gifs': join(RAIZ_ARCHIVOS, 'gifs'),
    'sonidos': join(RAIZ_ARCHIVOS, 'sonidos'),
}

IGNORADOS = {
    '.gitkeep',
    '.DS_Store'
}
