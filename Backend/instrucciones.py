


# funciones para encapsular las instrucciones

def CreateTable(id_, columnas_):
  return {
    "tipo" : "CREATETABLE",
    "id" : id_,
    "columnas" : columnas_
  }

def AlterAgregar(tabla, columna , tipodato):
  return {
    "tipo" : "AgregarColumna",
    "tabla" : tabla,
    "columna" : columna,
    "tipodato" : tipodato
  }

def AlterDrop(tabla, columna):
  return {
    "tipo" : "DropColumna",
    "tabla" : tabla,
    "columna" : columna
  }

def TruncateTable(tabla):
  return{
    "tipo": "TruncateTable",
    "tabla":tabla
  }

def DropTable(tabla):
  return{
    "tipo": "DropTable",
    "tabla":tabla
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
    "tipo" : "tipoDato",
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


