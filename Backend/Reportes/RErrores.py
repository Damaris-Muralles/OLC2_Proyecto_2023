# clase que permita almacenar una lista (nativa) de datos que tenga numero,tipo,descripcion, fila y columna


class Nodo:
    def __init__(self, numero, tipo, descripcion, fila, columna):
        self.numero = numero
        self.tipo = tipo
        self.descripcion = descripcion
        self.fila = fila
        self.columna = columna
        self.siguiente = None
        self.anterior = None


class ListaError:

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.index = 0

    def vacia(self):
        return self.primero == None

    def insertar(self,  tipo, descripcion, fila, columna):
        self.index += 1
        nuevo = Nodo(self.index, tipo, descripcion, fila, columna)
        if self.vacia():
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            self.ultimo = nuevo

   
    # metodo que recorra la lista y que devuelva un string con codigo de graphviz para graficar la lista en forma de tabla con los datos de numero,tipo,descripcion, fila y columna pero solo los de tipo "Sintactico"

    def graficarSint(self):
        aux = self.primero
        cadena = "digraph G {\n"
        cadena += "node [shape=plaintext]\n"
        cadena += "arset [label=<\n"
        cadena += " <table border='1' cellborder='1' cellspacing='5' cellpadding='10' bgcolor='black' color='white'>\n"
        cadena += "<tr><td style='padding: 10px;'><font color='deepskyblue2'>No.</font></td><td style='padding: 10px;'><font color='deepskyblue2'>Tipo</font></td><td style='padding: 10px;'><font color='deepskyblue2'>Descripcion</font></td><td style='padding: 10px;'><font color='deepskyblue2'>Fila</font></td><td style='padding: 10px;'><font color='deepskyblue2'>Columna</font></td></tr>\n"
        while aux != None:
            if aux.tipo == "Sintactico":
                cadena += "<tr><td style='padding: 10px;'><font color='white'>" + str(aux.numero) + "</font></td><td style='padding: 10px;'><font color='white'>" + str(aux.tipo) + "</font></td><td style='padding: 10px;'><font color='white'>" + str(aux.descripcion) + "</font></td><td style='padding: 10px;'><font color='white'>" + str(aux.fila) + "</font></td><td style='padding: 10px;'><font color='white'>" + str(aux.columna) + "</font></td></tr>\n"
            aux = aux.siguiente
        cadena += "</table>>];\n}"
        return cadena
    
    def graficarLex(self):
        aux = self.primero
        cadena = "digraph G {\n"
        cadena += "node [shape=plaintext]\n"
        cadena += "arset [label=<\n"
        cadena += " <table border='1' cellborder='1' cellspacing='0' bgcolor='black' color='white'>\n"
        cadena += "<tr><td style='padding: 10px;'><font color='deepskyblue2'>No.</font></td><td><font color='deepskyblue2'>Tipo</font></td><td><font color='deepskyblue2'>Descripcion</font></td><td><font color='deepskyblue2'>Fila</font></td><td><font color='deepskyblue2'>Columna</font></td></tr>\n"
        while aux != None:
            if aux.tipo == "Lexico":
                cadena += "<tr><td><font color='white'>" + str(aux.numero) + "</font></td><td><font color='white'>" + str(aux.tipo) + "</font></td><td><font color='white'>" + str(aux.descripcion) + "</font></td><td><font color='white'>" + str(aux.fila) + "</font></td><td><font color='white'>" + str(aux.columna) + "</font></td></tr>\n"
            aux = aux.siguiente
        cadena += "</table>>];\n}"
        return cadena
    
    def graficarSem(self):
        aux = self.primero
        cadena = "digraph G {\n"
        cadena += "node [shape=plaintext]\n"
        cadena += "arset [label=<\n"
        cadena += " <table border='1' cellborder='1' cellspacing='5' cellpadding='10' bgcolor='black' color='white'>\n"
        cadena += "<tr><td style='padding: 10px;'><font color='deepskyblue2'>No.</font></td><td style='padding: 10px;'><font color='deepskyblue2'>Tipo</font></td><td style='padding: 10px;'><font color='deepskyblue2'>Descripcion</font></td><td style='padding: 10px;'><font color='deepskyblue2'>Fila</font></td><td style='padding: 10px;'><font color='deepskyblue2'>Columna</font></td></tr>\n"
        while aux != None:
            if aux.tipo == "Semantico":
                cadena += "<tr><td><font color='white'>" + str(aux.numero) + "</font></td><td><font color='white'>" + str(aux.tipo) + "</font></td><td><font color='white'>" + str(aux.descripcion) + "</font></td><td><font color='white'>" + str(aux.fila) + "</font></td><td><font color='white'>" + str(aux.columna) + "</font></td></tr>\n"
            aux = aux.siguiente
        cadena += "</table>>];\n}"
        return cadena