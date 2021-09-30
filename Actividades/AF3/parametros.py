import os


# Rutas archivos
RUTA_USUARIOS = os.path.join("datos", "usuarios.csv")
RUTA_PELICULAS = os.path.join("datos", "peliculas.csv")

# Rutas arte
RUTAS_ARTE = {
    "Deportes": os.path.join("images", "deportes.txt"),
    "Arte": os.path.join("images", "arte.txt"),
    "Ciencia Ficción": os.path.join("images", "sci_fi.txt"),
    "Fantasía": os.path.join("images", "fantasia.txt"),
    "Comedia": os.path.join("images", "comedia.txt"),
    "Acción": os.path.join("images", "accion.txt"),
}

# Categorias peliculas
CATEGORIAS = (
    "Deportes",
    "Arte",
    "Ciencia Ficción",
    "Fantasía",
    "Comedia",
    "Acción",
)

# Constantes adicionales
LARGO_LISTA_REPRODUCCION = 20
TIEMPO_REPRODUCCION = 0.3
