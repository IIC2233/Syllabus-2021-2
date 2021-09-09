import parametros as p
from cargar_datos import cargar_atracciones, cargar_personas
from parque import Parque


if __name__ == "__main__":
    # Cargado de datos
    lista_personas = cargar_personas(p.RUTA_PERSONAS)
    dic_atracciones = cargar_atracciones(p.RUTA_ATRACCIONES)
    # dic_atracciones = cargar_atracciones(p.RUTA_ATRACCIONES_BONUS)  # Descomentar para BONUS

    # Instanciar el parque, con los datos cargados
    parque = Parque(lista_personas, dic_atracciones)

    # Inicio del juego
    parque.iniciar_dia()
