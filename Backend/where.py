
from datetime import datetime
from instrucciones import *
import tablasimbolo as TS
from manejoxml import *


xml = XMLManejador("./BasesDatos.xml")  

basedata = ""
table = ""
listatipodatos = []
def procesar_where1(instr,base,tabla):
    global basedata
    basedata = base
    global table
    table = tabla
    global listatipodatos

    if isinstance(instr, dict):
        if instr.get("tipo") == TIPO_OPERACION.MAYOR_QUE:
           
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()

            print("")
            print(exp1," > ",exp2)

            exp1 = procesar_dato(exp1)
            exp2 = procesar_dato(exp2)
            tipoE2=listatipodatos.pop()
            tipoE1=listatipodatos.pop()
            if isinstance(exp1, dict):
                tipoE1 = exp1.get("tipo")
                exp1 = exp1.get("dato")
            if isinstance(exp2, dict):
                tipoE2 = exp2.get("tipo")
                exp2 = exp2.get("dato")

            respuesta = []
            tiporesult=[]
            if len(exp1) > 1 and len(exp2) > 1:
                for i,j,tipo1,tipo2 in zip(exp1,exp2,tipoE1,tipoE2):
                
                    if ((tipo1==TIPO_DATO.INT or tipo1==TIPO_DATO.DECIMAL) and (tipo2==TIPO_DATO.INT or tipo2==TIPO_DATO.DECIMAL)) or ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR)):
                        if i>j:
                            respuesta.append(1)
                        else:
                            respuesta.append(0)
                        tiporesult.append(TIPO_DATO.BIT)
                    elif (tipo1==TIPO_DATO.DATE or tipo1==TIPO_DATO.DATETIME) and (tipo2==TIPO_DATO.DATE or tipo2==TIPO_DATO.DATETIME):
                        if datetime.strptime(i, '%d-%m-%Y %H:%M:%S') > datetime.strptime(j, '%d-%m-%Y %H:%M:%S'):
                            respuesta.append(1)
                        else:
                            respuesta.append(0)
                        tiporesult.append(TIPO_DATO.BIT)
                    else:
                        print("Error: no se puede comparar los valores "+str(i)+" y "+str(j))
                        listatipodatos.append("ERROR")
                        return ["ERROR"]  
            else:
                for i in range(len(exp1)):
                    for j in range(len(exp2)):
                        if ((tipo1[i]==TIPO_DATO.INT or tipo1[i]==TIPO_DATO.DECIMAL) and (tipo2[j]==TIPO_DATO.INT or tipo2[j]==TIPO_DATO.DECIMAL)) or ((tipo1[i]==TIPO_DATO.CHAR or tipo1[i]==TIPO_DATO.VARCHAR) and (tipo2[j]==TIPO_DATO.CHAR or tipo2[j]==TIPO_DATO.VARCHAR)):
                            if i>j:
                                respuesta.append(1)
                            else:
                                respuesta.append(0)
                        elif (tipo1[i]==TIPO_DATO.DATE or tipo1[i]==TIPO_DATO.DATETIME) and (tipo2[j]==TIPO_DATO.DATE or tipo2[j]==TIPO_DATO.DATETIME):
                            if datetime.strptime(i, '%d-%m-%Y %H:%M:%S') > datetime.strptime(j, '%d-%m-%Y %H:%M:%S'):
                                respuesta.append(1)
                            else:
                                respuesta.append(0)
                        else:
                            print("Error: no se puede comparar los valores "+str(i)+" y "+str(j))
                            listatipodatos.append("ERROR")
                            return ["ERROR"]      
            
            print("exp1: ",exp1," exp2: ",exp2)
            listatipodatos.append(TIPO_DATO.BIT)
            print("respuesta: ",respuesta,"tipo:",listatipodatos)
            return respuesta
        elif instr.get("tipo") == TIPO_OPERACION.MENOR_QUE:
            
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            print("")
            print(exp1," < ",exp2)

            exp1 = procesar_dato(exp1)
            exp2 = procesar_dato(exp2)
            tipo2=listatipodatos.pop()
            tipo1=listatipodatos.pop()
            if isinstance(exp1, dict):
                tipo1 = exp1.get("tipo")
                exp1 = exp1.get("dato")
            if isinstance(exp2, dict):
                tipo2 = exp2.get("tipo")
                exp2 = exp2.get("dato")

            respuesta = []
        
            if len(exp1) > 1 and len(exp2) > 1:
                for i,j in zip(exp1,exp2):
                
                    if ((tipo1==TIPO_DATO.INT or tipo1==TIPO_DATO.DECIMAL) and (tipo2==TIPO_DATO.INT or tipo2==TIPO_DATO.DECIMAL)) or ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR)):
                        if i<j:
                            respuesta.append(1)
                        else:
                            respuesta.append(0)
                    elif (tipo1==TIPO_DATO.DATE or tipo1==TIPO_DATO.DATETIME) and (tipo2==TIPO_DATO.DATE or tipo2==TIPO_DATO.DATETIME):
                        if datetime.strptime(i, '%d-%m-%Y %H:%M:%S') < datetime.strptime(j, '%d-%m-%Y %H:%M:%S'):
                            respuesta.append(1)
                        else:
                            respuesta.append(0)
                    else:
                        print("Error: no se puede comparar los valores "+str(i)+" y "+str(j))
                        listatipodatos.append("ERROR")
                        return ["ERROR"]  
            else:
                for i in exp1:
                    for j in exp2:
                        if ((tipo1==TIPO_DATO.INT or tipo1==TIPO_DATO.DECIMAL) and (tipo2==TIPO_DATO.INT or tipo2==TIPO_DATO.DECIMAL)) or ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR)):
                            if i<j:
                                respuesta.append(1)
                            else:
                                respuesta.append(0)
                        elif (tipo1==TIPO_DATO.DATE or tipo1==TIPO_DATO.DATETIME) and (tipo2==TIPO_DATO.DATE or tipo2==TIPO_DATO.DATETIME):
                            if datetime.strptime(i, '%d-%m-%Y %H:%M:%S') < datetime.strptime(j, '%d-%m-%Y %H:%M:%S'):
                                respuesta.append(1)
                            else:
                                respuesta.append(0)
                        else:
                            print("Error: no se puede comparar los valores "+str(i)+" y "+str(j))
                            listatipodatos.append("ERROR")
                            return ["ERROR"]      
            
            print("exp1: ",exp1," exp2: ",exp2)
            listatipodatos.append(TIPO_DATO.BIT)
            print("respuesta: ",respuesta,"tipo:",listatipodatos)
            return respuesta
        elif instr.get("tipo") == TIPO_OPERACION.IGUAL_IGUAL or instr.get("tipo") == TIPO_OPERACION.IGUAL:
            
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            print("")
            print(exp1," == ",exp2)

            exp1 = procesar_dato(exp1)
            exp2 = procesar_dato(exp2)
            tipo2=listatipodatos.pop()
            tipo1=listatipodatos.pop()
            if isinstance(exp1, dict):
                tipo1 = exp1.get("tipo")
                exp1 = exp1.get("dato")
            if isinstance(exp2, dict):
                tipo2 = exp2.get("tipo")
                exp2 = exp2.get("dato")

            respuesta = []
        
            if len(exp1) > 1 and len(exp2) > 1:
                for i,j in zip(exp1,exp2):
                    print("i: ",tipo1," j: ",tipo2)
                    if ((tipo1==TIPO_DATO.INT or tipo1==TIPO_DATO.DECIMAL) and (tipo2==TIPO_DATO.INT or tipo2==TIPO_DATO.DECIMAL)) or ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR)):
                        if i==j:
                            respuesta.append(1)
                        else:
                            respuesta.append(0)
                    elif (tipo1==TIPO_DATO.DATE or tipo1==TIPO_DATO.DATETIME) and (tipo2==TIPO_DATO.DATE or tipo2==TIPO_DATO.DATETIME):
                        if datetime.strptime(i, '%d-%m-%Y %H:%M:%S') == datetime.strptime(j, '%d-%m-%Y %H:%M:%S'):
                            respuesta.append(1)
                        else:
                            respuesta.append(0)
                    else:
                        print("Error: no se puede comparar los valores "+str(i)+" y "+str(j))
                        listatipodatos.append("ERROR")
                        return ["ERROR"]  
            else:
                for i in exp1:
                    for j in exp2:
                        if ((tipo1==TIPO_DATO.INT or tipo1==TIPO_DATO.DECIMAL) and (tipo2==TIPO_DATO.INT or tipo2==TIPO_DATO.DECIMAL)) or ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR)):
                            if i==j:
                                respuesta.append(1)
                            else:
                                respuesta.append(0)
                        elif (tipo1==TIPO_DATO.DATE or tipo1==TIPO_DATO.DATETIME) and (tipo2==TIPO_DATO.DATE or tipo2==TIPO_DATO.DATETIME):
                            if datetime.strptime(i, '%d-%m-%Y %H:%M:%S') == datetime.strptime(j, '%d-%m-%Y %H:%M:%S'):
                                respuesta.append(1)
                            else:
                                respuesta.append(0)
                        else:
                            print("Error: no se puede comparar los valores "+str(i)+" y "+str(j))
                            listatipodatos.append("ERROR")
                            return ["ERROR"]      
            
            print("exp1: ",exp1," exp2: ",exp2)
            listatipodatos.append(TIPO_DATO.BIT)
            print("respuesta: ",respuesta,"tipo:",listatipodatos)
            return respuesta
        elif instr.get("tipo") == TIPO_OPERACION.NO_IGUAL:
            
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            print("")
            print(exp1," != ",exp2)

            exp1 = procesar_dato(exp1)
            exp2 = procesar_dato(exp2)
            tipo2=listatipodatos.pop()
            tipo1=listatipodatos.pop()
            if isinstance(exp1, dict):
                tipo1 = exp1.get("tipo")
                exp1 = exp1.get("dato")
            if isinstance(exp2, dict):
                tipo2 = exp2.get("tipo")
                exp2 = exp2.get("dato")

            respuesta = []
        
            if len(exp1) > 1 and len(exp2) > 1:
                for i,j in zip(exp1,exp2):
                
                    if ((tipo1==TIPO_DATO.INT or tipo1==TIPO_DATO.DECIMAL) and (tipo2==TIPO_DATO.INT or tipo2==TIPO_DATO.DECIMAL)) or ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR)):
                        if i!=j:
                            respuesta.append(1)
                        else:
                            respuesta.append(0)
                    elif (tipo1==TIPO_DATO.DATE or tipo1==TIPO_DATO.DATETIME) and (tipo2==TIPO_DATO.DATE or tipo2==TIPO_DATO.DATETIME):
                        if datetime.strptime(i, '%d-%m-%Y %H:%M:%S') != datetime.strptime(j, '%d-%m-%Y %H:%M:%S'):
                            respuesta.append(1)
                        else:
                            respuesta.append(0)
                    else:
                        print("Error: no se puede comparar los valores "+str(i)+" y "+str(j))
                        listatipodatos.append("ERROR")
                        return ["ERROR"]  
            else:
                for i in exp1:
                    for j in exp2:
                        if ((tipo1==TIPO_DATO.INT or tipo1==TIPO_DATO.DECIMAL) and (tipo2==TIPO_DATO.INT or tipo2==TIPO_DATO.DECIMAL)) or ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR)):
                            if i!=j:
                                respuesta.append(1)
                            else:
                                respuesta.append(0)
                        elif (tipo1==TIPO_DATO.DATE or tipo1==TIPO_DATO.DATETIME) and (tipo2==TIPO_DATO.DATE or tipo2==TIPO_DATO.DATETIME):
                            if datetime.strptime(i, '%d-%m-%Y %H:%M:%S') != datetime.strptime(j, '%d-%m-%Y %H:%M:%S'):
                                respuesta.append(1)
                            else:
                                respuesta.append(0)
                        else:
                            print("Error: no se puede comparar los valores "+str(i)+" y "+str(j))
                            listatipodatos.append("ERROR")
                            return ["ERROR"]      
            
            print("exp1: ",exp1," exp2: ",exp2)
            listatipodatos.append(TIPO_DATO.BIT)
            print("respuesta: ",respuesta,"tipo:",listatipodatos)
            return respuesta
        elif instr.get("tipo") == TIPO_OPERACION.MAYOR_IGUAL:
            
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            print("")
            print(exp1," >= ",exp2)

            exp1 = procesar_dato(exp1)
            exp2 = procesar_dato(exp2)
            tipo2=listatipodatos.pop()
            tipo1=listatipodatos.pop()
            if isinstance(exp1, dict):
                tipo1 = exp1.get("tipo")
                exp1 = exp1.get("dato")
            if isinstance(exp2, dict):
                tipo2 = exp2.get("tipo")
                exp2 = exp2.get("dato")

            respuesta = []
        
            if len(exp1) > 1 and len(exp2) > 1:
                for i,j in zip(exp1,exp2):
                
                    if ((tipo1==TIPO_DATO.INT or tipo1==TIPO_DATO.DECIMAL) and (tipo2==TIPO_DATO.INT or tipo2==TIPO_DATO.DECIMAL)) or ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR)):
                        if i>=j:
                            respuesta.append(1)
                        else:
                            respuesta.append(0)
                    elif (tipo1==TIPO_DATO.DATE or tipo1==TIPO_DATO.DATETIME) and (tipo2==TIPO_DATO.DATE or tipo2==TIPO_DATO.DATETIME):
                        if datetime.strptime(i, '%d-%m-%Y %H:%M:%S') >= datetime.strptime(j, '%d-%m-%Y %H:%M:%S'):
                            respuesta.append(1)
                        else:
                            respuesta.append(0)
                    else:
                        print("Error: no se puede comparar los valores "+str(i)+" y "+str(j))
                        listatipodatos.append("ERROR")
                        return ["ERROR"]  
            else:
                for i in exp1:
                    for j in exp2:
                        if ((tipo1==TIPO_DATO.INT or tipo1==TIPO_DATO.DECIMAL) and (tipo2==TIPO_DATO.INT or tipo2==TIPO_DATO.DECIMAL)) or ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR)):
                            if i>=j:
                                respuesta.append(1)
                            else:
                                respuesta.append(0)
                        elif (tipo1==TIPO_DATO.DATE or tipo1==TIPO_DATO.DATETIME) and (tipo2==TIPO_DATO.DATE or tipo2==TIPO_DATO.DATETIME):
                            if datetime.strptime(i, '%d-%m-%Y %H:%M:%S') >= datetime.strptime(j, '%d-%m-%Y %H:%M:%S'):
                                respuesta.append(1)
                            else:
                                respuesta.append(0)
                        else:
                            print("Error: no se puede comparar los valores "+str(i)+" y "+str(j))
                            listatipodatos.append("ERROR")
                            return ["ERROR"]      
            
            print("exp1: ",exp1," exp2: ",exp2)
            listatipodatos.append(TIPO_DATO.BIT)
            print("respuesta: ",respuesta,"tipo:",listatipodatos)
            return respuesta
        elif instr.get("tipo") == TIPO_OPERACION.MENOR_IGUAL:
            
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            print("")
            print(exp1," <= ",exp2)

            exp1 = procesar_dato(exp1)
            exp2 = procesar_dato(exp2)
            tipo2=listatipodatos.pop()
            tipo1=listatipodatos.pop()
            if isinstance(exp1, dict):
                tipo1 = exp1.get("tipo")
                exp1 = exp1.get("dato")
            if isinstance(exp2, dict):
                tipo2 = exp2.get("tipo")
                exp2 = exp2.get("dato")

            respuesta = []
        
            if len(exp1) > 1 and len(exp2) > 1:
                for i,j in zip(exp1,exp2):
                
                    if ((tipo1==TIPO_DATO.INT or tipo1==TIPO_DATO.DECIMAL) and (tipo2==TIPO_DATO.INT or tipo2==TIPO_DATO.DECIMAL)) or ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR)):
                        if i<=j:
                            respuesta.append(1)
                        else:
                            respuesta.append(0)
                    elif (tipo1==TIPO_DATO.DATE or tipo1==TIPO_DATO.DATETIME) and (tipo2==TIPO_DATO.DATE or tipo2==TIPO_DATO.DATETIME):
                        if datetime.strptime(i, '%d-%m-%Y %H:%M:%S') <= datetime.strptime(j, '%d-%m-%Y %H:%M:%S'):
                            respuesta.append(1)
                        else:
                            respuesta.append(0)
                    else:
                        print("Error: no se puede comparar los valores "+str(i)+" y "+str(j))
                        listatipodatos.append("ERROR")
                        return ["ERROR"]  
            else:
                for i in exp1:
                    for j in exp2:
                        if ((tipo1==TIPO_DATO.INT or tipo1==TIPO_DATO.DECIMAL) and (tipo2==TIPO_DATO.INT or tipo2==TIPO_DATO.DECIMAL)) or ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR)):
                            if i<=j:
                                respuesta.append(1)
                            else:
                                respuesta.append(0)
                        elif (tipo1==TIPO_DATO.DATE or tipo1==TIPO_DATO.DATETIME) and (tipo2==TIPO_DATO.DATE or tipo2==TIPO_DATO.DATETIME):
                            if datetime.strptime(i, '%d-%m-%Y %H:%M:%S') <= datetime.strptime(j, '%d-%m-%Y %H:%M:%S'):
                                respuesta.append(1)
                            else:
                                respuesta.append(0)
                        else:
                            print("Error: no se puede comparar los valores "+str(i)+" y "+str(j))
                            listatipodatos.append("ERROR")
                            return ["ERROR"]      
            
            print("exp1: ",exp1," exp2: ",exp2)
            listatipodatos.append(TIPO_DATO.BIT)
            print("respuesta: ",respuesta,"tipo:",listatipodatos)
            return respuesta
        elif instr.get("tipo") == TIPO_OPERACION.AND:
            
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
       
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            print("")
            print(exp1," && ",exp2)

            exp1 = procesar_dato(exp1)
            exp2 = procesar_dato(exp2)
            tipo2=listatipodatos.pop()
            tipo1=listatipodatos.pop()
            if isinstance(exp1, dict):
                tipo1 = exp1.get("tipo")
                exp1 = exp1.get("dato")
            if isinstance(exp2, dict):
                tipo2 = exp2.get("tipo")
                exp2 = exp2.get("dato")

            respuesta = []
            try:
                if len(exp1)>1 and len(exp2)>1:
                    respuesta = [1 if i and j else 0 for i, j in zip(exp1, exp2)]
                else:
                    respuesta = [1 if i and j else 0 for i in exp1 for j in exp2]
            except:
                print("Error: no se puede comparar los valores "+str(exp1)+" y "+str(exp2))
                listatipodatos.append("ERROR")
                return ["ERROR"]

            print("exp1: ",exp1," exp2: ",exp2)
            listatipodatos.append(TIPO_DATO.BIT)
            print("respuesta: ",respuesta,"tipo:",listatipodatos)
            return respuesta
        elif instr.get("tipo") == TIPO_OPERACION.OR:
          
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            print("")
            print(exp1," || ",exp2)

            exp1 = procesar_dato(exp1)
            exp2 = procesar_dato(exp2)
            tipo2=listatipodatos.pop()
            tipo1=listatipodatos.pop()
            if isinstance(exp1, dict):
                tipo1 = exp1.get("tipo")
                exp1 = exp1.get("dato")
            if isinstance(exp2, dict):
                tipo2 = exp2.get("tipo")
                exp2 = exp2.get("dato")
            print("exp1: ",exp1," exp2: ",exp2)
            respuesta = []
            try:
                if len(exp1)>1 and len(exp2)>1:
                    respuesta = [1 if i or j else 0 for i, j in zip(exp1, exp2)]
                else:
                    respuesta = [1 if i or j else 0 for i in exp1 for j in exp2]
            except:
                print("Error: no se puede comparar los valores "+str(exp1)+" y "+str(exp2))
                listatipodatos.append("ERROR")
                return ["ERROR"]

            
            listatipodatos.append(TIPO_DATO.BIT)
            print("respuesta: ",respuesta,"tipo:",listatipodatos)
            return respuesta
        elif instr.get("tipo") == TIPO_OPERACION.NOT:
            
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            print("")
            print("!", exp1)

            exp1 = procesar_dato(exp1)
            tipo1=listatipodatos.pop()
            if isinstance(exp1, dict):
                tipo1 = exp1.get("tipo")
                exp1 = exp1.get("dato")
            print("exp1: ",exp1)
            respuesta = []
            try:

                for i in exp1:
                    respuesta.append(not i)
            except:
                print("Error: no se puede negar el valor "+str(exp1))
                listatipodatos.append("ERROR")
                return ["ERROR"]
            
            listatipodatos.append(TIPO_DATO.BIT)
            print("respuesta: ",respuesta,"tipo:",listatipodatos)
            
            return respuesta
        elif instr.get("tipo") == TIPO_OPERACION.BETWEEN:
            
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            exp2=procesar_where1(instr.get("exp2").get("exp1"))
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            exp3=procesar_where1(instr.get("exp2").get("exp2"))
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            print("")
            print(exp1, "esta entre", exp2 , " y ", exp3)

            exp1 = procesar_dato(exp1)
            exp2 = procesar_dato(exp2)
            exp3 = procesar_dato(exp3)
            tipo3=listatipodatos.pop()
            tipo2=listatipodatos.pop()
            tipo1=listatipodatos.pop()

            if isinstance(exp1, dict):
                tipo1 = exp1.get("tipo")
                exp1 = exp1.get("dato")
            if isinstance(exp2, dict):
                tipo2 = exp2.get("tipo")
                exp2 = exp2.get("dato")
            if isinstance(exp3, dict):
                tipo3 = exp3.get("tipo")
                exp3 = exp3.get("dato")
            print("exp1: ",exp1," exp2: ",exp2," exp3: ",exp3)
            respuesta = []
           
            if len(exp1) > 1 and len(exp2) > 1 and len(exp3)>1:
                for i,j,k in zip(exp1,exp2):
                    print("i: ",tipo1," j: ",tipo2," k: ",tipo3)
                    if ((tipo1==TIPO_DATO.INT or tipo1==TIPO_DATO.DECIMAL) and (tipo2==TIPO_DATO.INT or tipo2==TIPO_DATO.DECIMAL) and (tipo3==TIPO_DATO.INT or tipo3==TIPO_DATO.DECIMAL)) or ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR) and (tipo3==TIPO_DATO.CHAR or tipo3==TIPO_DATO.VARCHAR)):
                        if j<=i<=k:
                            respuesta.append(1)
                        else:
                            respuesta.append(0)
                    elif (tipo1==TIPO_DATO.DATE or tipo1==TIPO_DATO.DATETIME) and (tipo2==TIPO_DATO.DATE or tipo2==TIPO_DATO.DATETIME) and (tipo3==TIPO_DATO.DATE or tipo3==TIPO_DATO.DATETIME):
                        if  datetime.strptime(j, '%d-%m-%Y %H:%M:%S')<= datetime.strptime(i, '%d-%m-%Y %H:%M:%S') <= datetime.strptime(k, '%d-%m-%Y %H:%M:%S'):
                            respuesta.append(1)
                        else:
                            respuesta.append(0)
                    else:
                        print("Error: no se puede evaluar si "+str(i)+" esta entre "+str(j)+" y "+str(k))
                        listatipodatos.append("ERROR")
                        return ["ERROR"]  
            else:
                for i in exp1:
                    print("i: ",tipo1," j: ",tipo2," k: ",tipo3)
                    if ((tipo1==TIPO_DATO.INT or tipo1==TIPO_DATO.DECIMAL) and (tipo2==TIPO_DATO.INT or tipo2==TIPO_DATO.DECIMAL) and (tipo3==TIPO_DATO.INT or tipo3==TIPO_DATO.DECIMAL)) or ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR) and (tipo3==TIPO_DATO.CHAR or tipo3==TIPO_DATO.VARCHAR)):
                        if exp2[0]<=i<=exp3[0]:
                            respuesta.append(1)
                        else:
                            respuesta.append(0)
                    elif (tipo1==TIPO_DATO.DATE or tipo1==TIPO_DATO.DATETIME) and (tipo2==TIPO_DATO.DATE or tipo2==TIPO_DATO.DATETIME) and (tipo3==TIPO_DATO.DATE or tipo3==TIPO_DATO.DATETIME):
                        if  datetime.strptime(exp2[0], '%d-%m-%Y %H:%M:%S')<= datetime.strptime(i, '%d-%m-%Y %H:%M:%S') <= datetime.strptime(exp3[0], '%d-%m-%Y %H:%M:%S'):
                            respuesta.append(1)
                        else:
                            respuesta.append(0)
                    else:
                        print("Error: no se puede evaluar si  "+str(i)+" esta entre "+str(exp2[0])+" y "+str(exp3[0]))
                        listatipodatos.append("ERROR")
                        return ["ERROR"]       

            listatipodatos.append(TIPO_DATO.BIT)
            print("respuesta: ",respuesta,"tipo:",listatipodatos)
            
            return respuesta
        elif instr.get("tipo") == TIPO_OPERACION.SUMA:
           
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            print("")
            print(exp1, "+", exp2)
            exp1 = procesar_dato(exp1)
            exp2 = procesar_dato(exp2)
            tipo2 = listatipodatos.pop()
            tipo1 = listatipodatos.pop()
            #tipo de dato:
            
            if isinstance(exp1, dict):
                tipo1 = exp1.get("tipo")
                exp1 = exp1.get("dato")
            if isinstance(exp2, dict):
                tipo2 = exp2.get("tipo")
                exp2 = exp2.get("dato")
            print("exp1: ",exp1," exp2: ",exp2)
            tiporesult=""
            respuesta = []
            if len(exp1)>1 and len(exp2)>1:
                for i, j in zip(exp1, exp2):
                    dat = 0
                    print("i: ",tipo1," j: ",tipo2)
                    if (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and (j==1 or j==0)) or ((j==1 or j==0) and (i==1 or i==0)):
                        dat = i or j
                        tiporesult = TIPO_DATO.BIT
                    elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(j,int)) or ((i==1 or i==0) and isinstance(j,int)):
                        dat = int(i + j)
                        tiporesult = TIPO_DATO.INT
                    elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(j,float)) or ((i==1 or i==0) and isinstance(j,float)):
                        dat = round(float(i + j),2)
                        tiporesult = TIPO_DATO.DECIMAL
                    elif (tipo1==TIPO_DATO.BIT and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR) ) or ((tipo2==TIPO_DATO.CHAR or tipo2 == TIPO_DATO.VARCHAR) and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(j,str)) or ((i==1 or i==0) and isinstance(j,str)) and (is_date_or_datetime(j)==False):
                        dat = str(i) + str(j)
                        tiporesult=TIPO_DATO.VARCHAR
                    elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and (j==1 or j==0) ) or ((j==1 or j==0) and isinstance(i,int)):
                        dat = int(i + j)
                        tiporesult = TIPO_DATO.INT
                    elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(j,int)) or (isinstance(i,int) and isinstance(j,int)):
                        dat = int(i + j)
                        tiporesult = TIPO_DATO.INT
                    elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(j,float)) or (isinstance(i,int) and isinstance(j,float)):
                        dat = round(float(i + j),2)
                        tiporesult = TIPO_DATO.DECIMAL
                    elif (tipo1==TIPO_DATO.INT and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR) ) or ((tipo2==TIPO_DATO.CHAR or tipo2 == TIPO_DATO.VARCHAR) and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(j,str)) or (isinstance(i,int) and isinstance(j,str)) and (is_date_or_datetime(j)==False):
                        dat = str(i) + str(j)
                        tiporesult=TIPO_DATO.VARCHAR
                    elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and (j==1 or j==0)) or (isinstance(i,float) and (j==1 or j==0)):
                        dat = round(float(i + j),2)
                        tiporesult = TIPO_DATO.DECIMAL
                    elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(j,int)) or (isinstance(i,float) and isinstance(j,int)):
                        dat = round(float(i + j),2)
                        tiporesult = TIPO_DATO.DECIMAL
                    elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(j,float)) or (isinstance(i,float) and isinstance(j,float)):
                        dat = round(float(i + j),2)
                        tiporesult = TIPO_DATO.DECIMAL
                    elif (tipo1==TIPO_DATO.DECIMAL and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR) ) or ((tipo2==TIPO_DATO.CHAR or tipo2 == TIPO_DATO.VARCHAR) and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(j,str)) or (isinstance(i,float) and isinstance(j,str)) and (is_date_or_datetime(j)==False):
                        dat = str(i) + str(j)
                        tiporesult=TIPO_DATO.VARCHAR
                    elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and tipo2==TIPO_DATO.BIT) or ((tipo1==TIPO_DATO.CHAR or tipo1 == TIPO_DATO.VARCHAR) and (j==1 or j==0)) or (tipo2==TIPO_DATO.BIT and isinstance(i,str)) or (isinstance(i,str) and (j==1 or j==0)) and (is_date_or_datetime(i)==False):
                        dat = str(i) + str(j)
                        tiporesult=TIPO_DATO.VARCHAR
                    elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and tipo2==TIPO_DATO.INT) or ((tipo1==TIPO_DATO.CHAR or tipo1 == TIPO_DATO.VARCHAR) and isinstance(j,int)) or (tipo2==TIPO_DATO.INT and isinstance(i,str)) or (isinstance(i,str) and isinstance(j,int)) and (is_date_or_datetime(i)==False):
                        dat = str(i) + str(j)
                        tiporesult=TIPO_DATO.VARCHAR
                    elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and tipo2==TIPO_DATO.DECIMAL) or ((tipo1==TIPO_DATO.CHAR or tipo1 == TIPO_DATO.VARCHAR) and isinstance(j,float)) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,str)) or (isinstance(i,str) and isinstance(j,float)) and (is_date_or_datetime(i)==False):
                        dat = str(i) + str(j)
                        tiporesult=TIPO_DATO.VARCHAR
                    elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR) and   isinstance(i,str)) or ((tipo1==TIPO_DATO.CHAR or tipo1 == TIPO_DATO.VARCHAR) and isinstance(j,str)) or (isinstance(i,str) and isinstance(j,str)) and (is_date_or_datetime(i)==False):
                        dat = str(i) + str(j)
                        tiporesult=TIPO_DATO.VARCHAR
                    else:
                        print("Error: no se puede sumar los valores "+str(i)+" y "+str(j))
                        listatipodatos.append("ERROR")
                        return ["ERROR"]
                        
                    
                    respuesta.append(dat)

            else:
                for i in exp1:
                    for j in exp2:
                        dat = 0
                        print("i: ",tipo1," j: ",tipo2)
                        if (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and (j==1 or j==0)) or ((j==1 or j==0) and (i==1 or i==0)):
                            dat = i or j
                            tiporesult = TIPO_DATO.BIT
                        elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(j,int)) or ((i==1 or i==0) and isinstance(j,int)):
                            dat = int(i + j)
                            tiporesult = TIPO_DATO.INT
                        elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(j,float)) or ((i==1 or i==0) and isinstance(j,float)):
                            dat = round(float(i + j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif (tipo1==TIPO_DATO.BIT and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR) ) or ((tipo2==TIPO_DATO.CHAR or tipo2 == TIPO_DATO.VARCHAR) and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(j,str)) or ((i==1 or i==0) and isinstance(j,str)) and (is_date_or_datetime(j)==False):
                            dat = str(i) + str(j)
                            tiporesult=TIPO_DATO.VARCHAR
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and (j==1 or j==0) ) or ((j==1 or j==0) and isinstance(i,int)):
                            dat = int(i + j)
                            tiporesult = TIPO_DATO.INT
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(j,int)) or (isinstance(i,int) and isinstance(j,int)):
                            dat = int(i + j)
                            tiporesult = TIPO_DATO.INT
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(j,float)) or (isinstance(i,int) and isinstance(j,float)):
                            dat = round(float(i + j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif (tipo1==TIPO_DATO.INT and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR) ) or ((tipo2==TIPO_DATO.CHAR or tipo2 == TIPO_DATO.VARCHAR) and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(j,str)) or (isinstance(i,int) and isinstance(j,str)) and (is_date_or_datetime(j)==False):
                            dat = str(i) + str(j)
                            tiporesult=TIPO_DATO.VARCHAR
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and (j==1 or j==0)) or (isinstance(i,float) and (j==1 or j==0)):
                            dat = round(float(i + j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(j,int)) or (isinstance(i,float) and isinstance(j,int)):
                            dat = round(float(i + j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(j,float)) or (isinstance(i,float) and isinstance(j,float)):
                            dat = round(float(i + j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif (tipo1==TIPO_DATO.DECIMAL and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR) ) or ((tipo2==TIPO_DATO.CHAR or tipo2 == TIPO_DATO.VARCHAR) and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(j,str)) or (isinstance(i,float) and isinstance(j,str)) and (is_date_or_datetime(j)==False):
                            dat = str(i) + str(j)
                            tiporesult=TIPO_DATO.VARCHAR
                        elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and tipo2==TIPO_DATO.BIT) or ((tipo1==TIPO_DATO.CHAR or tipo1 == TIPO_DATO.VARCHAR) and (j==1 or j==0)) or (tipo2==TIPO_DATO.BIT and isinstance(i,str)) or (isinstance(i,str) and (j==1 or j==0)) and (is_date_or_datetime(i)==False):
                            dat = str(i) + str(j)
                            tiporesult=TIPO_DATO.VARCHAR
                        elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and tipo2==TIPO_DATO.INT) or ((tipo1==TIPO_DATO.CHAR or tipo1 == TIPO_DATO.VARCHAR) and isinstance(j,int)) or (tipo2==TIPO_DATO.INT and isinstance(i,str)) or (isinstance(i,str) and isinstance(j,int)) and (is_date_or_datetime(i)==False):
                            dat = str(i) + str(j)
                            tiporesult=TIPO_DATO.VARCHAR
                        elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and tipo2==TIPO_DATO.DECIMAL) or ((tipo1==TIPO_DATO.CHAR or tipo1 == TIPO_DATO.VARCHAR) and isinstance(j,float)) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,str)) or (isinstance(i,str) and isinstance(j,float)) and (is_date_or_datetime(i)==False):
                            dat = str(i) + str(j)
                            tiporesult=TIPO_DATO.VARCHAR
                        elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR) and   isinstance(i,str)) or ((tipo1==TIPO_DATO.CHAR or tipo1 == TIPO_DATO.VARCHAR) and isinstance(j,str)) or (isinstance(i,str) and isinstance(j,str)) and (is_date_or_datetime(i)==False):
                            dat = str(i) + str(j)
                            tiporesult=TIPO_DATO.VARCHAR
                        else:
                            print("Error: no se puede sumar los valores "+str(i)+" y "+str(j))
                            listatipodatos.append("ERROR")
                            return None
                            
                        
                        respuesta.append(dat)   

           
            
            listatipodatos.append(tiporesult)
            print("respuesta: ",respuesta,"tipo:",listatipodatos)
            
            return respuesta
        elif instr.get("tipo") == TIPO_OPERACION.RESTA:
            
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            print("")
            print(exp1, "-", exp2)
            exp1 = procesar_dato(exp1)
            exp2 = procesar_dato(exp2)
            tipo2 = listatipodatos.pop()
            tipo1 = listatipodatos.pop()
            if isinstance(exp1, dict):
                tipo1 = exp1.get("tipo")
                exp1 = exp1.get("dato")
            if isinstance(exp2, dict):
                tipo2 = exp2.get("tipo")
                exp2 = exp2.get("dato")
            print("exp1: ",exp1," exp2: ",exp2)
            tiporesult=""
            respuesta = []
            
            if len(exp1)>1 and len(exp2)>1:
                for i, j in zip(exp1, exp2):
                        dat = 0
                        print("i: ",tipo1," j: ",tipo2)
                        if (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(j,int)) or ((i==1 or i==0) and isinstance(j,int)):
                            dat = int(i - j)
                            tiporesult = TIPO_DATO.INT
                        elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(j,float)) or ((i==1 or i==0) and isinstance(j,float)):
                            dat = round(float(i - j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and (j==1 or j==0)) or ((j==1 or j==0) and isinstance(i,int)):
                            dat = int(i - j)
                            tiporesult = TIPO_DATO.INT
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(j,int)) or (isinstance(i,int) and isinstance(j,int)):
                            dat = int(i - j)
                            tiporesult = TIPO_DATO.INT
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(j,float)) or (isinstance(i,int) and isinstance(j,float)):
                            dat = round(float(i - j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and (j==1 or j==0)) or ((j==1 or j==0) and isinstance(i,float)):
                            dat = round(float(i - j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(j,int)) or (isinstance(i,float) and isinstance(j,int)):
                            dat = round(float(i - j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(j,float)) or (isinstance(i,float) and isinstance(j,float)):
                            dat = round(float(i - j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        else:
                            print("Error: no se puede restar los valores "+str(i)+" y "+str(j))
                            listatipodatos.append("ERROR")
                            return ["ERROR"]
                            
                        
                        respuesta.append(dat)  
            else:
                for i in exp1:
                
                    for j in exp2:
                        dat = 0
                        print("i: ",tipo1," j: ",tipo2)
                        if (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(j,int)) or ((i==1 or i==0) and isinstance(j,int)):
                            dat = int(i - j)
                            tiporesult = TIPO_DATO.INT
                        elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(j,float)) or ((i==1 or i==0) and isinstance(j,float)):
                            dat = round(float(i - j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and (j==1 or j==0)) or ((j==1 or j==0) and isinstance(i,int)):
                            dat = int(i - j)
                            tiporesult = TIPO_DATO.INT
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(j,int)) or (isinstance(i,int) and isinstance(j,int)):
                            dat = int(i - j)
                            tiporesult = TIPO_DATO.INT
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(j,float)) or (isinstance(i,int) and isinstance(j,float)):
                            dat = round(float(i - j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and (j==1 or j==0)) or ((j==1 or j==0) and isinstance(i,float)):
                            dat = round(float(i - j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(j,int)) or (isinstance(i,float) and isinstance(j,int)):
                            dat = round(float(i - j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(j,float)) or (isinstance(i,float) and isinstance(j,float)):
                            dat = round(float(i - j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        else:
                            print("Error: no se puede restar los valores "+str(i)+" y "+str(j))
                            listatipodatos.append("ERROR")
                            return ["ERROR"]
                            
                        
                        respuesta.append(dat)   

            
            listatipodatos.append(tiporesult)
            print("respuesta: ",respuesta,"tipo:",listatipodatos)
            
            
            return respuesta
        elif instr.get("tipo") == TIPO_OPERACION.MULTIPLICACION:
            
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            print("")
            print(exp1, "*", exp2)
            exp1 = procesar_dato(exp1)
            exp2 = procesar_dato(exp2)
            tipo2 = listatipodatos.pop()
            tipo1 = listatipodatos.pop()
            if isinstance(exp1, dict):
                tipo1 = exp1.get("tipo")
                exp1 = exp1.get("dato")
            if isinstance(exp2, dict):
                tipo2 = exp2.get("tipo")
                exp2 = exp2.get("dato")
            print("exp1: ",exp1," exp2: ",exp2)
            tiporesult=""
            respuesta = []
            if len(exp1)>1 and len(exp2)>1:
                for i, j in zip(exp1, exp2):
                        print("i: ",tipo1," j: ",tipo2)
                        dat = 0
                        if (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and (j==1 or j==0)) or ((j==1 or j==0) and (i==1 or i==0)):
                            dat = i and j
                            tiporesult = TIPO_DATO.BIT
                        elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(j,int)) or ((i==1 or i==0) and isinstance(j,int)):
                            dat = int(i * j)
                            tiporesult = TIPO_DATO.INT
                        elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(j,float)) or ((i==1 or i==0) and isinstance(j,float)):
                            dat = round(float(i * j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and (j==1 or j==0)) or ((j==1 or j==0) and isinstance(i,int)):
                            dat = int(i * j)
                            tiporesult = TIPO_DATO.INT
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(j,int)) or (isinstance(i,int) and isinstance(j,int)):
                            dat = int(i * j)
                            tiporesult = TIPO_DATO.INT
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(j,float)) or (isinstance(i,int) and isinstance(j,float)):
                            dat = round(float(i * j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and (j==1 or j==0)) or ((j==1 or j==0) and isinstance(i,float)):
                            dat = round(float(i * j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(j,int)) or (isinstance(i,float) and isinstance(j,int)):
                            dat = round(float(i * j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(j,float)) or (isinstance(i,float) and isinstance(j,float)):
                            dat = round(float(i * j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.DATE or tipo2==TIPO_DATO.DATETIME )) or ((tipo2==TIPO_DATO.DATE or tipo2 == TIPO_DATO.DATETIME) and isinstance(i,str)) or ((tipo1==TIPO_DATO.CHAR or tipo1 == TIPO_DATO.VARCHAR) and is_date_or_datetime(j)) or (is_date_or_datetime(i) and isinstance(j,str)):
                            dat = str(i) + str(j)
                            tiporesult=TIPO_DATO.VARCHAR
                        elif ((tipo1==TIPO_DATO.DATE or tipo1==TIPO_DATO.DATETIME) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR )) or ((tipo2==TIPO_DATO.CHAR or tipo2 == TIPO_DATO.VARCHAR) and is_date_or_datetime(i)) or ((tipo1==TIPO_DATO.DATE or tipo1 == TIPO_DATO.DATETIME) and isinstance(j,str)) or (is_date_or_datetime(i) and isinstance(j,str)):
                            dat = str(i) + str(j)
                            tiporesult=TIPO_DATO.VARCHAR
                        else:
                            print("Error: no se puede multiplicar los valores "+str(i)+" y "+str(j))
                            listatipodatos.append("ERROR")
                            return ["ERROR"]
                            
                        
                        respuesta.append(dat)  
            else:
                for i in exp1:
                
                    for j in exp2:
                        print("i: ",tipo1," j: ",tipo2)
                        dat = 0
                        if (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and (j==1 or j==0)) or ((j==1 or j==0) and (i==1 or i==0)):
                            dat = i and j
                            tiporesult = TIPO_DATO.BIT
                        elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(j,int)) or ((i==1 or i==0) and isinstance(j,int)):
                            dat = int(i * j)
                            tiporesult = TIPO_DATO.INT
                        elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(j,float)) or ((i==1 or i==0) and isinstance(j,float)):
                            dat = round(float(i * j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and (j==1 or j==0)) or ((j==1 or j==0) and isinstance(i,int)):
                            dat = int(i * j)
                            tiporesult = TIPO_DATO.INT
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(j,int)) or (isinstance(i,int) and isinstance(j,int)):
                            dat = int(i * j)
                            tiporesult = TIPO_DATO.INT
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(j,float)) or (isinstance(i,int) and isinstance(j,float)):
                            dat = round(float(i * j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and (j==1 or j==0)) or ((j==1 or j==0) and isinstance(i,float)):
                            dat = round(float(i * j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(j,int)) or (isinstance(i,float) and isinstance(j,int)):
                            dat = round(float(i * j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(j,float)) or (isinstance(i,float) and isinstance(j,float)):
                            dat = round(float(i * j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.DATE or tipo2==TIPO_DATO.DATETIME )) or ((tipo2==TIPO_DATO.DATE or tipo2 == TIPO_DATO.DATETIME) and isinstance(i,str)) or ((tipo1==TIPO_DATO.CHAR or tipo1 == TIPO_DATO.VARCHAR) and is_date_or_datetime(j)) or (is_date_or_datetime(i) and isinstance(j,str)):
                            dat = str(i) + str(j)
                            tiporesult=TIPO_DATO.VARCHAR
                        elif ((tipo1==TIPO_DATO.DATE or tipo1==TIPO_DATO.DATETIME) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR )) or ((tipo2==TIPO_DATO.CHAR or tipo2 == TIPO_DATO.VARCHAR) and is_date_or_datetime(i)) or ((tipo1==TIPO_DATO.DATE or tipo1 == TIPO_DATO.DATETIME) and isinstance(j,str)) or (is_date_or_datetime(i) and isinstance(j,str)):
                            dat = str(i) + str(j)
                            tiporesult=TIPO_DATO.VARCHAR
                        else:
                            print("Error: no se puede multiplicar los valores "+str(i)+" y "+str(j))
                            listatipodatos.append("ERROR")
                            return ["ERROR"]
                            
                        
                        respuesta.append(dat)   

         
            listatipodatos.append(tiporesult)
            print("respuesta: ",respuesta,"tipo:",listatipodatos)
            
            
            return respuesta
        elif instr.get("tipo") == TIPO_OPERACION.DIVISION:
        
            exp1=procesar_where1(instr.get("exp1"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            exp2=procesar_where1(instr.get("exp2"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            print("")
            print(exp1, "/", exp2)
            exp1 = procesar_dato(exp1)
            exp2 = procesar_dato(exp2)
            tipo2 = listatipodatos.pop()
            tipo1 = listatipodatos.pop()
            if isinstance(exp1, dict):
                tipo1 = exp1.get("tipo")
                exp1 = exp1.get("dato")
            if isinstance(exp2, dict):
                tipo2 = exp2.get("tipo")
                exp2 = exp2.get("dato")
            print("exp1: ",exp1," exp2: ",exp2)
            tiporesult=""
            respuesta = []
            if len(exp1)>1 and len(exp2)>1:
                for i, j in zip(exp1, exp2):
                    print("i: ",tipo1," j: ",tipo2)
                    try:
                        dat = 0
                        if (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(j,int)) or ((i==1 or i==0) and isinstance(j,int)):
                            dat = int(i / j)
                            tiporesult = TIPO_DATO.INT
                        elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(j,float)) or ((i==1 or i==0) and isinstance(j,float)):
                            dat = round(float(i / j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and (j==1 or j==0)) or ((j==1 or j==0) and isinstance(i,int)):
                            dat = int(i / j)
                            tiporesult = TIPO_DATO.INT
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(j,int)) or (isinstance(i,int) and isinstance(j,int)):
                            dat = int(i / j)
                            tiporesult = TIPO_DATO.INT
                        elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(j,float)) or (isinstance(i,int) and isinstance(j,float)):
                            dat = round(float(i / j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and (j==1 or j==0)) or ((j==1 or j==0) and isinstance(i,float)):
                            dat = round(float(i / j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(j,int)) or (isinstance(i,float) and isinstance(j,int)):
                            dat = round(float(i / j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(j,float)) or (isinstance(i,float) and isinstance(j,float)):
                            dat = round(float(i / j),2)
                            tiporesult = TIPO_DATO.DECIMAL
                        elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.DATE or tipo2==TIPO_DATO.DATETIME )) or ((tipo2==TIPO_DATO.DATE or tipo2 == TIPO_DATO.DATETIME) and isinstance(i,str)) or ((tipo1==TIPO_DATO.CHAR or tipo1 == TIPO_DATO.VARCHAR) and is_date_or_datetime(j)) or (is_date_or_datetime(i) and isinstance(j,str)):
                            dat = str(i) + str(j)
                            tiporesult=TIPO_DATO.VARCHAR
                        elif ((tipo1==TIPO_DATO.DATE or tipo1==TIPO_DATO.DATETIME) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR )) or ((tipo2==TIPO_DATO.CHAR or tipo2 == TIPO_DATO.VARCHAR) and is_date_or_datetime(i)) or ((tipo1==TIPO_DATO.DATE or tipo1 == TIPO_DATO.DATETIME) and isinstance(j,str)) or (is_date_or_datetime(i) and isinstance(j,str)):
                            dat = str(i) + str(j)
                            tiporesult=TIPO_DATO.VARCHAR
                        else:
                            print("Error: no se puede dividir los valores "+str(i)+" y "+str(j))
                            listatipodatos.append("ERROR")
                            return ["ERROR"]
                            
                        
                        respuesta.append(dat) 
                    except ZeroDivisionError:
                        print("¡Error! División por cero.") 
                        listatipodatos.append("ERROR")
                        return ["ERROR"]
            else:
                for i in exp1:
                    try:
                        for j in exp2:
                            print("i: ",tipo1," j: ",tipo2)
                            dat = 0
                            if (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(j,int)) or ((i==1 or i==0) and isinstance(j,int)):
                                dat = int(i / j)
                                tiporesult = TIPO_DATO.INT
                            elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and (i==1 or i==0)) or (tipo1==TIPO_DATO.BIT and isinstance(j,float)) or ((i==1 or i==0) and isinstance(j,float)):
                                dat = round(float(i / j),2)
                                tiporesult = TIPO_DATO.DECIMAL
                            elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and (j==1 or j==0)) or ((j==1 or j==0) and isinstance(i,int)):
                                dat = int(i / j)
                                tiporesult = TIPO_DATO.INT
                            elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(j,int)) or (isinstance(i,int) and isinstance(j,int)):
                                dat = int(i / j)
                                tiporesult = TIPO_DATO.INT
                            elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,int)) or (tipo1==TIPO_DATO.INT and isinstance(j,float)) or (isinstance(i,int) and isinstance(j,float)):
                                dat = round(float(i / j),2)
                                tiporesult = TIPO_DATO.DECIMAL
                            elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.BIT) or (tipo2==TIPO_DATO.BIT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and (j==1 or j==0)) or ((j==1 or j==0) and isinstance(i,float)):
                                dat = round(float(i / j),2)
                                tiporesult = TIPO_DATO.DECIMAL
                            elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.INT) or (tipo2==TIPO_DATO.INT and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(j,int)) or (isinstance(i,float) and isinstance(j,int)):
                                dat = round(float(i / j),2)
                                tiporesult = TIPO_DATO.DECIMAL
                            elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.DECIMAL) or (tipo2==TIPO_DATO.DECIMAL and isinstance(i,float)) or (tipo1==TIPO_DATO.DECIMAL and isinstance(j,float)) or (isinstance(i,float) and isinstance(j,float)):
                                dat = round(float(i / j),2)
                                tiporesult = TIPO_DATO.DECIMAL
                            elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.DATE or tipo2==TIPO_DATO.DATETIME )) or ((tipo2==TIPO_DATO.DATE or tipo2 == TIPO_DATO.DATETIME) and isinstance(i,str)) or ((tipo1==TIPO_DATO.CHAR or tipo1 == TIPO_DATO.VARCHAR) and is_date_or_datetime(j)) or (is_date_or_datetime(i) and isinstance(j,str)):
                                dat = str(i) + str(j)
                                tiporesult=TIPO_DATO.VARCHAR
                            elif ((tipo1==TIPO_DATO.DATE or tipo1==TIPO_DATO.DATETIME) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR )) or ((tipo2==TIPO_DATO.CHAR or tipo2 == TIPO_DATO.VARCHAR) and is_date_or_datetime(i)) or ((tipo1==TIPO_DATO.DATE or tipo1 == TIPO_DATO.DATETIME) and isinstance(j,str)) or (is_date_or_datetime(i) and isinstance(j,str)):
                                dat = str(i) + str(j)
                                tiporesult=TIPO_DATO.VARCHAR
                            else:
                                print("Error: no se puede dividir los valores "+str(i)+" y "+str(j))
                                listatipodatos.append("ERROR")
                                return ["ERROR"]
                                    
                                
                            respuesta.append(dat) 
                    except ZeroDivisionError:
                        print("¡Error! División por cero.") 
                        listatipodatos.append("ERROR")
                        return ["ERROR"] 
                    
            listatipodatos.append(tiporesult)
            print("respuesta: ",respuesta,"tipo:",listatipodatos)
            
            
            return respuesta
        elif instr.get("tipo")==TIPO_INSTRUCCION.HOY:
                fecha_hora_actual = datetime.now()
                fecha_hora_formateada = fecha_hora_actual.strftime("\'%d-%m-%Y %H:%M:%S\'")
                listatipodatos.append(TIPO_DATO.DATETIME)
                return fecha_hora_formateada
        elif instr.get("tipo")==TIPO_INSTRUCCION.CONTATENACION:
           
            exp1=procesar_where1(instr.get("cadena1"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            exp2=procesar_where1(instr.get("cadena2"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            print("")
            print(exp1, " concatenado ", exp2)
            exp1 = procesar_dato(exp1)
            exp2 = procesar_dato(exp2)
            tipo2 = listatipodatos.pop()
            tipo1 = listatipodatos.pop()

            
            if isinstance(exp1, dict):
                tipo1 = exp1.get("tipo")
                exp1 = exp1.get("dato")
            if isinstance(exp2, dict):
                tipo2 = exp2.get("tipo")
                exp2 = exp2.get("dato")
            print("exp1: ",exp1," exp2: ",exp2)
            respuesta = []
            if len(exp1)>1 and len(exp2)>1:
                for i, j in zip(exp1, exp2):
                    print("i: ",tipo1," j: ",tipo2)
                    if i is None or j is None:
                        print("Error: no se puede concatenar con un valor nulo")
                        listatipodatos.append("ERROR")
                        return ["ERROR"]
                    # si tienen formato de fecha o fecha hora, error
                    elif is_date_or_datetime(i) or is_date_or_datetime(j):
                        print("Error: no se puede concatenar con un valor de tipo fecha o fecha hora")
                        listatipodatos.append("ERROR")
                        return ["ERROR"]
                    # si son int o float, error
                    elif isinstance(i,int) or isinstance(i,float) or isinstance(j,int) or isinstance(j,float):
                        print("Error: no se puede concatenar con un valor de tipo entero o decimal")
                        listatipodatos.append("ERROR")
                        return ["ERROR"]
                    
                    c1=str(i)
                    c2=str(j)
                    # añadir a la respuesta
                    respuesta.append(f"\'{c1+c2}\'")
                    
            else:
                for i in exp1:
                    for j in exp2:
                        print("i: ",tipo1," j: ",tipo2)
                        if i is None or j is None:
                            print("Error: no se puede concatenar con un valor nulo")
                            listatipodatos.append("ERROR")
                            return ["ERROR"]
                        # si tienen formato de fecha o fecha hora, error
                        elif is_date_or_datetime(i) or is_date_or_datetime(j):
                            print("Error: no se puede concatenar con un valor de tipo fecha o fecha hora")
                            listatipodatos.append("ERROR")
                            return ["ERROR"]
                        # si son int o float, error
                        elif isinstance(i,int) or isinstance(i,float) or isinstance(j,int) or isinstance(j,float):
                            print("Error: no se puede concatenar con un valor de tipo entero o decimal")
                            listatipodatos.append("ERROR")
                            return ["ERROR"]
                        
                        c1=str(i)
                        c2=str(j)
                        # añadir a la respuesta
                        respuesta.append(f"{c1+c2}")
            
            listatipodatos.append(TIPO_DATO.VARCHAR)
            
            print("respuesta: ",respuesta,"tipo:",listatipodatos)

            return respuesta
        elif instr.get("tipo")==TIPO_INSTRUCCION.SUBSTRER:
            
            exp1=procesar_where1(instr.get("cadena"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            exp2=procesar_where1(instr.get("inicio"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            exp3=procesar_where1(instr.get("fin"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()

            print("")
            print(exp1, " substraer ", exp2,exp3)
            exp1 = procesar_dato(exp1)
            exp2 = procesar_dato(exp2)
            exp3 = procesar_dato(exp3)
            tipo3 = listatipodatos.pop()
            tipo2 = listatipodatos.pop()
            tipo1 = listatipodatos.pop()


            if isinstance(exp1, dict):
                tipo1 = exp1.get("tipo")
                exp1 = exp1.get("dato")
            if isinstance(exp2, dict):
                tipo2 = exp2.get("tipo")
                exp2 = exp2.get("dato")
            if isinstance(exp3, dict):
                tipo3 = exp3.get("tipo")
                exp3 = exp3.get("dato")
            print("exp1: ",exp1," exp2: ",exp2," exp3: ",exp3)
            respuesta = []
            if len(exp1)>1 and len(exp2)>1:
                for i, j,k in zip(exp1, exp2):
                    print("i: ",tipo1," j: ",tipo2," k: ",tipo3)
                    if i is None :
                        print("Error: no se puede substraer de un valor nulo")
                        listatipodatos.append("ERROR")
                        return ["ERROR"]
                    # si tienen formato de fecha o fecha hora, error
                    elif is_date_or_datetime(i) :
                        print("Error: no se puede substraer de un valor de tipo fecha o fecha hora")
                        listatipodatos.append("ERROR")
                        return ["ERROR"]
                    # si son int o float, error
                    elif isinstance(i,int) or isinstance(i,float):
                        print("Error: no se puede substraer de un valor de tipo entero o decimal")
                        listatipodatos.append("ERROR")
                        return ["ERROR"]
                    elif not isinstance(j,int) or not isinstance(k,int):
                        print("Error: Para substraer se necesita de dos valores enteros como parametros")
                        listatipodatos.append("ERROR")
                        return ["ERROR"]
                    
                    # substraer  cadena,inicio,fin
                    c1= i[j:k]
                    # añadir a la respuesta
                    respuesta.append(f"\'{c1}\'")
                        
            else:
                for i in exp1:                    
                    print("i: ",tipo1," j: ",tipo2," k: ",tipo3)
                    if i is None :
                        print("Error: no se puede substraer de un valor nulo")
                        listatipodatos.append("ERROR")
                        return ["ERROR"]
                    # si tienen formato de fecha o fecha hora, error
                    elif is_date_or_datetime(i) :
                        print("Error: no se puede substraer de un valor de tipo fecha o fecha hora")
                        listatipodatos.append("ERROR")
                        return ["ERROR"]
                    # si son int o float, error
                    elif isinstance(i,int) or isinstance(i,float):
                        print("Error: no se puede substraer de un valor de tipo entero o decimal")
                        listatipodatos.append("ERROR")
                        return ["ERROR"]
                    elif not isinstance(exp2[0],int) or not isinstance(exp3[0],int):
                        print("Error: Para substraer se necesita de dos valores enteros como parametros")
                        listatipodatos.append("ERROR")
                        return ["ERROR"]
                    
                    c1=i[exp2[0]:exp3[0]]
                    # añadir a la respuesta
                    respuesta.append(f"\'{c1}\'")
            
            listatipodatos.append(TIPO_DATO.VARCHAR)
            
            print("respuesta: ",respuesta,"tipo:",listatipodatos)

            return respuesta        
        elif instr.get("tipo")==TIPO_INSTRUCCION.CAST:
            
            exp1=procesar_where1(instr.get("columna"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            print("")
            print(exp1, " castear a ", instr.get("tipodato").get("tipo"))
            exp1 = procesar_dato(exp1)
            tipo1 = listatipodatos.pop()


            if isinstance(exp1, dict):
                tipo1 = exp1.get("tipo")
                exp1 = exp1.get("dato")
                
            print("exp1: ",exp1)
            respuesta = []
            if len(exp1)>=1:
                for i in exp1:
                    print("i: ",tipo1," tipo2: ",instr.get("tipodato").get("tipo"))
                    if i is None :
                        print("Error: no se puede castear un valor nulo")
                        listatipodatos.append("ERROR")
                        return ["ERROR"]
                    elif (tipo1==TIPO_DATO.INT or tipo1==TIPO_DATO.DECIMAL) and instr.get("tipodato").get("tipo")==TIPO_DATO.BIT:
                        if int(i)==0 :
                            respuesta.append(0)
                        else:
                            respuesta.append(1)
                    elif (tipo1==TIPO_DATO.INT or tipo1==TIPO_DATO.DECIMAL) and instr.get("tipodato").get("tipo")==TIPO_DATO.INT:
                        respuesta.append(int(i))
                    elif (tipo1==TIPO_DATO.INT or tipo1==TIPO_DATO.DECIMAL) and instr.get("tipodato").get("tipo")==TIPO_DATO.DECIMAL:
                        respuesta.append(round(float(i),2))
                    elif (tipo1==TIPO_DATO.INT or tipo1==TIPO_DATO.DECIMAL) and (instr.get("tipodato").get("tipo")==TIPO_DATO.CHAR or instr.get("tipodato").get("tipo")==TIPO_DATO.VARCHAR):
                        if 0<=int(i)<=255:
                            if instr.get("tipodato").get("tipo")==TIPO_DATO.CHAR:
                                #justificar con espacios al final  
                                respuesta.append(chr(int(i)).ljust(instr.get("tipodato").get("longitud")))
                            else:
                                respuesta.append(chr(int(i)))
                        else:
                            respuesta.append(None)
                    elif tipo1==TIPO_DATO.BIT and instr.get("tipodato").get("tipo")==TIPO_DATO.INT:
                        respuesta.append(int(i))
                    elif tipo1==TIPO_DATO.BIT and instr.get("tipodato").get("tipo")==TIPO_DATO.DECIMAL:
                        respuesta.append(round(float(i),2))
                    elif tipo1==TIPO_DATO.BIT and (instr.get("tipodato").get("tipo")==TIPO_DATO.CHAR or instr.get("tipodato").get("tipo")==TIPO_DATO.VARCHAR):
                        if instr.get("tipodato").get("tipo")==TIPO_DATO.CHAR:
                            #justificar con espacios al final  
                            respuesta.append(str(i).ljust(instr.get("tipodato").get("longitud")))
                        else:
                            respuesta.append(str(i))
                    elif (tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and instr.get("tipodato").get("tipo")==TIPO_DATO.INT:
                        sumaassii=0
                        for j in i:
                            sumaassii+=ord(j)
                        respuesta.append(sumaassii)
                    elif (tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and instr.get("tipodato").get("tipo")==TIPO_DATO.DECIMAL:
                        sumaassii=0
                        for j in i:
                            sumaassii+=ord(j)
                        respuesta.append(round(float(sumaassii),2))
                    elif (tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and instr.get("tipodato").get("tipo")==TIPO_DATO.BIT:
                        sumaassii=0
                        for j in i:
                            sumaassii+=ord(j)
                        if sumaassii==0:
                            respuesta.append(0)
                        else:
                            respuesta.append(1)
                    elif (tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (instr.get("tipodato").get("tipo")==TIPO_DATO.CHAR or instr.get("tipodato").get("tipo")==TIPO_DATO.VARCHAR):
                        if len(str(i))>instr.get("tipodato").get("longitud"):
                            respuesta.append(str(i)[:instr.get("tipodato").get("longitud")])
                        else:
                            if instr.get("tipodato").get("tipo")>TIPO_DATO.CHAR:
                                #completar con espacios al final jstifi
                                respuesta.append(str(i).ljust(instr.get("tipodato").get("longitud")))
                            else:
                                # igual
                                respuesta.append(str(i))
                    elif (tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and instr.get("tipodato").get("tipo")==TIPO_DATO.DATE:
                        error=False
                        try:
                            fecha=datetime.strptime(i, '%d/%m/%Y').strftime('%d-%m-%Y')
                            
                        except ValueError:
                            error=True
                        try:
                            
                            fecha=datetime.strptime(fecha, '%d/%m/%Y %H:%M:%S').strftime('%d-%m-%Y')
                            error=False
                        except ValueError:
                            error=True
                        
                        if error:
                            print("Error: no se puede castear el valor "+str(i)+" a tipo DATE")
                            listatipodatos.append("ERROR")
                            return ["ERROR"]
                        else:
                            respuesta.append(str(fecha))        
                    elif (tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and instr.get("tipodato").get("tipo")==TIPO_DATO.DATETIME:
                        error=False
                        fecha=""
                        try:
                            fecha=datetime.strptime(i, '%d/%m/%Y').strftime('%d-%m-%Y %H:%M:%S')
                            
                        except ValueError:
                            error=True
                        try:
                            
                            fecha=datetime.strptime(fecha, '%d/%m/%Y %H:%M:%S').strftime('%d-%m-%Y %H:%M:%S')
                            error=False
                        except ValueError:
                            error=True
                        
                        if error:
                            print("Error: no se puede castear el valor "+str(i)+" a tipo DATETIME")
                            listatipodatos.append("ERROR")
                            return ["ERROR"]
                        else:
                            respuesta.append(str(fecha))
                    elif tipo1==TIPO_DATO.DATE and (instr.get("tipodato").get("tipo")==TIPO_DATO.CHAR or instr.get("tipodato").get("tipo")==TIPO_DATO.VARCHAR):
                        fecha=""
                        try:
                            fecha=datetime.strptime(i, '%d-%m-%Y').strftime('%d/%m/%Y')
                            
                        except ValueError:
                            print("Error: no se puede castear el valor "+str(i)+" a tipo CHAR")
                            listatipodatos.append("ERROR")
                            return ["ERROR"]
                        if len(str(fecha))>instr.get("tipodato").get("longitud"):
                            respuesta.append(str(fecha)[:instr.get("tipodato").get("longitud")])
                        else:
                            #completar con espacios al final jstifi
                            if instr.get("tipodato").get("tipo")>TIPO_DATO.CHAR:
                                respuesta.append(str(fecha).ljust(instr.get("tipodato").get("longitud")))
                            else:
                                respuesta.append(str(fecha))
                    elif tipo1==TIPO_DATO.DATE and instr.get("tipodato").get("tipo")==TIPO_DATO.DATETIME:
                        fecha=""
                        try:
                            fecha=datetime.strptime(i, '%d-%m-%Y').strftime('%d/%m/%Y %H:%M:%S')
                            
                        except ValueError:
                            print("Error: no se puede castear el valor "+str(i)+" a tipo DATETIME")
                            listatipodatos.append("ERROR")
                            return ["ERROR"]
                        respuesta.append(str(fecha))
                    elif tipo1==TIPO_DATO.DATETIME and (instr.get("tipodato").get("tipo")==TIPO_DATO.CHAR or instr.get("tipodato").get("tipo")==TIPO_DATO.VARCHAR):
                        fecha=""
                        try:
                            fecha=datetime.strptime(i, '%d-%m-%Y %H:%M:%S').strftime('%d/%m/%Y %H:%M:%S')
                            
                        except ValueError:
                            print("Error: no se puede castear el valor "+str(i)+" a tipo CHAR")
                            listatipodatos.append("ERROR")
                            return ["ERROR"]
                        if len(str(fecha))>instr.get("tipodato").get("longitud"):
                            respuesta.append(str(fecha)[:instr.get("tipodato").get("longitud")])
                        else:
                            #completar con espacios al final jstifi
                            if instr.get("tipodato").get("tipo")>TIPO_DATO.CHAR:
                                respuesta.append(str(fecha).ljust(instr.get("tipodato").get("longitud")))
                            else:
                                respuesta.append(str(fecha))
                    elif tipo1==TIPO_DATO.DATETIME and instr.get("tipodato").get("tipo")==TIPO_DATO.DATE:
                        fecha=""
                        try:
                            fecha=datetime.strptime(i, '%d-%m-%Y %H:%M:%S').strftime('%d-%m-%Y')
                            
                        except ValueError:
                            print("Error: no se puede castear el valor "+str(i)+" a tipo DATE")
                            listatipodatos.append("ERROR")
                            return ["ERROR"]
                        respuesta.append(str(fecha))
                    else:
                        print("Error: no se puede castear el valor "+str(i)+" a tipo "+str(instr.get("tipodato").get("tipo")))
                        listatipodatos.append("ERROR")
                        return ["ERROR"]

                    
            listatipodatos.append(instr.get("tipodato").get("tipo"))
            
            print("respuesta: ",respuesta,"tipo:",listatipodatos)

            return respuesta
        elif instr.get("tipo")==TIPO_INSTRUCCION.IF:
            
            exp1=procesar_where1(instr.get("condicion"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            exp2=procesar_where1(instr.get("verdadero"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            exp3=procesar_where1(instr.get("falso"), base, tabla)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            
            print("")
            print("if ",exp1)
            exp1 = procesar_dato(exp1)
            exp2 = procesar_dato(exp2)
            exp3 = procesar_dato(exp3)
            tipo3 = listatipodatos.pop()
            tipo2 = listatipodatos.pop()
            tipo1 = listatipodatos.pop()

            if isinstance(exp1, dict):
                tipo1 = exp1.get("tipo")
                exp1 = exp1.get("dato")
               
            if isinstance(exp2, dict):
                tipo2 = exp2.get("tipo")
                exp2 = exp2.get("dato")
               
            if isinstance(exp3, dict):
                tipo3 = exp3.get("tipo")
                exp3 = exp3.get("dato")
                
            print("exp1: ",exp1," V: ",exp2," F: ",exp3)
            respuesta = []
            if len(exp1)>1 and len(exp2)>1 and len(exp3)>1:
                for i, j,k in zip(exp1, exp2,exp3):
                    print("i: ",tipo1," j: ",tipo2," k: ",tipo3)
                    if i is None :
                        print("Error: no se puede evaluar un valor nulo")
                        listatipodatos.append("ERROR")
                        return ["ERROR"]
                    if i:
                        respuesta.append(j)
                        listatipodatos.append(tipo2)
                    else:
                        respuesta.append(k)
                        listatipodatos.append(tipo3)
                
            else:
                for i in exp1:
                    print("i: ",tipo1," j: ",tipo2," k: ",tipo3)
                    if i is None :
                        print("Error: no se puede evaluar un valor nulo")
                        listatipodatos.append("ERROR")
                        return ["ERROR"]
                    if i:
                        respuesta.append(exp2[0])
                        listatipodatos.append(tipo2)
                    else:
                        respuesta.append(exp3[0])
                        listatipodatos.append(tipo3)
          
            print("respuesta: ",respuesta,"tipo:",listatipodatos)
            return respuesta
                              
        else:
            print("Error: instruccion no valida")
            listatipodatos.append("ERROR")
            return ["ERROR"]
    else:
        listatipodatos.append("noinstr")
        return instr
    
def procesar_dato(cadena):
    # si expresion contine comillas dobles o simples escribir algo
    if isinstance(cadena, str):
        if not cadena.startswith('\"') and not cadena.startswith('\''):
            # se tiene que buscar en la tabla la columna correspondiente
            colum=xml.obtener_registros(basedata,table,cadena)
            print("colum: ",colum)
            listatipodatos.append(colum.get("tipo"))
            
            return colum
        
        elif cadena.startswith('@'):
            # se tiene que buscar en la tabla de simbolos
            listatipodatos.append(TIPO_DATO.INT)
            return [5]
        else:
            # quitar las comillas
            cadena = cadena[1:-1]
            tip=TIPO_DATO.VARCHAR
            try:
                # Intenta convertir la cadena en una fecha
                datetime.strptime(cadena, '%d-%m-%Y')
                tip=TIPO_DATO.DATE
            except ValueError:
                pass

            try:
                # Intenta convertir la cadena en una fecha con hora
                datetime.strptime(cadena, '%d-%m-%Y %H:%M:%S')
                tip=TIPO_DATO.DATETIME
            except ValueError:
                pass
            
            listatipodatos.append(tip)
            return [cadena]
    else:
        tip=""
        if isinstance(cadena, list):
            return cadena
        else:
            if isinstance(cadena, int):
                tip = TIPO_DATO.INT
            else:
                tip=TIPO_DATO.DECIMAL
            listatipodatos.append(tip)
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