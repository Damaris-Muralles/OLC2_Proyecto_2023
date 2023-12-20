from datetime import datetime
from Analizadores.instrucciones import *


def mayor_que(exp1,exp2,tipoE1,tipoE2):
    
    respuesta = []
    tiporesult=[]

    if len(exp1) > 1 and len(exp2) > 1:
        for i,j,tipo1,tipo2 in zip(exp1,exp2,tipoE1,tipoE2):
            print("i: ",tipo1," j: ",tipo2)
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
                return {"respuesta":"ERROR","tipo":"ERROR"}
    else:
        a=-1
        for i in exp1:
            a+=1
            b=-1
            for j in exp2:
                b+=1
                print("i: ",tipoE1[a]," j: ",tipoE2[b])
                if ((tipoE1[a]==TIPO_DATO.INT or tipoE1[a]==TIPO_DATO.DECIMAL) and (tipoE2[b]==TIPO_DATO.INT or tipoE2[b]==TIPO_DATO.DECIMAL)) or ((tipoE1[a]==TIPO_DATO.CHAR or tipoE1[a]==TIPO_DATO.VARCHAR) and (tipoE2[b]==TIPO_DATO.CHAR or tipoE2[b]==TIPO_DATO.VARCHAR)):
                    if i>j:
                        respuesta.append(1)
                    else:
                        respuesta.append(0)
                    tiporesult.append(TIPO_DATO.BIT)
                elif (tipoE1[a]==TIPO_DATO.DATE or tipoE1[a]==TIPO_DATO.DATETIME) and (tipoE2[b]==TIPO_DATO.DATE or tipoE2[b]==TIPO_DATO.DATETIME):
                    if datetime.strptime(i, '%d-%m-%Y %H:%M:%S') > datetime.strptime(j, '%d-%m-%Y %H:%M:%S'):
                        respuesta.append(1)
                    else:
                        respuesta.append(0)
                        tiporesult.append(TIPO_DATO.BIT)
                else:
                    print("Error: no se puede comparar los valores "+str(i)+" y "+str(j))
                 
                    return {"respuesta":"ERROR","tipo":"ERROR"}
    
    print("respuesta: ",respuesta,"tipo:",tiporesult)
    return {"respuesta":respuesta,"tipo":tiporesult}

def menor_que(exp1,exp2,tipoE1,tipoE2):
    respuesta = []
    tiporesult = []

    if len(exp1) > 1 and len(exp2) > 1:
        for i,j,tipo1,tipo2 in zip(exp1,exp2,tipoE1,tipoE2):
            print("i: ",tipo1," j: ",tipo2)
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
                return {"respuesta":"ERROR","tipo":"ERROR"} 
            
            tiporesult.append(TIPO_DATO.BIT) 
    else:
        a=-1
        for i in exp1:
            a+=1
            b=-1
            for j in exp2:
                b+=1
                print("i: ",tipoE1[a]," j: ",tipoE2[b])
                if ((tipoE1[a]==TIPO_DATO.INT or tipoE1[a]==TIPO_DATO.DECIMAL) and (tipoE2[b]==TIPO_DATO.INT or tipoE2[b]==TIPO_DATO.DECIMAL)) or ((tipoE1[a]==TIPO_DATO.CHAR or tipoE1[a]==TIPO_DATO.VARCHAR) and (tipoE2[b]==TIPO_DATO.CHAR or tipoE2[b]==TIPO_DATO.VARCHAR)):
                    if i<j:
                        respuesta.append(1)
                    else:
                        respuesta.append(0)
                elif (tipoE1[a]==TIPO_DATO.DATE or tipoE1[a]==TIPO_DATO.DATETIME) and (tipoE2[b]==TIPO_DATO.DATE or tipoE2[b]==TIPO_DATO.DATETIME):
                    if datetime.strptime(i, '%d-%m-%Y %H:%M:%S') < datetime.strptime(j, '%d-%m-%Y %H:%M:%S'):
                        respuesta.append(1)
                    else:
                        respuesta.append(0)
                else:
                    print("Error: no se puede comparar los valores "+str(i)+" y "+str(j))
                    
                    return {"respuesta":"ERROR","tipo":"ERROR"}   
                tiporesult.append(TIPO_DATO.BIT)   
    
    print("respuesta: ",respuesta,"tipo:",tiporesult)
    return {"respuesta":respuesta,"tipo":tiporesult}

def menor_igual_que(exp1,exp2,tipoE1,tipoE2):
    respuesta = []
    tiporesult=[]

    if len(exp1) > 1 and len(exp2) > 1:
        for i,j,tipo1,tipo2 in zip(exp1,exp2,tipoE1,tipoE2):
            print("i: ",tipo1," j: ",tipo2)
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
                
                return {"respuesta":"ERROR","tipo":"ERROR"}  
            tiporesult.append(TIPO_DATO.BIT)
    else:
        a=-1
        for i in exp1:
            a+=1
            b=-1
            for j in exp2:
                b+=1
                print("i: ",tipoE1[a]," j: ",tipoE2[b])
                if ((tipoE1[a]==TIPO_DATO.INT or tipoE1[a]==TIPO_DATO.DECIMAL) and (tipoE2[b]==TIPO_DATO.INT or tipoE2[b]==TIPO_DATO.DECIMAL)) or ((tipoE1[a]==TIPO_DATO.CHAR or tipoE1[a]==TIPO_DATO.VARCHAR) and (tipoE2[b]==TIPO_DATO.CHAR or tipoE2[b]==TIPO_DATO.VARCHAR)):
                    if i<=j:
                        respuesta.append(1)
                    else:
                        respuesta.append(0)
                elif (tipoE1[a]==TIPO_DATO.DATE or tipoE1[a]==TIPO_DATO.DATETIME) and (tipoE2[b]==TIPO_DATO.DATE or tipoE2[b]==TIPO_DATO.DATETIME):
                    if datetime.strptime(i, '%d-%m-%Y %H:%M:%S') <= datetime.strptime(j, '%d-%m-%Y %H:%M:%S'):
                        respuesta.append(1)
                    else:
                        respuesta.append(0)
                else:
                    print("Error: no se puede comparar los valores "+str(i)+" y "+str(j))
                    
                    return {"respuesta":"ERROR","tipo":"ERROR"}    
                tiporesult.append(TIPO_DATO.BIT)  
    
    
    print("respuesta: ",respuesta,"tipo:",tiporesult)
    return {"respuesta":respuesta,"tipo":tiporesult}

def mayor_igual_que(exp1,exp2,tipoE1,tipoE2):
    respuesta = []
    tiporesult=[]

    if len(exp1) > 1 and len(exp2) > 1:
        for i,j,tipo1,tipo2 in zip(exp1,exp2,tipoE1,tipoE2):
            print("i: ",tipo1," j: ",tipo2)
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
                
                return {"respuesta":"ERROR","tipo":"ERROR"}  
            tiporesult.append(TIPO_DATO.BIT)
    else:
        a=-1
        for i in exp1:
            a+=1
            b=-1
            for j in exp2:
                b+=1
                print("i: ",tipoE1[a]," j: ",tipoE2[b])
                if ((tipoE1[a]==TIPO_DATO.INT or tipoE1[a]==TIPO_DATO.DECIMAL) and (tipoE2[b]==TIPO_DATO.INT or tipoE2[b]==TIPO_DATO.DECIMAL)) or ((tipoE1[a]==TIPO_DATO.CHAR or tipoE1[a]==TIPO_DATO.VARCHAR) and (tipoE2[b]==TIPO_DATO.CHAR or tipoE2[b]==TIPO_DATO.VARCHAR)):
                    if i>=j:
                        respuesta.append(1)
                    else:
                        respuesta.append(0)
                elif (tipoE1[a]==TIPO_DATO.DATE or tipoE1[a]==TIPO_DATO.DATETIME) and (tipoE2[b]==TIPO_DATO.DATE or tipoE2[b]==TIPO_DATO.DATETIME):
                    if datetime.strptime(i, '%d-%m-%Y %H:%M:%S') >= datetime.strptime(j, '%d-%m-%Y %H:%M:%S'):
                        respuesta.append(1)
                    else:
                        respuesta.append(0)
                else:
                    print("Error: no se puede comparar los valores "+str(i)+" y "+str(j))
                    
                    return {"respuesta":"ERROR","tipo":"ERROR"}      
            tiporesult.append(TIPO_DATO.BIT)
    
    
    print("respuesta: ",respuesta,"tipo:",tiporesult)
    return {"respuesta":respuesta,"tipo":tiporesult}

def igual_que(exp1,exp2,tipoE1,tipoE2):
    respuesta = []
    tiporesult = []

    if len(exp1) > 1 and len(exp2) > 1:
        for i,j,tipo1,tipo2 in zip(exp1,exp2,tipoE1,tipoE2):
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
                
                return {"respuesta":"ERROR","tipo":"ERROR"}  
            tiporesult.append(TIPO_DATO.BIT)
    else:
        a=-1
        for i in exp1:
            a+=1
            b=-1
            for j in exp2:
                b+=1
                print("i: ",tipoE1[a]," j: ",tipoE2[b])
                if ((tipoE1[a]==TIPO_DATO.INT or tipoE1[a]==TIPO_DATO.DECIMAL) and (tipoE2[b]==TIPO_DATO.INT or tipoE2[b]==TIPO_DATO.DECIMAL)) or ((tipoE1[a]==TIPO_DATO.CHAR or tipoE1[a]==TIPO_DATO.VARCHAR) and (tipoE2[b]==TIPO_DATO.CHAR or tipoE2[b]==TIPO_DATO.VARCHAR)):
                    if i==j:
                        respuesta.append(1)
                    else:
                        respuesta.append(0)
                elif (tipoE1[a]==TIPO_DATO.DATE or tipoE1[a]==TIPO_DATO.DATETIME) and (tipoE2[b]==TIPO_DATO.DATE or tipoE2[b]==TIPO_DATO.DATETIME):
                    if datetime.strptime(i, '%d-%m-%Y %H:%M:%S') == datetime.strptime(j, '%d-%m-%Y %H:%M:%S'):
                        respuesta.append(1)
                    else:
                        respuesta.append(0)
                else:
                    print("Error: no se puede comparar los valores "+str(i)+" y "+str(j))
                    
                    return {"respuesta":"ERROR","tipo":"ERROR"} 
                tiporesult.append(TIPO_DATO.BIT)     
    
    
    print("respuesta: ",respuesta,"tipo:",tiporesult)
    return {"respuesta":respuesta,"tipo":tiporesult}

def diferente_que(exp1,exp2,tipoE1,tipoE2):
    respuesta = []
    tiporesult = []

    if len(exp1) > 1 and len(exp2) > 1:
        for i,j,tipo1,tipo2 in zip(exp1,exp2,tipoE1,tipoE2):
        
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
                
                return {"respuesta":"ERROR","tipo":"ERROR"}  
            tiporesult.append(TIPO_DATO.BIT)
    else:
        a=-1
        for i in exp1:
            a+=1
            b=-1
            for j in exp2:
                b+=1
                print("i: ",tipoE1[a]," j: ",tipoE2[b])
                if ((tipoE1[a]==TIPO_DATO.INT or tipoE1[a]==TIPO_DATO.DECIMAL) and (tipoE2[b]==TIPO_DATO.INT or tipoE2[b]==TIPO_DATO.DECIMAL)) or ((tipoE1[a]==TIPO_DATO.CHAR or tipoE1[a]==TIPO_DATO.VARCHAR) and (tipoE2[b]==TIPO_DATO.CHAR or tipoE2[b]==TIPO_DATO.VARCHAR)):
                    if i!=j:
                        respuesta.append(1)
                    else:
                        respuesta.append(0)
                elif (tipoE1[a]==TIPO_DATO.DATE or tipoE1[a]==TIPO_DATO.DATETIME) and (tipoE2[b]==TIPO_DATO.DATE or tipoE2[b]==TIPO_DATO.DATETIME):
                    if datetime.strptime(i, '%d-%m-%Y %H:%M:%S') != datetime.strptime(j, '%d-%m-%Y %H:%M:%S'):
                        respuesta.append(1)
                    else:
                        respuesta.append(0)
                else:
                    print("Error: no se puede comparar los valores "+str(i)+" y "+str(j))
                    
                    return {"respuesta":"ERROR","tipo":"ERROR"}   
                tiporesult.append(TIPO_DATO.BIT)   
    
    print("respuesta: ",respuesta,"tipo:",tiporesult)
    return {"respuesta":respuesta,"tipo":tiporesult}
