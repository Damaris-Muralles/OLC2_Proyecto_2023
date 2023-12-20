
from Analizadores.instrucciones import *

def if_simple(exp1,exp2,exp3,tipoE1,tipoE2,tipoE3):
    respuesta = []
    tiporesult=[]

    if len(exp1)>1 and len(exp2)>1 and len(exp3)>1:
        for i, j,k,tipo1,tipo2,tipo3 in zip(exp1, exp2,exp3,tipoE1,tipoE2,tipoE3):
            print("i: ",tipo1," j: ",tipo2," k: ",tipo3)
            if i is None :
                print("Error: no se puede evaluar un valor nulo")
                return {"respuesta":"ERROR","tipo":"ERROR"}
            if i:
                respuesta.append(j)
                tiporesult.append(tipo2)
            else:
                respuesta.append(k)
                tiporesult.append(tipo3)
        
    else:
        for i in range(len(exp1)):
            print("i: ",tipoE1[i]," j: ",tipoE2[0]," k: ",tipoE3[0])
            if exp1[i] is None :
                print("Error: no se puede evaluar un valor nulo")
                return {"respuesta":"ERROR","tipo":"ERROR"}
            if exp1[i]:
                respuesta.append(exp2[0])
                tiporesult.append(tipoE2[0])
            else:
                respuesta.append(exp3[0])
                tiporesult.append(tipoE3[0])

    print("respuesta: ",respuesta,"tipo:",tiporesult)
    return {"respuesta":respuesta,"tipo":tiporesult}

def if_procedure_funcion():
    pass