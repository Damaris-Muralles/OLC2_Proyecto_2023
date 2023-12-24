# Imports
from Entornos.Rmetodo import *  # Asegúrate de tener definido el módulo rmetodo

# Constructor
class ListaMetodo:
    def __init__(self):
        self.lista = []

    def add(self, nombre, tipo):
        nuevo = RMetodo(nombre, tipo)
        self.lista.append(nuevo)

