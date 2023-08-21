from .NodoDatos import NodoDatos
import os
import sys

class ListaDatos:
    def __init__(self):
        self.cabeza = None
        self.contador_datos = 0
        
    def agregar(self, dato):
        if self.cabeza is None:
            self.cabeza = NodoDatos(dato=dato)
            self.contador_datos += 1
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = NodoDatos(dato=dato)
        self.contador_datos += 1

    def imprimir_lista_datos(self):
        print('========================================')
        actual = self.cabeza
        while actual is not None:
            print('Tiempo:', actual.dato.tiempo, 'Amplitud:', actual.dato.amplitud, 'Valor:', actual.dato.valor)
            actual = actual.siguiente