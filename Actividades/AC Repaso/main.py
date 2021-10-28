
from PyQt5.QtWidgets import QApplication
from frontend.ventana_coccion import VentanaCoccion
from frontend.ventana_pedido import VentanaPedido
from frontend.ventana_armado import VentanaArmado
from backend.backend import DCChef
import sys

app = QApplication([])
backend = DCChef()
ventana_pedido = VentanaPedido()
parrilla = VentanaCoccion(ventana_pedido)
armado = VentanaArmado(parrilla)

armado.senal_agregar_ingrediente.connect(backend.agregar_ingrediente_sandwich)
armado.senal_finalizar_sandwich.connect(backend.finalizar_juego)

parrilla.senal_agregar_hamburguesa.connect(
    backend.agregar_hamburguesa_parrilla
)
parrilla.senal_pasar_armado.connect(backend.empezar_armado)

backend.senal_hamburguesa_agregada.connect(parrilla.agregar_hamburguesa)
backend.senal_hamburguesa_botada.connect(parrilla.eliminar_hamburguesa)
backend.senal_pedido_generado.connect(parrilla.pedido_generado)
backend.senal_hamburguesa_termino_cocerse.connect(parrilla.terminar_cocer)
backend.senal_informar_resultado.connect(armado.mostrar_resultado)
backend.senal_ingrediente_anadido_sandwich.connect(
    armado.agregar_ingrediente_a_hamburguesa
)

# Conectar señales
# senal_coccion_hamburguesa
# senal_comenzo_armado
# senal_botar_hamburguesa
# senal_sacar_hamburguesa
# senal_agregar_hamburguesa
# senal_generar_pedido


ventana_pedido.show()

sys.exit(app.exec_())
