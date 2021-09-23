from shopper import Shopper
from tienda import Tienda
import os


def cargar_shoppers(path):
    """
    Carga los shoppers del archivo entregado en path
    Retorna una lista de objetos (Shopper)
    """

    shoppers = []

    with open(path, 'r', encoding='utf-8') as archivo:
        for line in archivo.readlines():
            line = line.rstrip().split(',')
            shopper = Shopper(line[0], int(line[1]))
            shoppers.append(shopper)
    return shoppers


def cargar_tiendas(path):
    """
    Carga las tiendas del archivo entregado en path
    Retorna un diccionario con llave nombre de la tienda y
    valor un objeto Tienda
    """

    tiendas = {}

    with open(path, 'r', encoding='utf-8') as archivo:
        for line in archivo.readlines():
            line = line.rstrip().split(',')
            tienda = Tienda(line[0])
            tiendas[tienda.nombre] = tienda
    return tiendas


def cargar_pedidos(path):
    """
    Carga los pedidos del archivo entregado en path
    Retorna una lista de listas con la información de un pedido
    """

    pedidos = []
    with open(path, 'r', encoding='utf-8') as archivo:
        for line in archivo.readlines():
            line = line.rstrip().split(',')
            pedidos.append(line)

    return pedidos


if __name__ == '__main__':
    shoppers = cargar_shoppers(os.path.join("datos", "shoppers.csv"))
    for shopper in shoppers:
        print(shopper.nombre, shopper.velocidad)
    pedidos = cargar_pedidos(os.path.join("datos", "pedidos.csv"))
    for pedido in pedidos:
        print(pedido)
