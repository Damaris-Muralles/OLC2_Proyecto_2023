
class simbolo():
    def __init__(self,id,tipo,valor):
        self.id = id
        self.tipo = tipo
        self.valor = valor

class TablaSimbolo():

    def __init__(self,simbolos = {}):
        self.listsimbolos = simbolos

    def add_simbolo(self,simbolo):
        self.listsimbolos[simbolo.id] = simbolo

    def update_simbolo(self,simbolo):
        if id in self.listsimbolos:
            self.listsimbolos[simbolo.id] = simbolo
            return {"Error":None}
        
        else:
            return {"Error":f"variable {simbolo.id} no definida"}
        
    def get_simbolo(self,id):
        if id in self.listsimbolos:
            return {"Error":None,"simbol":self.listsimbolos[id]}
        else:
            return {"Error":f"variable {id} no definida", "simbol":None}
        