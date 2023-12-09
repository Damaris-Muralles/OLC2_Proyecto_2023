


# funciones para encapsular las instrucciones

def CreateTable(id_, columnas_):
  return {
    "tipo" : "CREATETABLE",
    "id" : id_,
    "columnas" : columnas_
  }

def AlterAgregar(id_, accion):
  return {
    "tipo" : "AgregarColumna",
    "id" : id_,
    "accion" : accion
  }

def AlterDrop(id_, accion):
  return {
    "tipo" : "DropColumna",
    "id" : id_,
    "accion" : accion
  }

def TruncateTable(id_):
  return{
    "tipo": "TruncateTable",
    "id":id_,
      
  }



# funciones para encapsular expresiones y datos
def ColumnaTable(id, tdato, atributo):
  return {
    "tipo" : "columnaTable",
    "id" : id,
    "tipodato" :tdato,
    "atributo" :atributo
  }

def TipoDato(tipo, longitud, cantidad):
  return {
    "tipo" : "dato",
    "tipodato" :tipo,
    "longitud" :longitud,
    "cantidad" :cantidad
  }


def Atributo(nombre, id1, id2):
  return {
    "tipo" : "atributo",
    "nombre" :nombre,
    "id1" :id1,
    "id2" :id2
  }


