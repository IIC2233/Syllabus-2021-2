import json
from os import path
from parametros import PATH_USUARIOS


def cargar_usuarios():
    with open(path.join(*PATH_USUARIOS), 'rt', encoding='utf-8') as file:
        dict_usuarios = json.load(file)['USERS']

    return dict_usuarios
