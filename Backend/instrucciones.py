# enums para las instrucciones
from enum import Enum
# enump para tipo instruccion
class TIPO_INSTRUCCION(Enum):
  USE_DATABASE = 1
  CREATE_DATABASE = 2
  CREATE_TABLE = 3
  ADD_COLUMNA = 4
  DROP_COLUMNA = 5
  TRUNCATE_TABLE = 6
  DROP_TABLE = 7
  UPDATE_TABLE = 8
  DELETE_TABLE = 9
  SELECT_TABLE = 10
  INSERT_TABLE = 11
  CASE = 12
  SENTENCIA = 13
  LLAVE = 14
  FUNCION_NATIVA = 15
  IF = 16
  DECLARAR_VARIABLE = 17
  ASIGNACION_VARIABLE = 18
  PARAMETRO = 19
  PROCEDURE = 20
  FUNCTION = 21
  RETORNAR = 22
# enump para tipo dato
class TIPO_DATO(Enum):
  INT = 1
  DECIMAL = 2
  
# enump para tipo operacion


# funciones para encapsular las instrucciones
def UseDatabase(id):
  return {
    "tipo" : TIPO_INSTRUCCION.USE_DATABASE,
    "idbase" : id
  }
  
def CreateDatabase(id):
  return {
    "tipo" : TIPO_INSTRUCCION.CREATE_DATABASE,
    "idbase" : id
  }

def CreateTable(id_, columnas_):
  return {
    "tipo" : TIPO_INSTRUCCION.CREATE_TABLE,
    "idtabla" : id_,
    "columnas" : columnas_
  }

def AlterAgregar(tabla, columna , tipodato):
  return {
    "tipo" : TIPO_INSTRUCCION.ADD_COLUMNA,
    "idtabla" : tabla,
    "idcolumna" : columna,
    "tipodato" : tipodato
  }

def AlterDrop(tabla, columna):
  return {
    "tipo" : TIPO_INSTRUCCION.DROP_COLUMNA,
    "idtabla" : tabla,
    "idcolumna" : columna
  }

def TruncateTable(tabla):
  return{
    "tipo": TIPO_INSTRUCCION.TRUNCATE_TABLE,
    "idtabla":tabla
  }

def DropTable(tabla):
  return{
    "tipo": TIPO_INSTRUCCION.DROP_TABLE,
    "idtabla":tabla
  }

def UpdateTable(tabla, set, where):
  return{
    "tipo": TIPO_INSTRUCCION.UPDATE_TABLE,
    "idtabla":tabla,
    "set":set,
    "where":where
  }

def DeleteTable(tabla, where):
  return{
    "tipo": TIPO_INSTRUCCION.DELETE_TABLE,
    "idtabla":tabla,
    "where":where
  }

def SelectTable(columnas, tablas, where):
  return{
    "tipo": TIPO_INSTRUCCION.SELECT_TABLE,
    "columna":columnas,
    "tablas":tablas,
    "where":where
  }
def InsertTable(tabla,columnas , valores):
  return{
    "tipo": TIPO_INSTRUCCION.INSERT_TABLE,
    "idtabla":tabla,
    "columnas":columnas,
    "valores":valores
  }

def Case(tipo,expresion,when,else_):
  return{
    "tipo": "CASE",
    "sentencias":tipo  
  }

def Sentencia(tipo,expresion,resultado):
  return{
    "tipo": "SENTENCIA",
    "tipo":tipo,
    "condicion":expresion,
    "resultado":resultado
  }

def Llaves( punto, idtabla, idcolumna):
  return{
    "tipo": "LLAVE",
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

