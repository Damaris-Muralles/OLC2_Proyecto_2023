# clase que permita almacenar una lista (nativa) de datos que tenga token, lexema, fila y columna


class Nodo:
    def __init__(self, token, lexema, fila, columna):
        self.token = token
        self.lexema = lexema
        self.fila = fila
        self.columna = columna
        self.siguiente = None
        self.anterior = None


class ListaGramar:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def insertar(self, token, lexema, fila, columna):
        nuevo = Nodo(token, lexema, fila, columna)
        if self.vacia():
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            self.ultimo = nuevo

    def recorrer(self):
        aux = self.primero
        while aux != None:
            print(aux.token, aux.lexema, aux.fila, aux.columna)
            aux = aux.siguiente
    # metodo que recorra la lista y que devuelva un string con codigo de graphviz para graficar la lista en forma de tabla con los datos de token, lexema, fila y columna
            
    def graficar(self):
        aux = self.primero
        cadena = "digraph G {\n"
        cadena += "node [shape=plaintext]\n"
        cadena += "arset [label=<\n"
        cadena += " <table border='1' cellborder='1' cellspacing='0' bgcolor='black' color='white'>\n"
        cadena += "<tr><td><font color='deepskyblue2'>Token</font></td><td><font color='deepskyblue2'>Lexema</font></td><td><font color='deepskyblue2'>Fila</font></td><td><font color='deepskyblue2'>Columna</font></td></tr>\n"
        while aux != None:
            cadena += "<tr><td><font color='white'>" + str(aux.token) + "</font></td><td><font color='white'>" + str(aux.lexema) + "</font></td><td><font color='white'>" + str(aux.fila) + "</font></td><td><font color='white'>" + str(aux.columna) + "</font></td></tr>\n"
            aux = aux.siguiente
        cadena += "</table>>];\n}"
        return cadena
