class Entorno:
    def __init__(self, padre, nombre):
        self.nombre = nombre
        self.anterior = padre
        self.tablaSimbolos = {}
        self.tablaMetodos = {}
        self.retorno = ""

    def addSimbolo(self, nombre, simbolo):
        self.tablaSimbolos[nombre.lower()] = simbolo

    def addMetodo(self, nombre, metodo):
        print("nombre: ", metodo)
        self.tablaMetodos[nombre.lower()] = metodo

    def getSimbolo(self, nombre):
        entorno_actual = self
        while entorno_actual is not None:
            resultado = entorno_actual.tablaSimbolos.get(nombre.lower())
            if resultado is not None:
                return resultado
            entorno_actual = entorno_actual.anterior
        return None

    def getSimboloE(self, nombre):
        entorno_actual = self
        while entorno_actual is not None:
            resultado = entorno_actual.tablaSimbolos.get(nombre.lower())
            if resultado is not None:
                return {"resultado": resultado, "entorno": entorno_actual.nombre}
            entorno_actual = entorno_actual.anterior
        return None

    def actualizar(self, nombre, simbolo):
        entorno_actual = self
        while entorno_actual is not None:
            encontrado = entorno_actual.tablaSimbolos.get(nombre.lower())
            if encontrado:
                entorno_actual.tablaSimbolos[nombre.lower()] = simbolo
                return True
            entorno_actual = entorno_actual.anterior
        return False

    def getMetodo(self, nombre):
        for entorno in self.__iter_entornos():
            resultado = self.tablaMetodos.get(nombre.lower())
            if resultado is not None:
                return resultado
        return None


    def buscarSimboloGlobal(self, nombre):
        for entorno in self.__iter_entornos():
            resultado = self.tablaSimbolos.get(nombre.lower())
            if resultado is not None:
                return True
        return False

    def buscarSimbolo(self, nombre):
        return nombre.lower() in self.tablaSimbolos

    def buscarMetodo(self, nombre):
        for entorno in self.__iter_entornos():
            resultado = self.tablaMetodos.get(nombre.lower())
            if resultado is not None:
                return True
        return False

    def setRetorno(self, tipo):
        self.retorno = tipo

    def __iter_entornos(self):
        entorno_actual = self
        while entorno_actual is not None:
            yield entorno_actual
            entorno_actual = entorno_actual.anterior
