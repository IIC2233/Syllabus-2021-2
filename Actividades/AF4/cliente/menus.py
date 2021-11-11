"""
Este modulo implementa todos los menus que utiliza el usuario para interactuar
con el cliente. Los menus usan un kwarg 'fail' para saber si el usuario
introdujo una opcion valida.
"""
from os.path import join

from archivos import archivo_a_bytes, leer_data_local


def menu_inicio(fail=False):
    """
    Esta funcion se encarga del menu principal del programa, imprime las
    opciones para el usuario y luego el cliente llama a las funciones
    correspondientes.
    """
    # Usamos un diccionario de mensajes para el servidor
    opciones = {
        "0": "salir",
        "1": "explorar",
        "2": "almacenamiento",
        "3": "subir",
        "4": "descargar"
    }
    # Imprimimos la interfaz
    print("=< Menu inicio >=\n")
    print(
        "[1] Explorar nube\n"
        "[2] Almacenamiento Disponible\n"
        "[3] Subir Archivo\n"
        "[4] Descargar Archivo\n"
        "\n[0] Salir"
    )
    # Si hubo un error imprimimos el mensaje correspondiente
    if fail:
        print("Debes ingresar una opción válida!")
    else:
        print()
    seleccion = input()
    if seleccion not in opciones:
        # Si la seleccion no es valida pedimos de nuevo el input al usuario
        return menu_inicio(fail=True)
    return opciones[seleccion]


def menu_subida(fail=False):
    """
    Maneja la logica de la subida de archivos
    """
    print("=" * 40)
    print("Subida de Archivos".center(40))
    print("=" * 40)
    print()
    opciones = {
        "0": "volver",
        "1": "fotos",
        "2": "gifs",
        "3": "sonidos",
    }
    print("="*10 + "  <<< Menu subida >>>  " + "="*10 + "\n")
    print(
        "Eliga el tipo de archivo a mandar:\n"
        "[1] Fotos\n"
        "[2] Gifs\n"
        "[3] Sonidos\n"
        "\n[0] Volver"
    )
    seleccion = input()
    if seleccion not in opciones:
        return menu_subida(fail=True)
    tipo = opciones[seleccion]
    if tipo == 'volver':
        archivo, nombre = None, None
    else:
        nombre_archivo = menu_seleccion_archivo(tipo, 'subida')
        if nombre_archivo == "Volver":
            # Si el usuario decidio volver en el menu_seleccion_archivo
            return menu_subida(fail=False)

    if archivo:
        ruta = join('data', tipo, nombre_archivo)
        nombre = nombre_archivo.split(".")[0]
        archivo = archivo_a_bytes(ruta)
    return archivo, tipo, nombre


def menu_seleccion_archivo(categoria, operacion, fail=False):
    """
    Recibe una categoria de archivos (fotos, gifs, sonidos) y le permite al
    usuario seleccionar un archivo

    El argumento operacion puede tomar los valores "subida" o "descarga"
    """
    if not categoria:
        # Si se le entrega una lista vacia desde menu_descarga
        return
    print("="*10 + "  Selección de archivos  " + "="*10 + "\n")
    opciones = {"0": "Volver"}
    if operacion == 'subida':
        archivos = leer_data_local().get(categoria)
    elif operacion == 'descarga':
        archivos = categoria        # esto habria que arreglarlo
    if archivos:  # Es posible que este vacio
        for index, nombre_archivo in enumerate(archivos):
            print(f"[{index + 1}]: {nombre_archivo}")
            opciones[str(index + 1)] = nombre_archivo
    print("\n[0]: Volver")
    if fail:
        print("Debes ingresar una opción válida!")
    else:
        print()
    seleccion = input()
    if seleccion not in opciones:
        return menu_seleccion_archivo(categoria, fail=True)
    return opciones[seleccion]


def menu_descarga(archivos, fail=False):
    """
    Menu maneja la descarga de archivos, se ingresa cuando se explora
    archivos en modo descarga.
    """
    print("=" * 40)
    print("Descarga de archivos".center(40))
    print("=" * 40)
    print()
    print("="*10 + "  <<< Menu descarga >>>  " + "="*10 + "\n")
    opciones = {"0": "Volver"}
    for index, tipo_archivo in enumerate(archivos['contenido']):
        print(f"[{index + 1}]: {tipo_archivo}")
        opciones[str(index + 1)] = tipo_archivo
    print("\n[0]: Volver")
    if fail:
        print("Debes ingresar una opción válida!")
    else:
        print()
    seleccion = input()
    if seleccion not in opciones:
        return menu_descarga(archivos, fail=True)
    tipo_archivo = opciones[seleccion]
    categoria = archivos['contenido'].get(tipo_archivo)
    nombre_archivo = menu_seleccion_archivo(categoria, 'descarga')
    if nombre_archivo == 'Volver':
        return menu_descarga(archivos, fail=False)
    return tipo_archivo, nombre_archivo
