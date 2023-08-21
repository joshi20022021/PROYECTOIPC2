import xml.etree.ElementTree as ET
from cargar import cargar


def main():
    while True:
        print("=== Menú Principal ===")
        print("1. Cargar archivo")
        print("2. Procesar archivo")
        print("3. Escribir archivo salida")
        print("4. Mostrar datos del estudiante")
        print("5. Generar gráfico")
        print("6. Inicializar sistema")
        print("7. Salida")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            cargar()
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            pass 
        elif opcion == "6":
            pass 
        elif opcion == "7":
            exit()
        else:
            print("Opción no válida. Inténtalo nuevamente.")

if __name__ == "__main__":
    main()