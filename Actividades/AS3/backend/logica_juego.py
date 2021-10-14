import random

from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QRect

import parametros as p


class LogicaJuego(QObject):

    senal_perder = pyqtSignal()
    senal_actualizar = pyqtSignal(dict)

    def __init__(self, cobra):
        super().__init__()
        self.puntaje = 0
        self.cobra = cobra
        self.items_recolectados = 0
        self.instanciar_timer()
        self.pos_item = QRect(*p.POS_INICIO_ITEM)

    def instanciar_timer(self):
        # COMPLETAR
        pass

    def iniciar_juego(self):
        # COMPLETAR
        pass

    def detener_juego(self):
        self.timer.stop()

    def timer_tick(self):
        self.subtick += 1
        choca = self.cobra.avanzar()
        if choca:
            self.detener_juego()
            self.senal_perder.emit()
        elif self.colision_con_bordes():
            self.senal_perder.emit()
            self.detener_juego()
        elif self.recolecta_item():
            self.items_recolectados += 1
            self.elegir_posicion_item()
        if self.subtick == p.RANGO_APARICION_ITEM:
            self.subtick = 0
            self.elegir_posicion_item()
        self.senal_actualizar.emit({
            "pos_cabeza": self.cobra.bloques[-1],
            "direccion": self.cobra.direccion,
            "items": self.items_recolectados,
            "new_item": True,
            "pos_item": self.pos_item,
        })

    def colision_con_bordes(self):
        choca = False
        if not (p.MIN_X <= self.cobra.bloques[-1].x()
                <= p.MAX_X - p.WIDTH_COBRA):
            choca = True
        if not (p.MIN_Y <= self.cobra.bloques[-1].y()
                <= p.MAX_Y - p.HEIGHT_COBRA):
            choca = True
        return choca

    def recolecta_item(self):
        return self.cobra.bloques[-1].intersects(self.pos_item)

    def elegir_posicion_item(self):
        """llamado cuando se atrapa un item o pasan 10 segundos sin atraparse
        retorna el QRect en que se encontrará, cuidando de que no se intersecte
        con la cobra
        """
        self.subtick = 0
        choca = True
        rect = None
        while choca:
            pos_x = random.randint(p.MIN_X, p.MAX_X - p.WIDTH_COBRA)
            pos_y = random.randint(p.MIN_Y, p.MAX_Y - p.HEIGHT_COBRA)
            rect = QRect(pos_x, pos_y, p.WIDTH_COBRA, p.HEIGHT_COBRA)
            choca = False
            for bloque in self.cobra.bloques:
                if rect.intersects(bloque):
                    choca = True
                    break
        self.pos_item = rect


class DCCobra(QObject):

    def __init__(self):
        super().__init__()
        self.direccion = "R"
        self.contrario = {"R": "L", "L": "R", "U": "D", "D": "U"}
        self.bloques = [
            QRect(55 * i, 500, p.WIDTH_COBRA, p.HEIGHT_COBRA)
            for i in range(p.LARGO_COBRA)
        ]

    def cambiar_direccion(self, nueva_direccion):
        if nueva_direccion.upper() in "URDL":
            if self.direccion != self.contrario[nueva_direccion]:
                self.direccion = nueva_direccion

    def avanzar(self):
        if self.direccion == "R":
            delta = (p.MOVIMIENTO, 0)
        elif self.direccion == "L":
            delta = (-1 * p.MOVIMIENTO, 0)
        elif self.direccion == "U":
            delta = (0, -1 * p.MOVIMIENTO)
        else:
            delta = (0, p.MOVIMIENTO)
        self.bloques = self.bloques[1:]
        cabeza_nueva = self.bloques[-1].translated(*delta)
        self.bloques.append(cabeza_nueva)
        choca = self.revisar_autocolision()
        return choca

    def revisar_autocolision(self):
        cabeza = self.bloques[-1]
        for rect in self.bloques[:-3]:
            if cabeza.intersects(rect):
                return True
        return False
