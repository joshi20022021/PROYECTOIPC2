import xml.etree.ElementTree as ET
from Lista_Datos import ListaDatos
from lista_Senal import ListaSenal
from Datos import Datos
from senal import Senal

def cargar():
    try:
        archivo = input("\nIngrese la ruta del archivo XML: ")

        tree = ET.parse(archivo)
        root = tree.getroot()

        lista_senal_temporal = ListaSenal()

        for senal in root.findall('senal'):
            senal_nombre = senal.get('nombre')
            tiempo_senal = senal.get('t')
            amplitud_senal = senal.get('A')

            lista_datos_temporal = ListaDatos()
            lista_datos_patrones_temporal = ListaDatos()

            for dato in senal.findall('dato'):
                tiempo_dato = dato.get('t') or '0'
                amplitud_dato = dato.get('A') or '0'
                valor = dato.text or '0'

                nuevo_dato = Datos(tiempo_dato, amplitud_dato, valor)
                lista_datos_temporal.agregar(nuevo_dato)

                if tiempo_dato != '' and amplitud_dato != '':
                    nuevo_patron = Datos(tiempo_dato, amplitud_dato, valor)
                    lista_datos_patrones_temporal.agregar(nuevo_patron)

            nueva_senal = Senal(senal_nombre, tiempo_senal, amplitud_senal, lista_datos_temporal, lista_datos_patrones_temporal)
            lista_senal_temporal.agregar(nueva_senal)

        lista_senal_temporal.imprimir_listaSenal()
        lista_senal_temporal.grafica_lista_patrones()

    except FileNotFoundError:
        print("\nNo se pudo cargar el archivo XML, verifique la ruta ingresada")

# Call the function
cargar()