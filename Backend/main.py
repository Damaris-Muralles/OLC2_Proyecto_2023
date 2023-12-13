import gramar as g
import tablasimbolo as TS
from instrucciones import *
from manejoxml import *

xml = XMLManejador("./BasesDatos.xml")
ActualBaseDatos = ""

def procesar_createdatabase(instr) :
    global ActualBaseDatos
    print("create database: ",instr.get("id"))
    print(xml.add_database(instr.get("id")))
    ActualBaseDatos = instr.get("id")

def procesar_createtable(instr):
    print("create table")
    print(xml.add_table_info(ActualBaseDatos, instr))

def procesar_usedatabase(instr):
    global ActualBaseDatos
    base = instr.get("id")
    print("use database: ",instr.get("id"))
    ActualBaseDatos = base

def procesar_insert(instr):
    print("insert")
    print(xml.insert_data(ActualBaseDatos,instr))
def procesar_instrucciones(instrucciones) :
    ## lista de instrucciones recolectadas
    for instr in instrucciones :
        if instr.get('tipo')== TIPO_INSTRUCCION.CREATE_DATABASE : procesar_createdatabase(instr)
        elif instr.get('tipo') == TIPO_INSTRUCCION.CREATE_TABLE : procesar_createtable(instr)
        elif instr.get('tipo') == TIPO_INSTRUCCION.USE_DATABASE : procesar_usedatabase(instr)
        elif instr.get('tipo') == TIPO_INSTRUCCION.INSERT_TABLE : procesar_insert(instr)
        else : print('Error: instrucción no válida')

#f = open("./entrada.txt", "r")

#input = f.read()
input = """
CREATE DATA BASE intento; 

USAR intento;
 
CREATE TABLE products (
id int PRIMARY KEY,
nombre nvarchar(1000) NOT NULL,
bandera int NULL
);
INSERT INTO products (id,nombre,bandera) VALUES(1,'JULIO LOPEZ',1); 
"""
instrucciones = g.parse(input.lower())
ts_global = TS.TablaSimbolo()

procesar_instrucciones(instrucciones)



