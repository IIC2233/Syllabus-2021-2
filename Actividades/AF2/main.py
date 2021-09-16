# NO DEBES MODIFICAR ESTE ARCHIVO

from cargar_archivos import cargar_invitades, cargar_total_asistentes
from verificar_invitades import (
    corregir_edad,
    corregir_pase_movilidad,
    corregir_mail,
    dar_alerta_colado
)
from permitir_entrada import entregar_invitados


if __name__ == "__main__":

    diccionario_invitades = cargar_invitades("data/lista_oficial.csv")
    nombres_asistentes = cargar_total_asistentes("data/asistentes.txt")

    print("Revisando posibles errores en los datos de les invitades...\n")
    for ayudante in diccionario_invitades.values():
        corregir_edad(ayudante)
        corregir_pase_movilidad(ayudante)
        corregir_mail(ayudante)

    print("Revisando la lista de invitados...\n")
    for nombre_asistente in nombres_asistentes:
        dar_alerta_colado(nombre_asistente, diccionario_invitades)

    print("Solo los invitados sanos y no colados podrán entrar!\n")
    acceso = entregar_invitados(diccionario_invitades)

    print(54 * '*')
    print('¡WUJUUU! ¡Veamos quienes pudieron entrar al DCCarrete!\n')
    print(5 * '-' + ' INVITAD@S ACEPTAD@S ' + 5 * '-')
    for ayudante in acceso:
        ayudante = ayudante.center(29)
        print('|' + ayudante + '|')
    print(31 * '-')
    print('\nDISFRUTA EL DCCARRETE!')
