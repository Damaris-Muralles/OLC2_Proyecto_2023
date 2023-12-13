import gramar as g
import tablasimbolo as TS
from instrucciones import *
from manejoxml import *

xml = XMLManejador("./BasesDatos.xml")
ActualBaseDatos = ""

def procesar_createdatabase(instr) :
    global ActualBaseDatos
    print("create database")
    print(instr.get("id"))
    print(xml.add_database(instr.get("id")))
    ActualBaseDatos = instr.get("id")

def procesar_createtable(instr):
    print("create table")
   
 
    print(xml.add_table_info(ActualBaseDatos, instr))

def procesar_usedatabase(instr):
    global ActualBaseDatos
    base = instr.get("idbase")
    print("use database")
    print(instr.get("idbase"))
    ActualBaseDatos = base
    print(ActualBaseDatos)


def procesar_instrucciones(instrucciones) :
    ## lista de instrucciones recolectadas
    for instr in instrucciones :
        if instr.get('tipo')== TIPO_INSTRUCCION.CREATE_DATABASE : procesar_createdatabase(instr)
        elif instr.get('tipo') == TIPO_INSTRUCCION.CREATE_TABLE : procesar_createtable(instr)
        elif instr.get('tipo') == TIPO_INSTRUCCION.USE_DATABASE : procesar_usedatabase(instr)

#f = open("./entrada.txt", "r")

#input = f.read()
input = """
CREATE DATA BASE intento; 

USAR intento;
 
CREATE TABLE products (
product_no int PRIMARY KEY,
name nvarchar(1000) NOT NULL,
price decimal NULL,
product_no int REFERENCE products (product_no)
);

"""
instrucciones = g.parse(input.lower())
ts_global = TS.TablaSimbolo()

procesar_instrucciones(instrucciones)



