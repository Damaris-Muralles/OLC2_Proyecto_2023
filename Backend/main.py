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
    #print(xml.delete_registro(ActualBaseDatos, instr.get("id"),[1]))
    
    # solo para probar el where
    procesar_where1(instr.get("where"))
    
def procesar_where1(instr):
    
    if isinstance(instr, dict):
        if instr.get("tipo") == TIPO_OPERACION.MAYOR_QUE:
            
            exp1=procesar_where1(instr.get("exp1"))
            exp2=procesar_where1(instr.get("exp2"))
            print(exp1," > ",exp2)
            exp1 = procesar_expresion(exp1)
            exp2 = procesar_expresion(exp2)
            respuesta = []
            listas=False
            if len(exp1)>1 and len(exp2)>1:
                listas=True

            for i in exp1:
                if listas:
                    if i > exp2[exp1.index(i)]:
                        respuesta.append(1)
                    else:
                        respuesta.append(0)
                else:
                    for j in exp2:
                        if i > j:
                            respuesta.append(1)
                        else:
                            respuesta.append(0)
            print("exp1: ",exp1," exp2: ",exp2)
            print("respuesta: ",respuesta)
            return respuesta
        elif instr.get("tipo") == TIPO_OPERACION.MENOR_QUE:
            exp1=procesar_where1(instr.get("exp1"))
            exp2=procesar_where1(instr.get("exp2"))
            print(exp1," <",exp2)
            exp1 = procesar_expresion(exp1)
            exp2 = procesar_expresion(exp2)
            respuesta = []
            listas=False
            if len(exp1)>1 and len(exp2)>1:
                listas=True
            for i in exp1:
                if listas:
                    if i < exp2[exp1.index(i)]:
                        respuesta.append(1)
                    else:
                        respuesta.append(0)
                else:
                    for j in exp2:
                        if i < j:
                            respuesta.append(1)
                        else:
                            respuesta.append(0)
            print("exp1: ",exp1," exp2: ",exp2)
            print("respuesta: ",respuesta)
            return respuesta
        elif instr.get("tipo") == TIPO_OPERACION.IGUAL_IGUAL or instr.get("tipo") == TIPO_OPERACION.IGUAL:
            exp1=procesar_where1(instr.get("exp1"))
            exp2=procesar_where1(instr.get("exp2"))
            print(exp1,"==",exp2)
            exp1 = procesar_expresion(exp1)
            exp2 = procesar_expresion(exp2)
            respuesta = []
            listas=False
            if len(exp1)>1 and len(exp2)>1:
                listas=True
            for i in exp1:
                if listas:
                    if i == exp2[exp1.index(i)]:
                        respuesta.append(1)
                    else:
                        respuesta.append(0)
                else:
                    for j in exp2:
                        if i == j:
                            respuesta.append(1)
                        else:
                            respuesta.append(0)
            print("exp1: ",exp1," exp2: ",exp2)
            print("respuesta: ",respuesta)
            return respuesta
        elif instr.get("tipo") == TIPO_OPERACION.NO_IGUAL:
            exp1=procesar_where1(instr.get("exp1"))
            exp2=procesar_where1(instr.get("exp2"))
            print(exp1," !=",exp2)
            exp1 = procesar_expresion(exp1)
            exp2 = procesar_expresion(exp2)
            respuesta = []
            listas=False
            if len(exp1)>1 and len(exp2)>1:
                listas=True
            for i in exp1:
                if listas:
                    if i != exp2[exp1.index(i)]:
                        respuesta.append(1)
                    else:
                        respuesta.append(0)
                else:
                    for j in exp2:
                        if i != j:
                            respuesta.append(1)
                        else:
                            respuesta.append(0)
            print("exp1: ",exp1," exp2: ",exp2)
            print("respuesta: ",respuesta)
            return respuesta
        elif instr.get("tipo") == TIPO_OPERACION.MAYOR_IGUAL:
            exp1=procesar_where1(instr.get("exp1"))
            exp2=procesar_where1(instr.get("exp2"))
            print(exp1," >=",exp2)
            exp1 = procesar_expresion(exp1)
            exp2 = procesar_expresion(exp2)
            respuesta = []
            listas=False
            if len(exp1)>1 and len(exp2)>1:
                listas=True
            for i in exp1:
                if listas:
                    if i >= exp2[exp1.index(i)]:
                        respuesta.append(1)
                    else:
                        respuesta.append(0)
                else:
                    for j in exp2:
                        if i >= j:
                            respuesta.append(1)
                        else:
                            respuesta.append(0)
            print("exp1: ",exp1," exp2: ",exp2)
            print("respuesta: ",respuesta)
            return respuesta
        elif instr.get("tipo") == TIPO_OPERACION.MENOR_IGUAL:
            exp1=procesar_where1(instr.get("exp1"))
            exp2=procesar_where1(instr.get("exp2"))
            print(exp1," <=",exp2)
            exp1 = procesar_expresion(exp1)
            exp2 = procesar_expresion(exp2)
            respuesta = []
            listas=False
            if len(exp1)>1 and len(exp2)>1:
                listas=True
            for i in exp1:
                if listas:
                    if i <= exp2[exp1.index(i)]:
                        respuesta.append(1)
                    else:
                        respuesta.append(0)
                else:
                    for j in exp2:
                        if i <= j:
                            respuesta.append(1)
                        else:
                            respuesta.append(0)
            print("exp1: ",exp1," exp2: ",exp2)
            print("respuesta: ",respuesta)
            return respuesta
        elif instr.get("tipo") == TIPO_OPERACION.AND:
            exp1=procesar_where1(instr.get("exp1"))
            exp2=procesar_where1(instr.get("exp2"))
            print(exp1, "&&", exp2)
            exp1 = procesar_expresion(exp1)
            exp2 = procesar_expresion(exp2)
            respuesta = []
            listas=False
            if len(exp1)>1 and len(exp2)>1:
                listas=True

            for i in exp1:
                if listas:
                    if i==1 and exp2[exp1.index(i)]==1:
                        respuesta.append(1)
                    else:
                        respuesta.append(0)
                else:
                    for j in exp2:
                        if i==1 and j==1:
                            respuesta.append(1)
                        else:
                            respuesta.append(0) 

            print("exp1: ",exp1," exp2: ",exp2)
            print("respuesta: ",respuesta)
            
            return respuesta
        elif instr.get("tipo") == TIPO_OPERACION.OR:
            
            exp1=procesar_where1(instr.get("exp1"))
            exp2=procesar_where1(instr.get("exp2"))
            print(exp1, "||", exp2)
            exp1 = procesar_expresion(exp1)
            exp2 = procesar_expresion(exp2)
            respuesta = []
            listas=False
            if len(exp1)>1 and len(exp2)>1:
                listas=True

            for i in exp1:
                if listas:
                    if i==1 or exp2[exp1.index(i)]==1:
                        respuesta.append(1)
                    else:
                        respuesta.append(0)
                else:
                    for j in exp2:
                        if i==1 or j==1:
                            respuesta.append(1)
                        else:
                            respuesta.append(0) 

            print("exp1: ",exp1," exp2: ",exp2)
            print("respuesta: ",respuesta)
            
            return respuesta
        elif instr.get("tipo") == TIPO_OPERACION.NOT:

            exp1=procesar_where1(instr.get("exp1"))
            print("!", exp1)
            exp1 = procesar_expresion(exp1)
            respuesta = []
            listas=False
            for i in exp1:
                respuesta.append(not i)

            print("exp1: ",exp1)
            print("respuesta: ",respuesta)
            
            return respuesta
        elif instr.get("tipo") == TIPO_OPERACION.BETWEEN:
            exp1=procesar_where1(instr.get("exp1"))
            exp2=procesar_where1(instr.get("exp2").get("exp1"))
            exp3=procesar_where1(instr.get("exp2").get("exp2"))
            print(exp1, "esta entre", exp2 , " y ", exp3)
            exp1 = procesar_expresion(exp1)
            exp2 = procesar_expresion(exp2)
            exp3 = procesar_expresion(exp3)
            respuesta = []
            listas=False
            if len(exp1)>1 and len(exp2)>1 and len(exp3)>1:
                listas=True

            for i in exp1:
                if listas:
                    if exp2[exp1.index(i)]<=i<= exp3[exp1.index(i)]==1:
                        respuesta.append(1)
                    else:
                        respuesta.append(0)
                else:
                    if exp2[0]<=i<=exp3[0]:
                        respuesta.append(1)
                    else:
                        respuesta.append(0)
                   

            print("exp1: ",exp1," exp2: ",exp2)
            print("respuesta: ",respuesta)
            
            return respuesta
        elif instr.get("tipo") == TIPO_OPERACION.SUMA:
            print("+")
            exp1=procesar_where1(instr.get("exp1"))
            exp2=procesar_where1(instr.get("exp2"))
            print("exp1: ",exp1," exp2: ",exp2)
            return [exp1,exp2]
        elif instr.get("tipo") == TIPO_OPERACION.RESTA:
            print("-")
            exp1=procesar_where1(instr.get("exp1"))
            exp2=procesar_where1(instr.get("exp2"))
            print("exp1: ",exp1," exp2: ",exp2)
            return [exp1,exp2]
        elif instr.get("tipo") == TIPO_OPERACION.MULTIPLICACION:
            print("*")
            exp1=procesar_where1(instr.get("exp1"))
            exp2=procesar_where1(instr.get("exp2"))
            print("exp1: ",exp1," exp2: ",exp2)
            return [exp1,exp2]
        elif instr.get("tipo") == TIPO_OPERACION.DIVISION:
            print("/")
            exp1=procesar_where1(instr.get("exp1"))
            exp2=procesar_where1(instr.get("exp2"))
            print("exp1: ",exp1," exp2: ",exp2)
            return exp1/exp2
        
        else:
            # para funciones del sistema
            print(instr.get("tipo").name)
            print(instr)
    else:
        
        return instr
    
def procesar_expresion(cadena):
    # si expresion contine comillas dobles o simples escribir algo
   
    if isinstance(cadena, str):
        if not cadena.startswith('\"') or not cadena.startswith('\''):
            # comprobar si es una fecha con nel formato dd-mm-yyyy o dd-mm-yyyy hh:mm:ss
            if cadena.count('-') == 2:
                return [cadena]
            
            # se tiene que buscar en la tabla la columna correspondiente
            return [1,2,3]
        elif cadena.startswith('@'):
            # se tiene que buscar en la tabla de simbolos
            return [5]
        else:
            return [cadena]
    else:
        if isinstance(cadena, list):
            return cadena
        else:
            return [cadena]


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

DELETE FROM products where id = 3;
DELETE FROM tbvalores
WHERE id > 3 OR id < 100;

"""
instrucciones = g.parse(input.lower())
ts_global = TS.TablaSimbolo()

procesar_instrucciones(instrucciones)



