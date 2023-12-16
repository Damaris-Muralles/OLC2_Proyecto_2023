
from instrucciones import *
import tablasimbolo as TS
from instrucciones import *
from manejoxml import *

xml = XMLManejador("./BasesDatos.xml")  

basedata = ""
table = ""

def procesar_where1(instr,base,tabla):
    global basedata
    basedata = base
    global table
    table = tabla

    if isinstance(instr, dict):
        if instr.get("tipo") == TIPO_OPERACION.MAYOR_QUE:
            
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
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
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
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
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
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
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
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
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
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
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
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
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
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
            
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
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

            exp1=procesar_where1(instr.get("exp1"), base, tabla)
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
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
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
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
            print("exp1: ",exp1," exp2: ",exp2)
            return [exp1,exp2]
        elif instr.get("tipo") == TIPO_OPERACION.RESTA:
            print("-")
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
            print("exp1: ",exp1," exp2: ",exp2)
            return [exp1,exp2]
        elif instr.get("tipo") == TIPO_OPERACION.MULTIPLICACION:
            print("*")
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
            print("exp1: ",exp1," exp2: ",exp2)
            return [exp1,exp2]
        elif instr.get("tipo") == TIPO_OPERACION.DIVISION:
            print("/")
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
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
            # se tiene que buscar en la tabla la columna correspondiente
            return xml.obtener_registros(basedata,table,cadena)
        
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