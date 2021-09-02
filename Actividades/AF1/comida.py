class Comida:
	def __init__(self, nombre, calorias, probabilidad_vencer):
		self.nombre = nombre
		self.calorias = calorias
		self.probabilidad_vencer = probabilidad_vencer

	def __str__(self):
		return f'{self.nombre} con energia: {self.calorias}.'