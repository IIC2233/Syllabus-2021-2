from random import sample
from hotel import Hotel
from cargar_datos import cargar_mascotas
import parametros as p


def menu_inicio():
    while True:
        print(" MENU DE INICIO ".center(80, "="))
        print("Selecciona una opción")
        print("[1] Ingresar")
        print("[0] Salir :c")

        opcion = input("Indique su opción: ")

        if opcion == "1": # Ingresar
            hotel = Hotel()
            lista_mascotas = cargar_mascotas('mascotas.csv')
            mascotas_elegidas = sample(lista_mascotas, p.MASCOTAS_INICIALES)
            hotel.recibir_mascota(mascotas_elegidas)
            menu_mascotas(hotel)

        elif opcion == "0": # Salir
            print("Vuelve pronto!")
            break

        else:
            print("La opción ingresada no es válida")

def menu_mascotas(hotel):
    while hotel.funcionando:
        print(" MENU DE MASCOTAS ".center(80, "="))
        print("Selecciona una mascota para cuidar") 
        contador = 1
        for mascota in hotel.mascotas:
            print(f"[{contador}] {mascota.nombre} ")
            contador += 1

        op = input("Número de mascota: ")

        if 0 < int(op) <= len(hotel.mascotas):
            mascota = hotel.mascotas[int(op) - 1]
            menu_cuidados(mascota, hotel)

        else:
            print("La opción ingresada no es válida")


def menu_cuidados(mascota, hotel):
    while hotel.funcionando:
        print(" MENU DE CUIDADOS ".center(80, "="))     
        print(f"{mascota}")
        print(f"¿Qué quieres hacer con {mascota.nombre}?")
        print("[1] Pasear")
        print("[2] Alimentar")
        print("[d] Pasar de día")
        print("[-1] Volver atrás")
        print("\n")
        hotel.imprimir_estado()

        op = input("Indique su opción: ")

        if op == "-1": # Volver atrás
            menu_mascotas(hotel)
        
        elif op == "d":  # Pasar de día
            hotel.nuevo_dia()

        if op == "1" or op == "2" or op == "3":
            if hotel.revisar_energia() == True:
                if op == "1":  # Pasear
                    hotel.pasear_mascota(mascota)
                elif op == "2":  # Alimentar
                    hotel.alimentar_mascota(mascota)
            else:
                print("No hay energía suficiente :(")

        else:
            print("La opción ingresada no es válida")


if __name__ == '__main__':
    menu_inicio()
