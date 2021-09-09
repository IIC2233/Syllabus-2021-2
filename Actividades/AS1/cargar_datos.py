from personas import Adulto, Nino
from atracciones import (
    AtraccionAdrenalinica, AtraccionFamiliar, AtraccionAcuatica,
    MontanaAcuatica
)
from bonus import AtraccionTerrorifica, CasaEmbrujada
import parametros as p


def cargar_personas(ruta):
    lista_personas = []
    with open(ruta, "r", encoding="UTF-8") as archivo:
        for linea in archivo.readlines()[1:]:
            linea = linea.strip().split(",")
            if int(linea[1]) <= 13:
                class_ = Nino
                type_ = str
            else:
                class_ = Adulto
                type_ = int
            nueva_persona = class_(
                linea[0], int(linea[1]), bool(
                    int(linea[2])), linea[3].split(";"), type_(linea[4]),
            )
            lista_personas.append(nueva_persona)
    return lista_personas


def cargar_atracciones(ruta):
    dict_atracciones = {
        "Adrenalinica": AtraccionAdrenalinica,
        "Familiar": AtraccionFamiliar,
        "Acuatica": AtraccionAcuatica,
        "Terrorifica": AtraccionTerrorifica,
        "CasaEmbrujada": CasaEmbrujada,
        "MontanaAcuatica": MontanaAcuatica
    }
    atracciones = {}
    with open(ruta, "r", encoding="UTF-8") as archivo:
        for linea in archivo.readlines()[1:]:
            linea = linea.strip().split(",")
            if linea[1] in ["Adrenalinica", "Terrorifica", "CasaEmbrujada"]:
                nueva_atraccion = dict_atracciones[linea[1]](
                    linea[0], int(linea[2]), p.SALUD_NECESARIA,
                )
            elif linea[1] == "MontanaAcuatica":
                nueva_atraccion = dict_atracciones[linea[1]](
                    linea[0], int(linea[2]), p.SALUD_NECESARIA, 3,
                )
            else:
                nueva_atraccion = dict_atracciones[linea[1]](
                    linea[0], int(linea[2]),
                )
            atracciones[nueva_atraccion.nombre] = nueva_atraccion
    return atracciones
