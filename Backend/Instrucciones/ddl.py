
def procesar_usedatabase(instr):
    base = instr.get("id")
    return base

def procesar_createdatabase(instr,xml,imprimir):
    mens=xml.add_database(instr.get("id"))
    if mens.get('tipo')=="ERROR":
        imprimir.agregar("ERROR:\nConsulta: Create data base Fila: "+str(instr.get('linea'))+" Columna: "+str(instr.get('pos'))+f"\n{mens.get('dato')}")
    return instr.get("id")

def procesar_createtable(instr,ActualBaseDatos,xml,imprimir):
    mens=xml.add_table_info(ActualBaseDatos, instr)
    if mens.get('tipo')=="ERROR":
       imprimir.agregar("ERROR:\nConsulta: Create table Fila: "+str(instr.get('linea'))+" Columna: "+str(instr.get('pos'))+f"\n{mens.get('dato')}")

def procesar_addcolumna(instr,ActualBaseDatos,xml,imprimir):
    mens=xml.add_column(ActualBaseDatos, instr)
    if mens.get('tipo')=="ERROR":
        imprimir.agregar("ERROR:\nConsulta: Alter add Fila: "+str(instr.get('linea'))+" Columna: "+str(instr.get('pos'))+f"\n{mens.get('dato')}")

# validar si es esta referenciada en otra tabla
def procesar_dropcolumna(instr,ActualBaseDatos,xml,imprimir):
    mens=xml.drop_column(ActualBaseDatos, instr)
    if mens.get('tipo')=="ERROR":
        imprimir.agregar("ERROR:\nConsulta: Alter drop Fila: "+str(instr.get('linea'))+" Columna: "+str(instr.get('pos'))+f"\n{mens.get('dato')}")

def procesar_droptable(instr,ActualBaseDatos,xml,imprimir):
    mens=xml.drop_table(ActualBaseDatos, instr)
    if mens.get('tipo')=="ERROR":
        print("ERROR:\nConsulta: droptable Fila: "+str(instr.get('linea'))+" Columna: "+str(instr.get('pos'))+f"\n{mens.get('dato')}")

def procesar_truncatetable(instr,ActualBaseDatos,xml,imprimir):
    mens=xml.truncate_table(ActualBaseDatos, instr)
    if mens.get('tipo')=="ERROR":
        imprimir.agregar("ERROR:\nConsulta: truncatetable Fila: "+str(instr.get('linea'))+" Columna: "+str(instr.get('pos'))+f"\n{mens.get('dato')}")
               