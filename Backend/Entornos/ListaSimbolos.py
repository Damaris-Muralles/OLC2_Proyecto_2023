# Imports
from Entornos.Rsimbolo import RSimbolo  # Asegúrate de tener definido el módulo rsimbolo

# Constructor
class ListaSimbolo:
    def __init__(self):
        self.lista = []

    def add(self, nombre, contenido, tipo, entorno):
        nuevo = RSimbolo(nombre, contenido, tipo, entorno)
        self.lista.append(nuevo)

    def update(self, nombre, entorno, nuevo):
        for simbolo in self.lista:
            if simbolo.id == nombre and simbolo.entorno == entorno:
                simbolo.valor = nuevo
                break


