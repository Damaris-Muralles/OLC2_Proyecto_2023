


# funciones para encapsular las instrucciones
def UseDatabase(id):
  return {
    "tipo" : "USE_DATABASE",
    "idbase" : id
  }
  
def CreateDatabase(id):
  return {
    "tipo" : "CREATE_DATABASE",
    "idbase" : id
  }

def CreateTable(id_, columnas_):
  return {
    "tipo" : "CREATE_TABLE",
    "idtabla" : id_,
    "columnas" : columnas_
  }

def AlterAgregar(tabla, columna , tipodato):
  return {
    "tipo" : "ADD_COLUMNA",
    "idtabla" : tabla,
    "idcolumna" : columna,
    "tipodato" : tipodato
  }

def AlterDrop(tabla, columna):
  return {
    "tipo" : "DROP_COLUMNA",
    "idtabla" : tabla,
    "idcolumna" : columna
  }

def TruncateTable(tabla):
  return{
    "tipo": "TRUNCATE_TABLE",
    "idtabla":tabla
  }

def DropTable(tabla):
  return{
    "tipo": "DROP_TABLE",
    "idtabla":tabla
  }



# funciones para encapsular expresiones y datos
def ColumnaTable(id, tdato, atributo):
  return {
    "tipo" : "COLUMNA_TABLE",
    "idcolumna" : id,
    "tipodato" :tdato,
    "atributo" :atributo
  }

def TipoDato(tipo, longitud, cantidad):
  return {
    "tipo" : "TIPO_DATO",
    "tipodato" :tipo,
    "longitud" :longitud,
    "cantidad" :cantidad
  }

def Atributo(nombre, id1, id2):
  return {
    "tipo" : "ATRIBUTO_COLUMN",
    "atributo" :nombre,
    "idtabla" :id1,
    "idcolumna" :id2
  }


