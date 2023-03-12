import xml.etree.ElementTree as ET


def obtener_archivo_ordenado(archivo):
    tree = ET.parse(archivo)
    root = tree.getroot()

    # Ordenar las plataformas por su código
    plataformas = root.find('ListaPlataformas')
    plataformas_sorted = sorted(plataformas, key=lambda child: child.find('codigo').text)
    plataformas_pila = []
    for plataforma in plataformas_sorted:
        plataformas_pila.append(plataforma)
    root.remove(plataformas)
    for plataforma in reversed(plataformas_pila):
        root.insert(0, plataforma)

    # Ordenar los juegos por su código
    juegos = root.find('ListadoJuegos')
    juegos_sorted = sorted(juegos, key=lambda child: child.find('codigo').text)
    juegos_pila = []
    for juego in juegos_sorted:
        juegos_pila.append(juego)
    root.remove(juegos)
    for juego in reversed(juegos_pila):
        root.insert(0, juego)

    # Ordenar las plataformas en cada juego por su código
    for juego in juegos_pila:
        plataformas_juego = juego.find('Plataformas')
        plataformas_juego_sorted = sorted(plataformas_juego, key=lambda child: child.find('codigo').text)
        plataformas_juego_pila = []
        for plataforma in plataformas_juego_sorted:
            plataformas_juego_pila.append(plataforma)
        juego.remove(plataformas_juego)
        for plataforma in reversed(plataformas_juego_pila):
            juego.insert(0, plataforma)
            
    return ET.tostring(root, encoding='unicode')

