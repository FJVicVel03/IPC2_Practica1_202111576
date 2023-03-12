import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os
from xml_parser import obtener_archivo_ordenado
from file_handler import cargar_archivo, guardar_archivo


def cargar_archivo_xml():
    root = tk.Tk()
    archivo = filedialog.askopenfilename(title="Seleccionar archivo XML")
    while not os.path.isfile(archivo):
        archivo = filedialog.askopenfilename(title="Archivo no encontrado. Seleccionar un archivo XML válido")
    root.withdraw()
    return cargar_archivo(archivo)


def main():
    print("Bienvenido al programa de ordenamiento de archivos XML")
    while True:
        print("Menú:")
        print("1. Cargar archivo XML")
        print("2. Obtener nuevo archivo ordenado")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            archivo = cargar_archivo_xml()
            if archivo:
                print("Archivo cargado exitosamente.")
        elif opcion == '2':
            if archivo is None:
                print("Primero cargue un archivo XML.")
            else:
                archivo_ordenado = obtener_archivo_ordenado(archivo)
                nombre_archivo = input("Ingrese el nombre del nuevo archivo: ")
                guardar_archivo(nombre_archivo, archivo_ordenado)
                print("Archivo ordenado creado exitosamente.")
        elif opcion == '3':
            print("Adiós.")
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")


if __name__ == '__main__':
    main()
