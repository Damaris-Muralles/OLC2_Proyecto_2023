
from Analizadores.instrucciones import *
from BaseDatos.manejoxml import *
from Instrucciones.ddl import *
from Instrucciones.dml import *
from Instrucciones.Funciones.DeclararVariable import *
from Instrucciones.Funciones.AsignarVariables import *
from Instrucciones.Funciones.Si import *
from Instrucciones.Funciones.Ciclo import *
from Instrucciones.Funciones.Retornar import *
from Instrucciones.Funciones.Llamar import *
from Expresiones.Where import *
from Instrucciones.Funciones.Caso import *

def Local(instrucciones, entorno, xml,ActualBaseDatos, lsimbolo,imprimir):
    retornar = ""
    comprobador.tabla.clear()
    for instr in instrucciones :
        if listatipodatos and listatipodatos[-1] == "ERROR":
            listatipodatos.pop()
        #print("==================================================================================================================")
        #print("instruccion actual: ", instr)
        if instr.get('tipo') == TIPO_INSTRUCCION.CREATE_TABLE : procesar_createtable(instr,ActualBaseDatos,xml,imprimir)
        elif instr.get('tipo') == TIPO_INSTRUCCION.DROP_COLUMNA : procesar_dropcolumna(instr,ActualBaseDatos,xml,imprimir)
        elif instr.get('tipo') == TIPO_INSTRUCCION.ADD_COLUMNA : procesar_addcolumna(instr,ActualBaseDatos,xml,imprimir)
        elif instr.get('tipo') == TIPO_INSTRUCCION.DROP_TABLE : procesar_droptable(instr,ActualBaseDatos,xml,imprimir)
        elif instr.get('tipo') == TIPO_INSTRUCCION.TRUNCATE_TABLE : procesar_truncatetable(instr,ActualBaseDatos,xml,imprimir)
        elif instr.get('tipo') == TIPO_INSTRUCCION.INSERT_TABLE : procesar_insert(instr,ActualBaseDatos,xml,imprimir)
        elif instr.get('tipo') == TIPO_INSTRUCCION.DELETE_TABLE : procesar_delete(instr,ActualBaseDatos,xml,entorno,lsimbolo,imprimir)
        elif instr.get('tipo') == TIPO_INSTRUCCION.UPDATE_TABLE : procesar_update(instr,ActualBaseDatos,xml,entorno,lsimbolo,imprimir)
        
        elif instr.get('tipo') == TIPO_INSTRUCCION.LLAMAR_FUNCION : Llama(instr,entorno,lsimbolo,xml,ActualBaseDatos,imprimir)
        elif instr.get('tipo') == TIPO_INSTRUCCION.DECLARAR_VARIABLE : DeclararVariables(instr, entorno, entorno.nombre, lsimbolo,imprimir)
        elif instr.get('tipo') == TIPO_INSTRUCCION.ASIGNACION_VARIABLE : asignarVariable(instr,entorno,lsimbolo,imprimir)
        elif instr.get('tipo') == TIPO_INSTRUCCION.IF : Si(instr, entorno, lsimbolo, xml, ActualBaseDatos,imprimir)
        elif instr.get('tipo') == TIPO_INSTRUCCION.CWHILE : CicloW(instr, entorno, lsimbolo, xml, ActualBaseDatos,imprimir)
        elif instr.get('tipo') == TIPO_INSTRUCCION.CASE : Caso(instr, entorno, lsimbolo, xml, ActualBaseDatos,imprimir)
        elif instr.get('tipo') == TIPO_INSTRUCCION.RETORNAR : 
            retornar = RetornarI(instr, entorno, lsimbolo, xml, ActualBaseDatos,imprimir)
            return retornar
        
        else : print('Error: instrucción no válida')
        #print("==================================================================================================================")
