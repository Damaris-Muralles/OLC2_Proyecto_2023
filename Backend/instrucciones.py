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
  LLAMARCOLUMNA = 14
  FUNCION_NATIVA = 15
  IF = 16
  DECLARAR_VARIABLE = 17
  ASIGNACION_VARIABLE = 18
  PARAMETRO = 19
  PROCEDURE = 20
  FUNCTION = 21
  RETORNAR = 22
  COLUMNA = 23
  CONTATENACION = 24
  SUBSTRER = 25
  HOY = 26
  CONTAR = 27
  SUMA = 28
  CAST = 29
  
# enump para tipo dato
class TIPO_DATO(Enum):
  INT = 1
  DECIMAL = 2
  CHAR = 3
  DATE = 4
  DATETIME = 5
  VARCHAR = 6
  BIT = 7 
  INTEGER = 8

class TIPO_ATRIBUTO(Enum):
  PRIMARY_KEY = 1
  FOREIGN_KEY = 2
  NOT_NULL = 3
  NULL = 4

  
# enump para tipo operacion
class TIPO_OPERACION(Enum):
  SUMA = 1
  RESTA = 2
  MULTIPLICACION = 3
  DIVISION = 4
  MAYOR_QUE = 7
  MENOR_QUE = 8
  IGUAL_IGUAL = 9
  NO_IGUAL = 10
  MAYOR_IGUAL = 11
  MENOR_IGUAL = 12
  AND = 13
  OR = 14
  NOT = 15
  

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
    "tipo": TIPO_INSTRUCCION.CASE,
    "sentencias":tipo,
    "expresiones" : expresion,
    "when":when,

  }

def Sentencia(tipo,expresion,resultado):
  return{
    "tipo": TIPO_INSTRUCCION.SENTENCIA,
    "tipo":tipo,
    "condicion":expresion,
    "resultado":resultado
  }

def LlamarColumna( punto, idtabla, idcolumna):
  return{
    "tipo": TIPO_INSTRUCCION.LLAMARCOLUMNA,
    "punto":punto,
    "idtabla":idtabla,
    "idcolumna":idcolumna
  }


# funciones para encapsular expresiones y datos
def ColumnaTable(id, tdato, atributo):
  return {
    "tipo" : TIPO_INSTRUCCION.COLUMNA,
    "idcolumna" : id,
    "tipodato" :tdato,
    "atributo" :atributo
  }

def TipoDato(tipo, longitud, cantidad):
  if tipo =="int":
    tipo = TIPO_DATO.INT
  elif tipo == "decimal":
    tipo = TIPO_DATO.DECIMAL
  elif tipo == "char":
    tipo = TIPO_DATO.CHAR
  elif tipo == "date":
    tipo = TIPO_DATO.DATE
  elif tipo == "datetime":
    tipo = TIPO_DATO.DATETIME
  elif tipo == "varchar":
    tipo = TIPO_DATO.VARCHAR
  elif tipo == "bit":
    tipo = TIPO_DATO.BIT
  return {
    "tipo" :tipo,
    "longitud" :longitud,
    "cantidad" :cantidad
  }

def Atributo(nombre, tabla, columna):
  if nombre == "primary":
    nombre = TIPO_ATRIBUTO.PRIMARY_KEY
  elif nombre == "references":
    nombre = TIPO_ATRIBUTO.FOREIGN_KEY
  elif nombre == "not":
    nombre = TIPO_ATRIBUTO.NOT_NULL
  elif nombre == "null":
    nombre = TIPO_ATRIBUTO.NULL
  return {
    "tipo" :nombre,
    "idtabla_ref" :tabla,
    "idcolumna_ref" :columna
  }


#Funciones Sistema
def Concatena(cadena1, cadena2):
  return {
    "tipo" : TIPO_INSTRUCCION.CONTATENACION,
    "cadena1" : cadena1,
    "cadena2" : cadena2
  }

def Substraer(cadena, inicio, fin):
  return {
    "tipo" : TIPO_INSTRUCCION.SUBSTRER,
    "cadena" : cadena,
    "inicio" : inicio,
    "fin" : fin
  }

def Hoy():
  return {
    "tipo" : TIPO_INSTRUCCION.HOY
  }

def Contar():
  return {
    "tipo" : TIPO_INSTRUCCION.CONTAR
  }
def Suma(columna):
  return {
    "tipo" : TIPO_INSTRUCCION.SUMA,
    "columna" : columna
  }

def Cast(columna, tipo):
  return {
    "tipo" : TIPO_INSTRUCCION.CAST,
    "columna" : columna,
    "tipo" : tipo
  }

def Expresion(exp1, operador, exp2):
  if operador == "+":
    operador = TIPO_OPERACION.SUMA
  elif operador == "-":
    operador = TIPO_OPERACION.RESTA
  elif operador == "*":
    operador = TIPO_OPERACION.MULTIPLICACION
  elif operador == "/":
    operador = TIPO_OPERACION.DIVISION
  elif operador == ">":
    operador = TIPO_OPERACION.MAYOR_QUE
  elif operador == "<":
    operador = TIPO_OPERACION.MENOR_QUE
  elif operador == "==":
    operador = TIPO_OPERACION.IGUAL_IGUAL
  elif operador == "!=":
    operador = TIPO_OPERACION.NO_IGUAL
  elif operador == ">=":
    operador = TIPO_OPERACION.MAYOR_IGUAL
  elif operador == "<=":
    operador = TIPO_OPERACION.MENOR_IGUAL
  elif operador == "&&":
    operador = TIPO_OPERACION.AND
  elif operador == "||":
    operador = TIPO_OPERACION.OR
  elif operador == "!":
    operador = TIPO_OPERACION.NOT
  return {
    "tipo" : operador,
    "exp1" : exp1,
    "exp2" : exp2,
  }


#SSL

def sslIf(condicion, instrucciones):
  return {
    "tipo" : TIPO_INSTRUCCION.IF,
    "condicion" : condicion,
    "instrucciones" : instrucciones
  }

def DeclararVariable(id, tipo ,valor):
  return {
    "tipo" : TIPO_INSTRUCCION.DECLARAR_VARIABLE,
    "id" : id,
    "tipodato" : tipo,
    "valor" : valor
  }

def AsignacionVariable(id, valor):
  return {
    "tipo" : TIPO_INSTRUCCION.ASIGNACION_VARIABLE,
    "id" : id,
    "valor" : valor
  }

def Parametro(id, tipo):
  return {
    "tipo" : TIPO_INSTRUCCION.PARAMETRO,
    "id" : id,
    "tipodato" : tipo
  }
def sslprocedure(id, parametros, instrucciones):
  return {
    "tipo" : TIPO_INSTRUCCION.PROCEDURE,
    "id" : id,
    "parametros" : parametros,
    "instrucciones" : instrucciones
  }

def sslfunction(id, parametros, returns, instrucciones):
  return {
    "tipo" : TIPO_INSTRUCCION.FUNCTION,
    "id" : id,
    "parametros" : parametros,
    "return" : returns,
    "instrucciones" : instrucciones
  }

def Retornar(valor):
  return {
    "tipo" : TIPO_INSTRUCCION.RETORNAR,
    "valor" : valor
  }

