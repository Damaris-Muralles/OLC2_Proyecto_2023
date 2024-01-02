
from Analizadores.instrucciones import *
from BaseDatos.manejoxml import *
from Instrucciones.ddl import *
from Instrucciones.dml import *
from Instrucciones.Funciones.DeclararMetodo import *
from Instrucciones.Funciones.Llamar import *
from Instrucciones.Funciones.DeclararFuncion import *
from Expresiones.Where import *
ActualBaseDatos = ""
def Globales(instrucciones, entorno, xml, lsimbolo, lmetodo, imprimir):
    global ActualBaseDatos
    comprobador.tabla.clear()
    for instr in instrucciones :
        listatipodatos.clear()
        print("==================================================================================================================")
        #print("instruccion actual: ", instr)
        if instr.get('tipo') == TIPO_INSTRUCCION.CREATE_DATABASE : ActualBaseDatos=procesar_createdatabase(instr,xml,imprimir)
        elif instr.get('tipo') == TIPO_INSTRUCCION.CREATE_TABLE : procesar_createtable(instr,ActualBaseDatos,xml,imprimir)
        elif instr.get('tipo') == TIPO_INSTRUCCION.USE_DATABASE : ActualBaseDatos=procesar_usedatabase(instr)
        elif instr.get('tipo') == TIPO_INSTRUCCION.DROP_COLUMNA : procesar_dropcolumna(instr,ActualBaseDatos,xml,imprimir)
        elif instr.get('tipo') == TIPO_INSTRUCCION.ADD_COLUMNA : procesar_addcolumna(instr,ActualBaseDatos,xml,imprimir)
        elif instr.get('tipo') == TIPO_INSTRUCCION.DROP_TABLE : procesar_droptable(instr,ActualBaseDatos,xml,imprimir)
        elif instr.get('tipo') == TIPO_INSTRUCCION.TRUNCATE_TABLE : procesar_truncatetable(instr,ActualBaseDatos,xml,imprimir)
        elif instr.get('tipo') == TIPO_INSTRUCCION.INSERT_TABLE : procesar_insert(instr,ActualBaseDatos,xml,imprimir)
        elif instr.get('tipo') == TIPO_INSTRUCCION.DELETE_TABLE : procesar_delete(instr,ActualBaseDatos,xml,entorno,lsimbolo,imprimir)
        elif instr.get('tipo') == TIPO_INSTRUCCION.UPDATE_TABLE : procesar_update(instr,ActualBaseDatos,xml,entorno,lsimbolo,imprimir)
        elif instr.get('tipo') == TIPO_INSTRUCCION.SELECT_TABLE : procesar_select(instr,ActualBaseDatos,xml,entorno,lsimbolo,imprimir,1)

        elif instr.get('tipo') == TIPO_INSTRUCCION.PROCEDURE : 
            DeclararMetodos(instr,entorno,lmetodo) 
            mens= xml.AgregarPorcedure(ActualBaseDatos, instr)
            if mens.get('tipo')=="ERROR":
                imprimir.agregar("ERROR:\nConsulta: Create Procedure Fila: "+str(instr.get('linea'))+" Columna: "+str(instr.get('pos'))+f"\n{mens.get('dato')}")
            
        elif instr.get('tipo') == TIPO_INSTRUCCION.FUNCTION : 
            DeclararFuncion(instr,entorno,lmetodo)
            mens=xml.AgregarFuncion(ActualBaseDatos, instr)
            if mens.get('tipo')=="ERROR":
                imprimir.agregar("ERROR:\nConsulta: Create function Fila: "+str(instr.get('linea'))+" Columna: "+str(instr.get('pos'))+f"\n{mens.get('dato')}")

        elif instr.get('tipo') == TIPO_INSTRUCCION.LLAMAR_FUNCION : Llama(instr,entorno,lsimbolo,xml,ActualBaseDatos,imprimir)
        else : print('Error: instrucción no válida')
        print("==================================================================================================================")


