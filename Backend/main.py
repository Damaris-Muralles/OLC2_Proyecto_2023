import gramar as g
import tablasimbolo as TS
from instrucciones import *
from manejoxml import *
from Where import *

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

def procesar_dropcolumna(instr):
    print("drop columna")
    print(xml.drop_column(ActualBaseDatos, instr))

def procesar_addcolumna(instr):
    print("add columna")
    print(xml.add_column(ActualBaseDatos, instr))

def procesar_droptable(instr):
    print("drop table")
    print(xml.drop_table(ActualBaseDatos, instr))

def procesar_truncatetable(instr):
    print("truncate table")
    print(xml.truncate_table(ActualBaseDatos, instr))

def procesar_delete(instr):
    print("delete")
    print(instr.get("where"))
    # solo para probar el where
    eliminar=procesar_where1(instr.get("where"),ActualBaseDatos, instr.get("id"))
    
    #print(xml.delete_registro(ActualBaseDatos, instr.get("id"),eliminar))

def procesar_update(instr):
    print(instr)
    whereupdate = procesar_where1(instr.get("where"),ActualBaseDatos, instr.get("id"))
    listset = []

    for i in instr.get("set"):

        listset.append(procesar_where1(i.get("exp2"), ActualBaseDatos, instr.get("id")))

    print(listset)

    print(xml.UpdateTable(ActualBaseDatos, instr.get("id"),instr.get("set"), listset,whereupdate))


def procesar_instrucciones(instrucciones) :
    ## lista de instrucciones recolectadas
    for instr in instrucciones :
        if instr.get('tipo')== TIPO_INSTRUCCION.CREATE_DATABASE : procesar_createdatabase(instr)
        elif instr.get('tipo') == TIPO_INSTRUCCION.CREATE_TABLE : procesar_createtable(instr)
        elif instr.get('tipo') == TIPO_INSTRUCCION.DROP_COLUMNA : procesar_dropcolumna(instr)
        elif instr.get('tipo') == TIPO_INSTRUCCION.ADD_COLUMNA : procesar_addcolumna(instr)
        elif instr.get('tipo') == TIPO_INSTRUCCION.DROP_TABLE : procesar_droptable(instr)
        elif instr.get('tipo') == TIPO_INSTRUCCION.TRUNCATE_TABLE : procesar_truncatetable(instr)
        elif instr.get('tipo') == TIPO_INSTRUCCION.INSERT_TABLE : procesar_insert(instr)
        elif instr.get('tipo') == TIPO_INSTRUCCION.USE_DATABASE : procesar_usedatabase(instr)
        elif instr.get('tipo') == TIPO_INSTRUCCION.DELETE_TABLE : procesar_delete(instr)
        elif instr.get('tipo') == TIPO_INSTRUCCION.UPDATE_TABLE : procesar_update(instr)
        else : print('Error: instrucción no válida')

#f = open("./entrada.txt", "r")

#input = f.read()
# otras pruebas de entrada
"""USAR intento;
CREATE TABLE tbdetallefactura ( 
iddetallefac int PRIMARY KEY, 
product_no int REFERENCE products (id), 
price decimal NOT NULL, 
cantidad int  
);
 
INSERT INTO tbdetallefactura(iddetallefac,price,cantidad) VALUES(1,1.00,23);

DELETE FROM products where id = 3;"""



input = """

USAR intento;

CREATE TABLE tbdetallefactura ( 
iddetallefac int PRIMARY KEY, 
price decimal NOT NULL, 
cantidad int ,
texto nvarchar(50)
);
 
INSERT INTO tbdetallefactura(iddetallefac,price,cantidad,texto) VALUES(1,2.23,23, "hola");
INSERT INTO tbdetallefactura(iddetallefac,price,cantidad,texto) VALUES(2,2.24,23, "col2");
INSERT INTO tbdetallefactura(iddetallefac,price,cantidad,texto) VALUES(3,3.00,21, "col3");
INSERT INTO tbdetallefactura(iddetallefac,price,cantidad,texto) VALUES(4,3.31,24, "hola");
DELETE FROM tbdetallefactura where texto == "hola" || iddetallefac == 2 ;
"""
instrucciones = g.parse(input.lower())
ts_global = TS.TablaSimbolo()

procesar_instrucciones(instrucciones)



