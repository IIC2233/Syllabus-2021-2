import os


# Teclas
TECLA_ARRIBA = "w"
TECLA_IZQUIERDA = "a"
TECLA_ABAJO = "s"
TECLA_DERECHA = "d"

# Parámetros VentanaInicio:
WINDOW_SIZE_ARGS = (100, 100, 300, 300)

# Parámetros LogicaInicio
CONTRASENA = "IIC2233"

# Parámetros VentanaJuego:
MIN_X = 0
MAX_X = 800
MIN_Y = 220
MAX_Y = 670
Y_INICIAL = (MAX_Y + MIN_Y) // 2
LARGO_COBRA = 8
WIDTH_COBRA = 50
HEIGHT_COBRA = 50
POS_INICIO_ITEM = (0, 225, 10, 10)

# Parámetros LogicaJuego
RANGO_APARICION_ITEM = 15
VELOCIDAD = 1
MOVIMIENTO = 55

# Parámetros generales y paths:
RUTA_UI_VENTANA_JUEGO = os.path.join("frontend", "assets", "ventana_juego.ui")
RUTA_LOGO = os.path.join("frontend", "assets", "Logo.png")
RUTA_ICONO = os.path.join("frontend", "assets", "logo_cobreloa_icon.ico")
RUTA_IMAGEN = os.path.join("frontend", "assets", "imagen_sad.png")
RUTA_MAPA = os.path.join("frontend", "assets", "Arena.jpg")
RUTA_COBRA_CABEZA = os.path.join("frontend", "assets", "sprites",
                                 "cabeza_cobra.png")
RUTA_COBRA_CUERPO = os.path.join("frontend", "assets", "sprites",
                                 "cuerpo_cobra.png")
RUTA_ITEM = os.path.join("frontend", "assets", "comida.png")
RUTA_IMAGEN_SAD = os.path.join("frontend", "assets", "imagen_sad.png")

# Extras
stylesheet_boton = """QPushButton {
    background-color: #fd9500;
    border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: beige;
    font: bold 14px;
    min-width: 4em;
    padding: 6px;
    color: white;
}
QPushButton:pressed {
    background-color: rgb(144, 74, 16);
    border-style: inset;
}"""
