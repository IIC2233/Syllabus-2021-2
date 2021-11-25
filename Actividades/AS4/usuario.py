from parametros import COTA_FAMA


class Usuario:

    def __init__(self, nombre, correo, fama):
        """
        Recibe un nombre, correo y fama e inicializa un Usuario
        """
        self.nombre = nombre
        self.correo = correo
        self.fama = fama

    @property
    def es_famoso(self):
        return self.fama > COTA_FAMA

    def __repr__(self):
        return self.nombre
