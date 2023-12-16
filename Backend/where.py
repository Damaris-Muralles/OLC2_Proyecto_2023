
from datetime import datetime
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
            
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
            print(exp1, "+", exp2)
            exp1 = procesar_expresion(exp1)
            exp2 = procesar_expresion(exp2)

            #tipo de dato:
            tipo1=""
            tipo2=""
            if isinstance(exp1, dict):
                tipo1 = exp1.get("tipo")
            if isinstance(exp2, dict):
                tipo2 = exp2.get("tipo")


            respuesta = []
            listas=False
            if len(exp1)>1 and len(exp2)>1:
                listas=True
            
            for i in exp1:
                if listas:
                    dat = 0
                    if (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and (exp2[exp1.index(i)]==1 or exp2[exp1.index(i)]==0)) or ((i==1 or i==0) and (exp2[exp1.index(i)]==1 or exp2[exp1.index(i)]==0)):
                        dat = i or exp2[exp1.index(i)]
                    elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(exp2[exp1.index(i)],int)) or ((i==1 or i==0) and isinstance(exp2[exp1.index(i)],int)):
                        dat = int(i + exp2[exp1.index(i)])
                    elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(exp2[exp1.index(i)],float)) or ((i==1 or i==0) and isinstance(exp2[exp1.index(i)],float)):
                        dat = float(i + exp2[exp1.index(i)])
                    elif (tipo1==TIPO_DATO.BIT and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR) ) or ((tipo2==TIPO_DATO.CHAR or tipo2 == TIPO_DATO.VARCHAR) and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(exp2[exp1.index(i)],str)) or ((i==1 or i==0) and isinstance(exp2[exp1.index(i)],str)) and (is_date_or_datetime(exp2[exp1.index(i)])==False):
                        dat = str(i) + str(exp2[exp1.index(i)])
                    elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and (exp2[exp1.index(i)]==1 or exp2[exp1.index(i)]==0)) or ((exp2[exp1.index(i)]==1 or exp2[exp1.index(i)]==0) and isinstance(i,int)):
                        dat = int(i + exp2[exp1.index(i)])
                    elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(exp2[exp1.index(i)],int)) or (isinstance(i,int) and isinstance(exp2[exp1.index(i)],int)):
                        dat = int(i + exp2[exp1.index(i)])
                    elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(exp2[exp1.index(i)],float)) or (isinstance(i,int) and isinstance(exp2[exp1.index(i)],float)):
                        dat = float(i + exp2[exp1.index(i)])
                    elif (tipo1==TIPO_DATO.INT and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR) ) or ((tipo2==TIPO_DATO.CHAR or tipo2 == TIPO_DATO.VARCHAR) and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(exp2[exp1.index(i)],str)) or (isinstance(i,int) and isinstance(exp2[exp1.index(i)],str)) and (is_date_or_datetime(exp2[exp1.index(i)])==False):
                        dat = str(i) + str(exp2[exp1.index(i)])
                    elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and (exp2[exp1.index(i)]==1 or exp2[exp1.index(i)]==0)) or ((i==1 or i==0) and isinstance(exp2[exp1.index(i)],float)):
                        dat = float(i + exp2[exp1.index(i)])
                    elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(exp2[exp1.index(i)],int)) or (isinstance(i,float) and isinstance(exp2[exp1.index(i)],int)):
                        dat = float(i + exp2[exp1.index(i)])
                    elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(exp2[exp1.index(i)],float)) or (isinstance(i,float) and isinstance(exp2[exp1.index(i)],float)):
                        dat = float(i + exp2[exp1.index(i)])
                    elif (tipo1==TIPO_DATO.DECIMAL and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR) ) or ((tipo2==TIPO_DATO.CHAR or tipo2 == TIPO_DATO.VARCHAR) and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(exp2[exp1.index(i)],str)) or (isinstance(i,float) and isinstance(exp2[exp1.index(i)],str)) and (is_date_or_datetime(exp2[exp1.index(i)])==False):
                        dat = str(i) + str(exp2[exp1.index(i)])
                    elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and tipo2==TIPO_DATO.BIT) or ((tipo1==TIPO_DATO.CHAR or tipo1 == TIPO_DATO.VARCHAR) and (exp2[exp1.index(i)]==1 or exp2[exp1.index(i)]==0)) or (tipo2==TIPO_DATO.BIT and isinstance(i,str)) or (isinstance(i,str) and (exp2[exp1.index(i)]==1 or exp2[exp1.index(i)]==0)) and (is_date_or_datetime(i)==False):
                        dat = str(i) + str(exp2[exp1.index(i)])
                    elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and tipo2==TIPO_DATO.INT) or ((tipo1==TIPO_DATO.CHAR or tipo1 == TIPO_DATO.VARCHAR) and isinstance(exp2[exp1.index(i)],int)) or (tipo2==TIPO_DATO.INT and isinstance(i,str)) or (isinstance(i,str) and isinstance(exp2[exp1.index(i)],int)) and (is_date_or_datetime(i)==False):
                        dat = str(i) + str(exp2[exp1.index(i)])
                    elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and tipo2==TIPO_DATO.DECIMAL) or ((tipo1==TIPO_DATO.CHAR or tipo1 == TIPO_DATO.VARCHAR) and isinstance(exp2[exp1.index(i)],float)) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,str)) or (isinstance(i,str) and isinstance(exp2[exp1.index(i)],float)) and (is_date_or_datetime(i)==False):
                        dat = str(i) + str(exp2[exp1.index(i)])
                    elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR) and   isinstance(i,str)) or ((tipo1==TIPO_DATO.CHAR or tipo1 == TIPO_DATO.VARCHAR) and isinstance(exp2[exp1.index(i)],str)) or (isinstance(i,str) and isinstance(exp2[exp1.index(i)],str)) and (is_date_or_datetime(i)==False):
                        dat = str(i) + str(exp2[exp1.index(i)])
                    else:
                        print("Error: no se puede sumar los valores "+str(i)+" y "+str(exp2[exp1.index(i)]))
                        return
                        
                    
                    respuesta.append(dat)
                else:
                    for j in exp2:
                        dat = 0
                        if (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and (j==1 or j==0)) or ((j==1 or j==0) and (i==1 or i==0)):
                            dat = i or j
                        elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(j,int)) or ((i==1 or i==0) and isinstance(j,int)):
                            dat = int(i + j)
                        elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(j,float)) or ((i==1 or i==0) and isinstance(j,float)):
                            dat = float(i + j)
                        elif (tipo1==TIPO_DATO.BIT and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR) ) or ((tipo2==TIPO_DATO.CHAR or tipo2 == TIPO_DATO.VARCHAR) and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(j,str)) or ((i==1 or i==0) and isinstance(j,str)) and (is_date_or_datetime(j)==False):
                            dat = str(i) + str(j)
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and (j==1 or j==0) ) or ((j==1 or j==0) and isinstance(i,int)):
                            dat = int(i + j)
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(j,int)) or (isinstance(i,int) and isinstance(j,int)):
                            dat = int(i + j)
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(j,float)) or (isinstance(i,int) and isinstance(j,float)):
                            dat = float(i + j)
                        elif (tipo1==TIPO_DATO.INT and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR) ) or ((tipo2==TIPO_DATO.CHAR or tipo2 == TIPO_DATO.VARCHAR) and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(j,str)) or (isinstance(i,int) and isinstance(j,str)) and (is_date_or_datetime(j)==False):
                            dat = str(i) + str(j)
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and (j==1 or j==0)) or (isinstance(i,float) and (j==1 or j==0)):
                            dat = float(i + j)
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(j,int)) or (isinstance(i,float) and isinstance(j,int)):
                            dat = float(i + j)
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(j,float)) or (isinstance(i,float) and isinstance(j,float)):
                            dat = float(i + j)
                        elif (tipo1==TIPO_DATO.DECIMAL and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR) ) or ((tipo2==TIPO_DATO.CHAR or tipo2 == TIPO_DATO.VARCHAR) and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(j,str)) or (isinstance(i,float) and isinstance(j,str)) and (is_date_or_datetime(j)==False):
                            dat = str(i) + str(j)
                        elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and tipo2==TIPO_DATO.BIT) or ((tipo1==TIPO_DATO.CHAR or tipo1 == TIPO_DATO.VARCHAR) and (j==1 or j==0)) or (tipo2==TIPO_DATO.BIT and isinstance(i,str)) or (isinstance(i,str) and (j==1 or j==0)) and (is_date_or_datetime(i)==False):
                            dat = str(i) + str(j)
                        elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and tipo2==TIPO_DATO.INT) or ((tipo1==TIPO_DATO.CHAR or tipo1 == TIPO_DATO.VARCHAR) and isinstance(j,int)) or (tipo2==TIPO_DATO.INT and isinstance(i,str)) or (isinstance(i,str) and isinstance(j,int)) and (is_date_or_datetime(i)==False):
                            dat = str(i) + str(j)
                        elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and tipo2==TIPO_DATO.DECIMAL) or ((tipo1==TIPO_DATO.CHAR or tipo1 == TIPO_DATO.VARCHAR) and isinstance(j,float)) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,str)) or (isinstance(i,str) and isinstance(j,float)) and (is_date_or_datetime(i)==False):

                            dat = str(i) + str(j)
                        elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR) and   isinstance(i,str)) or ((tipo1==TIPO_DATO.CHAR or tipo1 == TIPO_DATO.VARCHAR) and isinstance(j,str)) or (isinstance(i,str) and isinstance(j,str)) and (is_date_or_datetime(i)==False):
                            dat = str(i) + str(j)
                        else:
                            print("Error: no se puede sumar los valores "+str(i)+" y "+str(j))
                            return
                            
                        
                        respuesta.append(dat)   

            print("exp1: ",exp1," exp2: ",exp2)
            print("respuesta: ",respuesta)
            
            return respuesta
        elif instr.get("tipo") == TIPO_OPERACION.RESTA:
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
            print(exp1, "-", exp2)
            exp1 = procesar_expresion(exp1)
            exp2 = procesar_expresion(exp2)

            #tipo de dato:
            tipo1=""
            tipo2=""
            if isinstance(exp1, dict):
                tipo1 = exp1.get("tipo")
            if isinstance(exp2, dict):
                tipo2 = exp2.get("tipo")


            respuesta = []
            listas=False
            if len(exp1)>1 and len(exp2)>1:
                listas=True
            
            for i in exp1:
                if listas:
                    dat = 0
                    if (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(exp2[exp1.index(i)],int)) or ((i==1 or i==0) and isinstance(exp2[exp1.index(i)],int)):
                        dat = int(i - exp2[exp1.index(i)])
                    elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(exp2[exp1.index(i)],float)) or ((i==1 or i==0) and isinstance(exp2[exp1.index(i)],float)):
                        dat = float(i . exp2[exp1.index(i)])
                    elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and (exp2[exp1.index(i)]==1 or exp2[exp1.index(i)]==0)) or ((exp2[exp1.index(i)]==1 or exp2[exp1.index(i)]==0) and isinstance(i,int)):
                        dat = int(i - exp2[exp1.index(i)])
                    elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(exp2[exp1.index(i)],int)) or (isinstance(i,int) and isinstance(exp2[exp1.index(i)],int)):
                        dat = int(i - exp2[exp1.index(i)])
                    elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(exp2[exp1.index(i)],float)) or (isinstance(i,int) and isinstance(exp2[exp1.index(i)],float)):
                        dat = float(i - exp2[exp1.index(i)])
                    elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and (exp2[exp1.index(i)]==1 or exp2[exp1.index(i)]==0)) or ((i==1 or i==0) and isinstance(exp2[exp1.index(i)],float)):
                        dat = float(i - exp2[exp1.index(i)])
                    elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(exp2[exp1.index(i)],int)) or (isinstance(i,float) and isinstance(exp2[exp1.index(i)],int)):
                        dat = float(i - exp2[exp1.index(i)])
                    elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(exp2[exp1.index(i)],float)) or (isinstance(i,float) and isinstance(exp2[exp1.index(i)],float)):
                        dat = float(i - exp2[exp1.index(i)])
                    
                    else:
                        print("Error: no se puede sumar los valores "+str(i)+" y "+str(exp2[exp1.index(i)]))
                        return
                        
                    
                    respuesta.append(dat)
                else:
                    for j in exp2:
                        dat = 0
                        
                        if (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(j,int)) or ((i==1 or i==0) and isinstance(j,int)):
                            dat = int(i - j)
                        elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(j,float)) or ((i==1 or i==0) and isinstance(j,float)):
                            dat = float(i - j)
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and (j==1 or j==0)) or ((j==1 or j==0) and isinstance(i,int)):
                            dat = int(i - j)
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(j,int)) or (isinstance(i,int) and isinstance(j,int)):
                            dat = int(i - j)
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(j,float)) or (isinstance(i,int) and isinstance(j,float)):
                            dat = float(i - j)
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and (j==1 or j==0)) or ((j==1 or j==0) and isinstance(i,float)):
                            dat = float(i - j)
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(j,int)) or (isinstance(i,float) and isinstance(j,int)):
                            dat = float(i - j)
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(j,float)) or (isinstance(i,float) and isinstance(j,float)):
                            dat = float(i - j)
                        else:
                            print("Error: no se puede sumar los valores "+str(i)+" y "+str(j))
                            return
                            
                        
                        respuesta.append(dat)   

            print("exp1: ",exp1," exp2: ",exp2)
            print("respuesta: ",respuesta)
            
            return respuesta
        elif instr.get("tipo") == TIPO_OPERACION.MULTIPLICACION:
            
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
            print(exp1, "*", exp2)
            exp1 = procesar_expresion(exp1)
            exp2 = procesar_expresion(exp2)

            #tipo de dato:
            tipo1=""
            tipo2=""
            if isinstance(exp1, dict):
                tipo1 = exp1.get("tipo")
            if isinstance(exp2, dict):
                tipo2 = exp2.get("tipo")


            respuesta = []
            listas=False
            if len(exp1)>1 and len(exp2)>1:
                listas=True
            
            for i in exp1:
                if listas:
                    dat = 0
                    if (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and (exp2[exp1.index(i)]==1 or exp2[exp1.index(i)]==0)) or ((i==1 or i==0) and (exp2[exp1.index(i)]==1 or exp2[exp1.index(i)]==0)):
                        dat = i and exp2[exp1.index(i)]
                    elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(exp2[exp1.index(i)],int)) or ((i==1 or i==0) and isinstance(exp2[exp1.index(i)],int)):
                        dat = int(i * exp2[exp1.index(i)])
                    elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(exp2[exp1.index(i)],float)) or ((i==1 or i==0) and isinstance(exp2[exp1.index(i)],float)):
                        dat = float(i * exp2[exp1.index(i)])
                    elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and (exp2[exp1.index(i)]==1 or exp2[exp1.index(i)]==0)) or ((exp2[exp1.index(i)]==1 or exp2[exp1.index(i)]==0) and isinstance(i,int)):
                        dat = int(i * exp2[exp1.index(i)])
                    elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(exp2[exp1.index(i)],int)) or (isinstance(i,int) and isinstance(exp2[exp1.index(i)],int)):
                        dat = int(i * exp2[exp1.index(i)])
                    elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(exp2[exp1.index(i)],float)) or (isinstance(i,int) and isinstance(exp2[exp1.index(i)],float)):
                        dat = float(i * exp2[exp1.index(i)])
                    elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and (exp2[exp1.index(i)]==1 or exp2[exp1.index(i)]==0)) or ((i==1 or i==0) and isinstance(exp2[exp1.index(i)],float)):
                        dat = float(i * exp2[exp1.index(i)])
                    elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(exp2[exp1.index(i)],int)) or (isinstance(i,float) and isinstance(exp2[exp1.index(i)],int)):
                        dat = float(i * exp2[exp1.index(i)])
                    elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(exp2[exp1.index(i)],float)) or (isinstance(i,float) and isinstance(exp2[exp1.index(i)],float)):
                        dat = float(i * exp2[exp1.index(i)])
                    elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.DATE or tipo2==TIPO_DATO.DATETIME )) or ((tipo2==TIPO_DATO.DATE or tipo2 == TIPO_DATO.DATETIME) and isinstance(i,str)) or ((tipo1==TIPO_DATO.CHAR or tipo1 == TIPO_DATO.VARCHAR) and is_date_or_datetime(j)) or (is_date_or_datetime(i) and isinstance(exp2[exp1.index(i)],str)):
                        dat = str(i) + str(exp2[exp1.index(i)])
                    elif ((tipo1==TIPO_DATO.DATE or tipo1==TIPO_DATO.DATETIME) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR )) or ((tipo2==TIPO_DATO.CHAR or tipo2 == TIPO_DATO.VARCHAR) and is_date_or_datetime(i)) or ((tipo1==TIPO_DATO.DATE or tipo1 == TIPO_DATO.DATETIME) and isinstance(exp2[exp1.index(i)],str)) or (is_date_or_datetime(i) and isinstance(exp2[exp1.index(i)],str)):
                        dat = str(i) + str(exp2[exp1.index(i)])
                    else:
                        print("Error: no se puede sumar los valores "+str(i)+" y "+str(exp2[exp1.index(i)]))
                        return
                        
                    
                    respuesta.append(dat)
                else:
                    for j in exp2:
                        dat = 0
                        if (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and (j==1 or j==0)) or ((j==1 or j==0) and (i==1 or i==0)):
                            dat = i and j
                        elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(j,int)) or ((i==1 or i==0) and isinstance(j,int)):
                            dat = int(i * j)
                        elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(j,float)) or ((i==1 or i==0) and isinstance(j,float)):
                            dat = float(i * j)
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and (j==1 or j==0)) or ((j==1 or j==0) and isinstance(i,int)):
                            dat = int(i * j)
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(j,int)) or (isinstance(i,int) and isinstance(j,int)):
                            dat = int(i * j)
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(j,float)) or (isinstance(i,int) and isinstance(j,float)):
                            dat = float(i * j)
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and (j==1 or j==0)) or ((j==1 or j==0) and isinstance(i,float)):
                            dat = float(i * j)
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(j,int)) or (isinstance(i,float) and isinstance(j,int)):
                            dat = float(i * j)
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(j,float)) or (isinstance(i,float) and isinstance(j,float)):
                            dat = float(i * j)
                        elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.DATE or tipo2==TIPO_DATO.DATETIME )) or ((tipo2==TIPO_DATO.DATE or tipo2 == TIPO_DATO.DATETIME) and isinstance(i,str)) or ((tipo1==TIPO_DATO.CHAR or tipo1 == TIPO_DATO.VARCHAR) and is_date_or_datetime(j)) or (is_date_or_datetime(i) and isinstance(j,str)):
                            dat = str(i) + str(j)
                        elif ((tipo1==TIPO_DATO.DATE or tipo1==TIPO_DATO.DATETIME) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR )) or ((tipo2==TIPO_DATO.CHAR or tipo2 == TIPO_DATO.VARCHAR) and is_date_or_datetime(i)) or ((tipo1==TIPO_DATO.DATE or tipo1 == TIPO_DATO.DATETIME) and isinstance(j,str)) or (is_date_or_datetime(i) and isinstance(j,str)):
                            dat = str(i) + str(j)
                        else:
                            print("Error: no se puede sumar los valores "+str(i)+" y "+str(j))
                            return
                            
                        
                        respuesta.append(dat)   

            print("exp1: ",exp1," exp2: ",exp2)
            print("respuesta: ",respuesta)
            
            return respuesta
        elif instr.get("tipo") == TIPO_OPERACION.DIVISION:
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
            print(exp1, "/", exp2)
            exp1 = procesar_expresion(exp1)
            exp2 = procesar_expresion(exp2)

            #tipo de dato:
            tipo1=""
            tipo2=""
            if isinstance(exp1, dict):
                tipo1 = exp1.get("tipo")
            if isinstance(exp2, dict):
                tipo2 = exp2.get("tipo")


            respuesta = []
            listas=False
            if len(exp1)>1 and len(exp2)>1:
                listas=True
            
            for i in exp1:
                try:
                    if listas:
                        dat = 0
                        if (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(exp2[exp1.index(i)],int)) or ((i==1 or i==0) and isinstance(exp2[exp1.index(i)],int)):
                            dat = int(i / exp2[exp1.index(i)])
                        elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(exp2[exp1.index(i)],float)) or ((i==1 or i==0) and isinstance(exp2[exp1.index(i)],float)):
                            dat = float(i / exp2[exp1.index(i)])
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and (exp2[exp1.index(i)]==1 or exp2[exp1.index(i)]==0)) or ((exp2[exp1.index(i)]==1 or exp2[exp1.index(i)]==0) and isinstance(i,int)):
                            dat = int(i / exp2[exp1.index(i)])
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(exp2[exp1.index(i)],int)) or (isinstance(i,int) and isinstance(exp2[exp1.index(i)],int)):
                            dat = int(i / exp2[exp1.index(i)])
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(exp2[exp1.index(i)],float)) or (isinstance(i,int) and isinstance(exp2[exp1.index(i)],float)):
                            dat = float(i / exp2[exp1.index(i)])
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and (exp2[exp1.index(i)]==1 or exp2[exp1.index(i)]==0)) or ((i==1 or i==0) and isinstance(exp2[exp1.index(i)],float)):
                            dat = float(i / exp2[exp1.index(i)])
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(exp2[exp1.index(i)],int)) or (isinstance(i,float) and isinstance(exp2[exp1.index(i)],int)):
                            dat = float(i / exp2[exp1.index(i)])
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(exp2[exp1.index(i)],float)) or (isinstance(i,float) and isinstance(exp2[exp1.index(i)],float)):
                            dat = float(i / exp2[exp1.index(i)])
                        elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.DATE or tipo2==TIPO_DATO.DATETIME )) or ((tipo2==TIPO_DATO.DATE or tipo2 == TIPO_DATO.DATETIME) and isinstance(i,str)) or ((tipo1==TIPO_DATO.CHAR or tipo1 == TIPO_DATO.VARCHAR) and is_date_or_datetime(exp2[exp1.index(i)])) or (is_date_or_datetime(i) and isinstance(exp2[exp1.index(i)],str)):
                            dat = str(i) + str(exp2[exp1.index(i)])
                        elif ((tipo1==TIPO_DATO.DATE or tipo1==TIPO_DATO.DATETIME) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR )) or ((tipo2==TIPO_DATO.CHAR or tipo2 == TIPO_DATO.VARCHAR) and is_date_or_datetime(i)) or ((tipo1==TIPO_DATO.DATE or tipo1 == TIPO_DATO.DATETIME) and isinstance(exp2[exp1.index(i)],str)) or (is_date_or_datetime(i) and isinstance(exp2[exp1.index(i)],str)):
                            dat = str(i) + str(exp2[exp1.index(i)])
                        else:
                            print("Error: no se puede sumar los valores "+str(i)+" y "+str(exp2[exp1.index(i)]))
                            return
                            
                        
                        respuesta.append(dat)
                    else:
                        for j in exp2:
                            dat = 0
                            if (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(j,int)) or ((i==1 or i==0) and isinstance(j,int)):
                                dat = int(i / j)
                            elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(j,float)) or ((i==1 or i==0) and isinstance(j,float)):
                                dat = float(i / j)
                            elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and (j==1 or j==0)) or ((j==1 or j==0) and isinstance(i,int)):
                                dat = int(i / j)
                            elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(j,int)) or (isinstance(i,int) and isinstance(j,int)):
                                dat = int(i / j)
                            elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(j,float)) or (isinstance(i,int) and isinstance(j,float)):
                                dat = float(i / j)
                            elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and (j==1 or j==0)) or ((j==1 or j==0) and isinstance(i,float)):
                                dat = float(i / j)
                            elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(j,int)) or (isinstance(i,float) and isinstance(j,int)):
                                dat = float(i / j)
                            elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(j,float)) or (isinstance(i,float) and isinstance(j,float)):
                                dat = float(i / j)
                            elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.DATE or tipo2==TIPO_DATO.DATETIME )) or ((tipo2==TIPO_DATO.DATE or tipo2 == TIPO_DATO.DATETIME) and isinstance(i,str)) or ((tipo1==TIPO_DATO.CHAR or tipo1 == TIPO_DATO.VARCHAR) and is_date_or_datetime(j)) or (is_date_or_datetime(i) and isinstance(j,str)):
                                dat = str(i) + str(j)
                            elif ((tipo1==TIPO_DATO.DATE or tipo1==TIPO_DATO.DATETIME) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR )) or ((tipo2==TIPO_DATO.CHAR or tipo2 == TIPO_DATO.VARCHAR) and is_date_or_datetime(i)) or ((tipo1==TIPO_DATO.DATE or tipo1 == TIPO_DATO.DATETIME) and isinstance(j,str)) or (is_date_or_datetime(i) and isinstance(j,str)):
                                dat = str(i) + str(j)
                            else:
                                print("Error: no se puede sumar los valores "+str(i)+" y "+str(j))
                                return
                                
                            
                            respuesta.append(dat) 
                except ZeroDivisionError:
                    print("¡Error! División por cero.") 
                    return 

            print("exp1: ",exp1," exp2: ",exp2)
            print("respuesta: ",respuesta)
            
            return respuesta
        
        else:
            # para funciones del sistema
            print(instr.get("tipo").name)
            print(instr)
    else:
        
        return instr
    
def procesar_expresion(cadena):
    # si expresion contine comillas dobles o simples escribir algo
    if isinstance(cadena, str):
        if not cadena.startswith('\"') and not cadena.startswith('\''):
            # se tiene que buscar en la tabla la columna correspondiente
             
            return xml.obtener_registros(basedata,table,cadena)
        
        elif cadena.startswith('@'):
            # se tiene que buscar en la tabla de simbolos
            return [5]
        else:
           
            # quitar las comillas
            cadena = cadena[1:-1]
            return [cadena]
    else:
        if isinstance(cadena, list):
            return cadena
        else:
            return [cadena]



def is_date_or_datetime(s):
    s = str(s)
    try:
        # Intenta convertir la cadena en una fecha
        datetime.strptime(s, '%d-%m-%Y')
        return True
    except ValueError:
        pass

    try:
        # Intenta convertir la cadena en una fecha con hora
        datetime.strptime(s, '%d-%m-%Y %H:%M:%S')
        return True
    except ValueError:
        pass

    # Si no se puede convertir en ninguna de las dos, retorna False
    return False