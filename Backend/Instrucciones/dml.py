from Expresiones.Where import *

def procesar_insert(instr,ActualBaseDatos,xml):
    print(xml.insert_data(ActualBaseDatos,instr))

def procesar_delete(instr,ActualBaseDatos,xml):

    #print(instr.get("where"))
    # solo para probar el where
    eliminar=procesar_where1(instr.get("where"),ActualBaseDatos, instr.get("id"))
    
    #print(xml.delete_registro(ActualBaseDatos, instr.get("id"),eliminar))

def procesar_update(instr,ActualBaseDatos,xml):
    print(instr)
    whereupdate = procesar_where1(instr.get("where"),ActualBaseDatos, instr.get("id"))
    listset = []

    for i in instr.get("set"):

        listset.append(procesar_where1(i.get("exp2"), ActualBaseDatos, instr.get("id")))

    print(listset)

    print(xml.UpdateTable(ActualBaseDatos, instr.get("id"),instr.get("set"), listset,whereupdate))

def procesar_select(instr,ActualBaseDatos,xml):
    pass

