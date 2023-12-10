


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

def UpdateTable(tabla, set, where):
  return{
    "tipo": "UPDATE_TABLE",
    "idtabla":tabla,
    "set":set,
    "where":where
  }

def DeleteTable(tabla, where):
  return{
    "tipo": "DELETE_TABLE",
    "idtabla":tabla,
    "where":where
  }

def SelectTable(columnas, tablas, where):
  return{
    "tipo": "SELECT_TABLE",
    "columna":columnas,
    "tablas":tablas,
    "where":where
  }
def InsertTable(tabla,columnas , valores):
  return{
    "tipo": "INSERT_TABLE",
    "idtabla":tabla,
    "columnas":columnas,
    "valores":valores
  }


def Llaves( punto, idtabla, idcolumna):
  return{
    "tipo": "Llave",
    "punto":punto,
    "idtabla":idtabla,
    "idcolumna":idcolumna
  }

def FuncionNativa(tipo,param1,param2,param3,param4):
  return {
    "tipo" : "FUNCION_NATIVA",
    "tipofuncion" : tipo,
    "param1" : param1,
    "param2" : param2,
    "param3" : param3,
    "param4" : param4
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


#Funciones Sistema
def Concatena(cadena1, cadena2):
  return {
    "tipo" : "CONCATENA",
    "cadena1" : cadena1,
    "cadena2" : cadena2
  }

def Substraer(cadena, inicio, fin):
  return {
    "tipo" : "SUBSTRAER",
    "cadena" : cadena,
    "inicio" : inicio,
    "fin" : fin
  }

def Hoy():
  return {
    "tipo" : "HOY"
  }

def Contar():
  return {
    "tipo" : "CONTAR"
  }
def Suma(columna):
  return {
    "tipo" : "SUMA",
    "columna" : columna
  }

def Cast(columna, tipo):
  return {
    "tipo" : "CAST",
    "columna" : columna,
    "tipo" : tipo
  }

def Expresion(exp1, operador, exp2):
  return {
    "tipo" : "EXPRESION",
    "exp1" : exp1,
    "exp2" : exp2,
    "operador" : operador
  }


#SSL

def sslIf(condicion, instrucciones):
  return {
    "tipo" : "IF",
    "condicion" : condicion,
    "instrucciones" : instrucciones
  }

def DeclararVariable(id, tipo ,valor):
  return {
    "tipo" : "DECLARAR_VARIABLE",
    "id" : id,
    "tipodato" : tipo,
    "valor" : valor
  }

def AsignacionVariable(id, valor):
  return {
    "tipo" : "ASIGNACION_VARIABLE",
    "id" : id,
    "valor" : valor
  }

def Parametro(id, tipo):
  return {
    "tipo" : "PARAMETRO",
    "id" : id,
    "tipodato" : tipo
  }
def sslprocedure(id, parametros, instrucciones):
  return {
    "tipo" : "PROCEDURE",
    "id" : id,
    "parametros" : parametros,
    "instrucciones" : instrucciones
  }

def sslfunction(id, parametros, returns, instrucciones):
  return {
    "tipo" : "FUNCTION",
    "id" : id,
    "parametros" : parametros,
    "return" : returns,
    "instrucciones" : instrucciones
  }

def Retornar(valor):
  return {
    "tipo" : "RETORNAR",
    "valor" : valor
  }

