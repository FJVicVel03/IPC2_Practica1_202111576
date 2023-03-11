import os
import xml.etree.ElementTree as ET

def cargar_archivo_xml():
    archivo = input("Ingrese la ruta del archivo XML: ")
    while not os.path.isfile(archivo):
        archivo = input("Archivo no encontrado. Ingrese una ruta válida: ")
    return archivo

def obtener_archivo_ordenado(archivo):
    tree = ET.parse(archivo)
    root = tree.getroot()

    # Ordenar las plataformas por su código
    plataformas = root.find('ListaPlataformas')
    plataformas[:] = sorted(plataformas, key=lambda child: child.find('codigo').text)

    # Ordenar los juegos por su nombre y luego por su código
    juegos = root.find('ListadoJuegos')
    juegos[:] = sorted(juegos, key=lambda child: (child.find('nombre').text, child.find('codigo').text))

    # Ordenar las plataformas en cada juego por su código
    for juego in juegos:
        plataformas_juego = juego.find('Plataformas')
        plataformas_juego[:] = sorted(plataformas_juego, key=lambda child: child.find('codigo').text)

    return ET.tostring(root, encoding='unicode')

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
            print("Archivo cargado exitosamente.")
        elif opcion == '2':
            if 'archivo' not in locals():
                print("Primero cargue un archivo XML.")
            else:
                archivo_ordenado = obtener_archivo_ordenado(archivo)
                nombre_archivo = input("Ingrese el nombre del nuevo archivo: ")
                with open(nombre_archivo, 'w') as f:
                    f.write(archivo_ordenado)
                print("Archivo ordenado creado exitosamente.")
        elif opcion == '3':
            print("Adiós.")
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")

if __name__ == '__main__':
    main()
