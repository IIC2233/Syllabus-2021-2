from app import DCComidApp
from cargar_datos import cargar_shoppers, cargar_pedidos, cargar_tiendas
import os


def iniciar_shoppers(shoppers):
    for shopper in shoppers:
        shopper.start()


def detener_shoppers(shoppers):
    for shopper in shoppers:
        shopper.termino_jornada = True


def esperar_shoppers(shoppers):
    for shopper in shoppers:
        shopper.join()


def iniciar_tiendas(tiendas):
    for tienda in tiendas.values():
        tienda.start()


def detener_tiendas(tiendas):
    for tienda in tiendas.values():
        tienda.abierta = False
        tienda.join()


if __name__ == '__main__':

    shoppers = cargar_shoppers(os.path.join("datos", "shoppers.csv"))
    tiendas = cargar_tiendas(os.path.join("datos", "tiendas.csv"))
    pedidos = cargar_pedidos(os.path.join("datos", "pedidos.csv"))

    app = DCComidApp(shoppers, tiendas, pedidos)

    print(" INICIANDO SIMULACIÓN ".center(80, "="))
    app.start()
    iniciar_tiendas(tiendas)
    iniciar_shoppers(shoppers)

    app.join()
    detener_shoppers(shoppers)
    detener_tiendas(tiendas)
    esperar_shoppers(shoppers)
    print(" SIMULACIÓN TERMINADA ".center(80, "="))
