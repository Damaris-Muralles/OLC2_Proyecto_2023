import Analizadores.gramar as g
from Analizadores.instrucciones import *
from BaseDatos.manejoxml import *
from Instrucciones.ddl import *
from Instrucciones.dml import *
from Instrucciones.ssl import *

from Expresiones.Where import *
import tablasimbolo as TS

xml = XMLManejador("./BaseDatos/BasesDatos.xml")  
ActualBaseDatos = ""


def procesar_instrucciones(instrucciones) :
    ## lista de instrucciones recolectadas
    global ActualBaseDatos
    
    for instr in instrucciones :
        print("==================================================================================================================")
        print("instruccion actual: ", instr)
        if instr.get('tipo')== TIPO_INSTRUCCION.CREATE_DATABASE : ActualBaseDatos=procesar_createdatabase(instr,xml)
        elif instr.get('tipo') == TIPO_INSTRUCCION.CREATE_TABLE : procesar_createtable(instr,ActualBaseDatos,xml)
        elif instr.get('tipo') == TIPO_INSTRUCCION.USE_DATABASE : ActualBaseDatos=procesar_usedatabase(instr)
        elif instr.get('tipo') == TIPO_INSTRUCCION.DROP_COLUMNA : procesar_dropcolumna(instr,ActualBaseDatos,xml)
        elif instr.get('tipo') == TIPO_INSTRUCCION.ADD_COLUMNA : procesar_addcolumna(instr,ActualBaseDatos,xml)
        elif instr.get('tipo') == TIPO_INSTRUCCION.DROP_TABLE : procesar_droptable(instr,ActualBaseDatos,xml)
        elif instr.get('tipo') == TIPO_INSTRUCCION.TRUNCATE_TABLE : procesar_truncatetable(instr,ActualBaseDatos,xml)
        elif instr.get('tipo') == TIPO_INSTRUCCION.INSERT_TABLE : procesar_insert(instr,ActualBaseDatos,xml)
        elif instr.get('tipo') == TIPO_INSTRUCCION.DELETE_TABLE : procesar_delete(instr,ActualBaseDatos,xml)
        elif instr.get('tipo') == TIPO_INSTRUCCION.UPDATE_TABLE : procesar_update(instr,ActualBaseDatos,xml)
        else : print('Error: instrucción no válida')
        print("==================================================================================================================")

#f = open("./entrada.txt", "r")

#input = f.read()
# otras pruebas de entrada


input = """

USAR intento;

DELETE FROM products where  case 
 when edad > 18 and edad <= 25
 then 'Adolecente'
 when edad > 25 and edad <= 35
 then 'Adulto joven'
 when edad >35 and edad <= 45
 then 'Adulto Maduro'
 else 'Adulto Mayor'
 end;
"""
instrucciones = g.parse(input.lower())
ts_global = TS.TablaSimbolo()

procesar_instrucciones(instrucciones)



