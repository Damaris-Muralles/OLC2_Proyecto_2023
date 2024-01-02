from random import SystemRandom

random = SystemRandom()

class AST:
    def __init__(self, nombre, color):
        self.ID = random.randint(0, 0x1fffffffffffff)
        self.nombre = nombre
        self.color = color
        self.hijos = []

    def graficar(self):
        salida = f'n{self.ID} [label="{self.nombre}" fillcolor={self.color}];\n'
        print("soy hijos: ", self.hijos)
        for hijo in self.hijos:
            print("soy hijo: ", hijo.nombre)
            salida += f'n{self.ID} -> n{hijo.ID} ;\n'
            salida += hijo.graficar()
        return salida


