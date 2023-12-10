import gramar as g
import tablasimbolo as TS
from instrucciones import *
from manejoxml import *

xml = XMLManejador("./BasesDatos.xml")

def procesar_createdatabase(instr) :
    print("create database")
    print(instr.get("idbase"))
    print(xml.add_database(instr.get("idbase")))

def procesar_instrucciones(instrucciones) :
    ## lista de instrucciones recolectadas
    for instr in instrucciones :
        if instr.get('tipo')== TIPO_INSTRUCCION.CREATE_DATABASE : procesar_createdatabase(instr)

#f = open("./entrada.txt", "r")

#input = f.read()
input = """
CREATE DATA BASE base_datos_1_prueba; 
"""
instrucciones = g.parse(input)
#ts_global = TS.TablaDeSimbolos()

procesar_instrucciones(instrucciones)
