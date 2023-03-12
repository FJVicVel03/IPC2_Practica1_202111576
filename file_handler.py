import os


def cargar_archivo(archivo):
    contenido = archivo
    return contenido


def guardar_archivo(nombre_archivo, contenido):
    with open(nombre_archivo, 'w') as f:
        f.write(contenido)
