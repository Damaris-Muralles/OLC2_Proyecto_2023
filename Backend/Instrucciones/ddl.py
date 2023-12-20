
def procesar_usedatabase(instr):
    base = instr.get("id")
    return base

def procesar_createdatabase(instr,xml) :
    print(xml.add_database(instr.get("id")))
    return instr.get("id")

def procesar_createtable(instr,ActualBaseDatos,xml):
    print(xml.add_table_info(ActualBaseDatos, instr))

def procesar_dropcolumna(instr,ActualBaseDatos,xml):
    print(xml.drop_column(ActualBaseDatos, instr))

def procesar_addcolumna(instr,ActualBaseDatos,xml):
    print(xml.add_column(ActualBaseDatos, instr))

def procesar_droptable(instr,ActualBaseDatos,xml):
    print(xml.drop_table(ActualBaseDatos, instr))

def procesar_truncatetable(instr,ActualBaseDatos,xml):
    print(xml.truncate_table(ActualBaseDatos, instr))
