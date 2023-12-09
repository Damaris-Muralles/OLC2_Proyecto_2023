
def CreateTable(id_, columnas_):
    return {
      "id" : id_,
      "columnas" : columnas_,
      "tipo" : "createTable"
    }


def ColumnaTable(id, tdato, atributo):
    return {
      "id" : id,
      "tdato" :tdato,
      "atributo" :atributo,
      "tipo" : "columnaTable"
    }

def Texto(texto, numero):
    return {
      "texto" :texto,
      "numero" :numero,
     "tipo" : "texto"
    }


def Atributo(nombre, id1, id2):
    return {
      "nombre" :nombre,
      "id1" :id1,
      "id2" :id2,
      "tipo" : "atributo"
    }

def AlterAgregar(id_, accion):
    return {
      "id" : id_,
      "accion" : accion,
      "tipo" : "AgregarColumna"
    }

def AlterDrop(id_, accion):
    return {
      "id" : id_,
      "accion" : accion,
      "tipo" : "DropColumna"
    }

def TruncateTable(id_):
    return{
        "id":id_,
        "tipo": "TruncateTable"
    }
