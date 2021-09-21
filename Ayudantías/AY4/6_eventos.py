# Este codigo esta inspirado en el ejemplo de eventos de el siguiente Notebook
# https://github.com/IIC2233/contenidos/blob/main/semana-05/2-concurrencia.ipynb

import threading
import time


def primer_logeado(nombre) -> None:

    print(f"	{nombre} se conecto")

    print(f"	{nombre} hizo git pull")

    print(f"	{nombre} trabajando ...")

    time.sleep(2)

    print(f"	{nombre} termino de trabajar y hizo git add y commit")

    print(f"	{nombre} pusheo los datos en {time.time():.6f}")
    # Avisamos que el primer usuario ya está cargado
    senal_usuario_uno_termino_trabajar.set()


def segundo_logeado(nombre) -> None:

    print(f"  	{nombre} se conecto")

    print(f"  	{nombre} esta esperando a que termine su compañero")

    senal_usuario_uno_termino_trabajar.wait()

    print(f"  	{nombre} hizo git pull")

    print(f"  	{nombre} trabajando ...")

    time.sleep(2)

    print(f" 	{nombre} termino de trabajar y hizo git add y commit")

    print(f"  	{nombre} pusheo todo en {time.time():.6f}")


if __name__ == "__main__":
    print("Empezando el día en el repositorio 'Avanzadamemes'")
    senal_usuario_uno_termino_trabajar = threading.Event()

    user1 = threading.Thread(target=primer_logeado, args=("gatochico",))
    user2 = threading.Thread(target=segundo_logeado, args=("fdelrio89",))

    user1.start()
    user2.start()

    user1.join()
    user2.join()

    print("Se termino el dia :)")
