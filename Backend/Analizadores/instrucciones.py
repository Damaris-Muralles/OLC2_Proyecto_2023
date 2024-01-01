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
  CWHILE = 30
  WHEN = 31
  ELSE = 32
  LLAMAR_FUNCION = 33
  
# enump para tipo dato
class TIPO_DATO(Enum):
  INT = 1
  DECIMAL = 2
  CHAR = 3
  DATE = 4
  DATETIME = 5
  VARCHAR = 6
  BIT = 7 

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
  MAYOR_QUE = 5
  MENOR_QUE = 6
  IGUAL_IGUAL = 7
  NO_IGUAL = 8
  MAYOR_IGUAL = 9
  MENOR_IGUAL = 10
  AND = 11
  OR = 12
  NOT = 13
  IGUAL = 14
  BETWEEN = 15
  NOT_BETWEEN = 16
  


# funciones para encapsular las instrucciones
# DDL
def UseDatabase(id, linea, pos):
  return {
    "tipo" : TIPO_INSTRUCCION.USE_DATABASE,
    "id" : id,
    "linea": linea,
    "pos": pos
  }
  
def CreateDatabase(id, linea, pos):
  return {
    "tipo" : TIPO_INSTRUCCION.CREATE_DATABASE,
    "id" : id,
    "linea": linea,
    "pos": pos
  }

def CreateTable(id_, columnas_, linea, pos):
  return {
    "tipo" : TIPO_INSTRUCCION.CREATE_TABLE,
    "id" : id_,
    "columnas" : columnas_,
    "linea": linea,
    "pos": pos
  }

def AlterAgregar(tabla, columna , tipodato, atributo, linea, pos):
  return {
    "tipo" : TIPO_INSTRUCCION.ADD_COLUMNA,
    "idtabla" : tabla,
    "idcolumna" : columna,
    "tipodato" : tipodato,
    "atributo" : atributo,
    "linea": linea,
    "pos": pos
  }

def AlterDrop(tabla, columna, linea, pos):
  return {
    "tipo" : TIPO_INSTRUCCION.DROP_COLUMNA,
    "idtabla" : tabla,
    "idcolumna" : columna,
    "linea": linea,
    "pos": pos
  }

def TruncateTable(tabla, linea, pos):
  return{
    "tipo": TIPO_INSTRUCCION.TRUNCATE_TABLE,
    "id":tabla,
    "linea": linea,
    "pos": pos
  }

def DropTable(tabla, linea, pos):
  return{
    "tipo": TIPO_INSTRUCCION.DROP_TABLE,
    "id":tabla,
    "linea": linea,
    "pos": pos
  }
# DML
def UpdateTable(tabla, set, where, linea, pos):
  return{
    "tipo": TIPO_INSTRUCCION.UPDATE_TABLE,
    "id":tabla,
    "set":set,
    "where":where,
    "linea": linea,
    "pos": pos
  }

def DeleteTable(tabla, where, linea, pos):
  return{
    "tipo": TIPO_INSTRUCCION.DELETE_TABLE,
    "id":tabla,
    "where":where,
    "linea": linea,
    "pos": pos
  }

def SelectTable(columnas, tablas, where, linea, pos):
  return{
    "tipo": TIPO_INSTRUCCION.SELECT_TABLE,
    "columna":columnas,
    "tablas":tablas,
    "where":where,
    "linea": linea,
    "pos": pos
  }
def tselect(col,encabezado,linea,pos):
  return{
    "colum":col,
    "encabezado":encabezado,
    "linea": linea,
    "pos": pos
  }
def InsertTable(tabla,columnas , valores, linea, pos):
  return{
    "tipo": TIPO_INSTRUCCION.INSERT_TABLE,
    "id":tabla,
    "columnas":columnas,
    "valores":valores,
    "linea": linea,
    "pos": pos
  }


def LlamarColumna( punto, idtabla, idcolumna):
  return idtabla+punto+idcolumna


# funciones para encapsular expresiones y datos
def ColumnaTable(id, tdato, atributo, linea, pos):
  return {
    "tipo" : TIPO_INSTRUCCION.COLUMNA,
    "id" : id,
    "tipodato" :tdato,
    "atributo" :atributo,
    "linea": linea,
    "pos": pos
  }

def TipoDato(tipo, longitud, linea, pos):
  if tipo =="int":
    tipo = TIPO_DATO.INT
  elif tipo == "decimal":
    tipo = TIPO_DATO.DECIMAL
  elif tipo == "nchar":
    tipo = TIPO_DATO.CHAR
  elif tipo == "date":
    tipo = TIPO_DATO.DATE
  elif tipo == "datetime":
    tipo = TIPO_DATO.DATETIME
  elif tipo == "nvarchar":
    tipo = TIPO_DATO.VARCHAR
  elif tipo == "bit":
    tipo = TIPO_DATO.BIT
  return {
    "tipo" :tipo,
    "longitud" :longitud,
    "linea": linea,
    "pos": pos
  }

def Atributo(nombre, tabla, columna, linea, pos):
  if nombre == "primary":
    nombre = TIPO_ATRIBUTO.PRIMARY_KEY
  elif nombre == "reference":
    nombre = TIPO_ATRIBUTO.FOREIGN_KEY
  elif nombre == "not":
    nombre = TIPO_ATRIBUTO.NOT_NULL
  elif nombre == "null":
    nombre = TIPO_ATRIBUTO.NULL
  return {
    "tipo" :nombre,
    "idtabla_ref" :tabla,
    "idcolumna_ref" :columna,
    "linea": linea,
    "pos": pos
  }


#Funciones Sistema
def Concatena(cadena1, cadena2, linea, pos):
  return {
    "tipo" : TIPO_INSTRUCCION.CONTATENACION,
    "cadena1" : cadena1,
    "cadena2" : cadena2,
    "linea": linea,
    "pos": pos
  }

def Substraer(cadena, inicio, fin, linea, pos):
  return {
    "tipo" : TIPO_INSTRUCCION.SUBSTRER,
    "cadena" : cadena,
    "inicio" : inicio,
    "fin" : fin,
    "linea": linea,
    "pos": pos
  }

def Hoy(linea, pos):
  return {
    "tipo" : TIPO_INSTRUCCION.HOY,
    "linea": linea,
    "pos": pos

  }

def Contar(columna, linea, pos):
  return {
    "tipo" : TIPO_INSTRUCCION.CONTAR,
    "columna" : columna,
    "linea": linea,
    "pos": pos
  }

def Suma(columna, linea, pos):
  return {
    "tipo" : TIPO_INSTRUCCION.SUMA,
    "columna" : columna,
    "linea": linea,
    "pos": pos
  }

def Cast(columna, tipo, linea, pos):
  return {
    "tipo" : TIPO_INSTRUCCION.CAST,
    "columna" : columna,
    "tipodato" : tipo,
    "linea": linea,
    "pos": pos
  }

def Expresion(exp1, operador, exp2, linea, pos):
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
  elif operador == "=":
    operador = TIPO_OPERACION.IGUAL
  elif operador == "!=":
    operador = TIPO_OPERACION.NO_IGUAL
  elif operador == ">=":
    operador = TIPO_OPERACION.MAYOR_IGUAL
  elif operador == "<=":
    operador = TIPO_OPERACION.MENOR_IGUAL
  elif operador == "&&" or operador == "and":
    operador = TIPO_OPERACION.AND
  elif operador == "||" or operador == "or":
    operador = TIPO_OPERACION.OR
  elif operador == "!" or operador == "not":
    operador = TIPO_OPERACION.NOT
  elif operador == "between":
    operador = TIPO_OPERACION.BETWEEN
  elif operador == "NOT_BET":
    operador = TIPO_OPERACION.NOT_BETWEEN
  return {
    "tipo" : operador,
    "exp1" : exp1,
    "exp2" : exp2,
    "linea": linea,
    "pos": pos
    
  }


#SSL
def Case(sentencia, linea, pos):
  return{
    "tipo": TIPO_INSTRUCCION.CASE,
    "sentencias":sentencia,
    "linea": linea,
    "pos": pos

  }

def CicloWhile(condicion, instrucciones, linea, pos):
  return {
    "tipo" : TIPO_INSTRUCCION.CWHILE,
    "condicion" : condicion,
    "instrucciones" : instrucciones,
    "linea": linea,
    "pos": pos
  }

def Sentencia(tipo,expresion,resultado,linea,pos):
  if tipo=="when":
    tipo=TIPO_INSTRUCCION.WHEN
  elif tipo=="else":
    tipo=TIPO_INSTRUCCION.ELSE
  return{
    "tipodato":tipo,
    "condicion":expresion,
    "resultado":resultado,
    "linea": linea,
    "pos": pos
}

def sslIf(condicion, verdadero, falso, linea, pos):
  return {
    "tipo" : TIPO_INSTRUCCION.IF,
    "condicion" : condicion,
    "verdadero" : verdadero,
    "falso" : falso,
    "linea": linea,
    "pos": pos
  }

def DeclararVariable(id, tipo ,valor, linea, pos):
  return {
    "tipo" : TIPO_INSTRUCCION.DECLARAR_VARIABLE,
    "id" : id,
    "tipodato" : tipo,
    "valor" : valor,
    "linea": linea,
    "pos": pos
  }

def LlamarFuncion(id, parametros, linea, pos):
  return {
    "tipo" : TIPO_INSTRUCCION.LLAMAR_FUNCION,
    "id" : id,
    "parametros" : parametros,
    "linea": linea,
    "pos": pos
  }
def AsignacionVariable(id, valor, linea, pos):
  return {
    "tipo" : TIPO_INSTRUCCION.ASIGNACION_VARIABLE,
    "id" : id,
    "valor" : valor,
    "linea": linea,
    "pos": pos
  }

def Parametro(id, tipo,valor, linea, pos):
  return {
    "tipo" : TIPO_INSTRUCCION.PARAMETRO,
    "id" : id,
    "tipodato" : tipo,
    "valor" : valor,
    "linea": linea,
    "pos": pos
  }

def sslprocedure(id, parametros, instrucciones, linea, pos):
  return {
    "tipo" : TIPO_INSTRUCCION.PROCEDURE,
    "id" : id,
    "parametros" : parametros,
    "instrucciones" : instrucciones,
    "linea": linea,
    "pos": pos
  }

def sslfunction(id, parametros, returns, instrucciones, linea, pos):
  return {
    "tipo" : TIPO_INSTRUCCION.FUNCTION,
    "id" : id,
    "parametros" : parametros,
    "retornar" : returns,
    "instrucciones" : instrucciones,
    "linea": linea,
    "pos": pos
  }

def Retornar(valor, linea, pos):
  return {
    "tipo" : TIPO_INSTRUCCION.RETORNAR,
    "valor" : valor,
    "linea": linea,
    "pos": pos
  }

