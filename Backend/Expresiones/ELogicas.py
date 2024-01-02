from datetime import datetime
from Analizadores.instrucciones import *


def and_logico(exp1,exp2):
    respuesta = []
    tiporesult = []
    try:
        if len(exp1)>1 and len(exp2)>1:
            respuesta = [1 if i and j else 0 for i, j in zip(exp1, exp2)]
            tiporesult=[TIPO_DATO.BIT for i, j in zip(exp1, exp2)]
        else:
            respuesta = [1 if i and j else 0 for i in exp1 for j in exp2]
            tiporesult=[TIPO_DATO.BIT for i in exp1 for j in exp2]
    except:
        print("Error: no se puede comparar los valores "+str(exp1)+" y "+str(exp2))
        return {"respuesta":"no se puede comparar los valores "+str(exp1)+" y "+str(exp2),"tipo":"ERROR"}

    print("respuesta: ",respuesta,"tipo:",tiporesult)
    return {"respuesta":respuesta,"tipo":tiporesult}

def or_logico(exp1,exp2):
    respuesta = []
    tiporesult = []
    try:
        if len(exp1)>1 and len(exp2)>1:
            respuesta = [1 if i or j else 0 for i, j in zip(exp1, exp2)]
            tiporesult=[TIPO_DATO.BIT for i, j in zip(exp1, exp2)]
        else:
            respuesta = [1 if i or j else 0 for i in exp1 for j in exp2]
            tiporesult=[TIPO_DATO.BIT for i in exp1 for j in exp2]
    except:
        print("Error: no se puede comparar los valores "+str(exp1)+" y "+str(exp2))
        return {"respuesta":"no se puede comparar los valores "+str(exp1)+" y "+str(exp2),"tipo":"ERROR"}

    
    print("respuesta: ",respuesta,"tipo:",tiporesult)
    return {"respuesta":respuesta,"tipo":tiporesult}

def not_logico(exp1):
    tiporesult = []
    respuesta = []
    try:

        for i in exp1:
            respuesta.append(int(not i))
            tiporesult.append(TIPO_DATO.BIT)
    except:
        print("Error: no se puede negar el valor "+str(exp1))
        return {"respuesta":"no se puede negar el valor "+str(exp1),"tipo":"ERROR"}
    
    print("respuesta: ",respuesta,"tipo:",tiporesult)
    return {"respuesta":respuesta,"tipo":tiporesult}

def procesar_beetwen(exp1,exp2,exp3,tipoE1,tipoE2,tipoE3):
    respuesta = []
    tiporesult  = []

    if len(exp1) > 1 and len(exp2) > 1 and len(exp3)>1:
        for i,j,k,tipo1,tipo2,tipo3 in zip(exp1,exp2,exp3,tipoE1,tipoE2,tipoE3):
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
                return {"respuesta":"no se puede evaluar si "+str(i)+" esta entre "+str(j)+" y "+str(k),"tipo":"ERROR"}
            
            tiporesult.append(TIPO_DATO.BIT)
    else:
        a=-1
        for i in exp1:
            a+=1
            print("i: ",tipoE1[a]," j: ",tipoE2[0]," k: ",tipoE3[0])
            if ((tipoE1[a]==TIPO_DATO.INT or tipoE1[a]==TIPO_DATO.DECIMAL) and (tipoE2[0]==TIPO_DATO.INT or tipoE2[0]==TIPO_DATO.DECIMAL) and (tipoE3[0]==TIPO_DATO.INT or tipoE3[0]==TIPO_DATO.DECIMAL)) or ((tipoE1[a]==TIPO_DATO.CHAR or tipoE1[a]==TIPO_DATO.VARCHAR) and (tipoE2[0]==TIPO_DATO.CHAR or tipoE2[0]==TIPO_DATO.VARCHAR) and (tipoE3[0]==TIPO_DATO.CHAR or tipoE3[0]==TIPO_DATO.VARCHAR)):
                if exp2[0]<=i<=exp3[0]:
                    respuesta.append(1)
                else:
                    respuesta.append(0)
            elif (tipoE1[a]==TIPO_DATO.DATE or tipoE1[a]==TIPO_DATO.DATETIME) and (tipoE2[0]==TIPO_DATO.DATE or tipoE2[0]==TIPO_DATO.DATETIME) and (tipoE3[0]==TIPO_DATO.DATE or tipoE3[0]==TIPO_DATO.DATETIME):
                if  datetime.strptime(exp2[0], '%d-%m-%Y %H:%M:%S')<= datetime.strptime(i, '%d-%m-%Y %H:%M:%S') <= datetime.strptime(exp3[0], '%d-%m-%Y %H:%M:%S'):
                    respuesta.append(1)
                else:
                    respuesta.append(0)
            else:
                print("Error: no se puede evaluar si  "+str(i)+" esta entre "+str(exp2[0])+" y "+str(exp3[0]))
                return {"respuesta":"no se puede evaluar si  "+str(i)+" esta entre "+str(exp2[0])+" y "+str(exp3[0]),"tipo":"ERROR"}
                 
            tiporesult.append(TIPO_DATO.BIT)

    print("respuesta: ",respuesta,"tipo:",tiporesult)
    return {"respuesta":respuesta,"tipo":tiporesult}