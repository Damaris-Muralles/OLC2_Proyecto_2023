from datetime import datetime
from Analizadores.instrucciones import *


    
def suma_op(exp1,exp2,tipoE1,tipoE2):
    tiporesult=""
    respuesta = []
    tipres=[]
    if len(exp1)>1 and len(exp2)>1:
        for i, j,tipo1,tipo2 in zip(exp1, exp2,tipoE1,tipoE2):
            dat = 0
            print("i: ",tipo1," j: ",tipo2)
            if (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.BIT) :
              
                dat = i or j
                tiporesult = TIPO_DATO.BIT
            elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.INT) :
                dat = int(i + j)
                tiporesult = TIPO_DATO.INT
            elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.DECIMAL) :
                dat = round(float(i + j),2)
                tiporesult = TIPO_DATO.DECIMAL
            elif (tipo1==TIPO_DATO.BIT and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR) ):
                dat = str(i) + str(j)
                tiporesult=TIPO_DATO.VARCHAR
            elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.BIT) :
                dat = int(i + j)
                tiporesult = TIPO_DATO.INT
            elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.INT):
                dat = int(i + j)
                tiporesult = TIPO_DATO.INT
            elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.DECIMAL) :
                dat = round(float(i + j),2)
                tiporesult = TIPO_DATO.DECIMAL
            elif (tipo1==TIPO_DATO.INT and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR) ):
                dat = str(i) + str(j)
                tiporesult=TIPO_DATO.VARCHAR
            elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.BIT) :
                dat = round(float(i + j),2)
                tiporesult = TIPO_DATO.DECIMAL
            elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.INT) :
                dat = round(float(i + j),2)
                tiporesult = TIPO_DATO.DECIMAL
            elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.DECIMAL) :
                dat = round(float(i + j),2)
                tiporesult = TIPO_DATO.DECIMAL
            elif (tipo1==TIPO_DATO.DECIMAL and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR) ):
                dat = str(i) + str(j)
                tiporesult=TIPO_DATO.VARCHAR
            elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and tipo2==TIPO_DATO.BIT) :
                dat = str(i) + str(j)
                tiporesult=TIPO_DATO.VARCHAR
            elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and tipo2==TIPO_DATO.INT):
                dat = str(i) + str(j)
                tiporesult=TIPO_DATO.VARCHAR
            elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and tipo2==TIPO_DATO.DECIMAL) :
                dat = str(i) + str(j)
                tiporesult=TIPO_DATO.VARCHAR
            elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR) and   isinstance(i,str)):
                dat = str(i) + str(j)
                tiporesult=TIPO_DATO.VARCHAR
            else:
                print("Error: no se puede sumar los valores "+str(i)+" y "+str(j))
                return {"respuesta":"no se puede sumar los valores "+str(i)+" y "+str(j),"tipo":"ERROR"}
                
            tipres.append(tiporesult)
            respuesta.append(dat)

    else:
        a=-1
        for i in exp1:
            a+=1
            b=-1
            for j in exp2:
                b+=1
                dat = 0
                print("i: ",tipoE1[a]," j: ",tipoE2[b])
                if (tipoE1[a]==TIPO_DATO.BIT and tipoE2[b]==TIPO_DATO.BIT) :
                    dat = i or j
                    tiporesult = TIPO_DATO.BIT
                elif (tipoE1[a]==TIPO_DATO.BIT and tipoE2[b]==TIPO_DATO.INT) :
                    dat = int(i + j)
                    tiporesult = TIPO_DATO.INT
                elif (tipoE1[a]==TIPO_DATO.BIT and tipoE2[b]==TIPO_DATO.DECIMAL):
                    dat = round(float(i + j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif (tipoE1[a]==TIPO_DATO.BIT and (tipoE2[b]==TIPO_DATO.CHAR or tipoE2[b]==TIPO_DATO.VARCHAR) ) :
                    dat = str(i) + str(j)
                    tiporesult=TIPO_DATO.VARCHAR
                elif (tipoE1[a]==TIPO_DATO.INT and tipoE2[b]==TIPO_DATO.BIT) :
                    dat = int(i + j)
                    tiporesult = TIPO_DATO.INT
                elif (tipoE1[a]==TIPO_DATO.INT and tipoE2[b]==TIPO_DATO.INT) :
                    dat = int(i + j)
                    tiporesult = TIPO_DATO.INT
                elif (tipoE1[a]==TIPO_DATO.INT and tipoE2[b]==TIPO_DATO.DECIMAL):
                    dat = round(float(i + j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif (tipoE1[a]==TIPO_DATO.INT and (tipoE2[b]==TIPO_DATO.CHAR or tipoE2[b]==TIPO_DATO.VARCHAR) ) :
                    dat = str(i) + str(j)
                    tiporesult=TIPO_DATO.VARCHAR
                elif (tipoE1[a]==TIPO_DATO.DECIMAL and tipoE2[b]==TIPO_DATO.BIT) :
                    dat = round(float(i + j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif (tipoE1[a]==TIPO_DATO.DECIMAL and tipoE2[b]==TIPO_DATO.INT) :
                    dat = round(float(i + j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif (tipoE1[a]==TIPO_DATO.DECIMAL and tipoE2[b]==TIPO_DATO.DECIMAL) :
                    dat = round(float(i + j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif (tipoE1[a]==TIPO_DATO.DECIMAL and (tipoE2[b]==TIPO_DATO.CHAR or tipoE2[b]==TIPO_DATO.VARCHAR) ) :
                    dat = str(i) + str(j)
                    tiporesult=TIPO_DATO.VARCHAR
                elif ((tipoE1[a]==TIPO_DATO.CHAR or tipoE1[a]==TIPO_DATO.VARCHAR) and tipoE2[b]==TIPO_DATO.BIT):
                    dat = str(i) + str(j)
                    tiporesult=TIPO_DATO.VARCHAR
                elif ((tipoE1[a]==TIPO_DATO.CHAR or tipoE1[a]==TIPO_DATO.VARCHAR) and tipoE2[b]==TIPO_DATO.INT) :
                    dat = str(i) + str(j)
                    tiporesult=TIPO_DATO.VARCHAR
                elif ((tipoE1[a]==TIPO_DATO.CHAR or tipoE1[a]==TIPO_DATO.VARCHAR) and tipoE2[b]==TIPO_DATO.DECIMAL) :
                    dat = str(i) + str(j)
                    tiporesult=TIPO_DATO.VARCHAR
                elif ((tipoE1[a]==TIPO_DATO.CHAR or tipoE1[a]==TIPO_DATO.VARCHAR) and (tipoE2[b]==TIPO_DATO.CHAR or tipoE2[b]==TIPO_DATO.VARCHAR) and   isinstance(i,str)) :
                    dat = str(i) + str(j)
                    tiporesult=TIPO_DATO.VARCHAR
                else:
                    print("Error: no se puede sumar los valores "+str(i)+" y "+str(j))
                    return {"respuesta":"no se puede sumar los valores "+str(i)+" y "+str(j),"tipo":"ERROR"}
                    
                tipres.append(tiporesult)
                respuesta.append(dat)   

    
    
    print("respuesta: ",respuesta,"tipo:",tipres)
    return {"respuesta":respuesta,"tipo":tipres}

def resta_op(exp1,exp2,tipoE1,tipoE2):
    tiporesult=""
    respuesta = []
    tipres=[]
    
    if len(exp1)>1 and len(exp2)>1:
        for i, j,tipo1,tipo2 in zip(exp1, exp2,tipoE1,tipoE2):
                dat = 0
                print("i: ",tipo1," j: ",tipo2)
                if (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.INT) :
                    dat = int(i - j)
                    tiporesult = TIPO_DATO.INT
                elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.DECIMAL) :
                    dat = round(float(i - j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.BIT) :
                    dat = int(i - j)
                    tiporesult = TIPO_DATO.INT
                elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.INT) :
                    dat = int(i - j)
                    tiporesult = TIPO_DATO.INT
                elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.DECIMAL) :
                    dat = round(float(i - j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.BIT) :
                    dat = round(float(i - j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.INT) :
                    dat = round(float(i - j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.DECIMAL) :
                    dat = round(float(i - j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                else:
                    print("Error: no se puede restar los valores "+str(i)+" y "+str(j))
                    return {"respuesta":"no se puede restar los valores "+str(i)+" y "+str(j),"tipo":"ERROR"}
                    
                tipres.append(tiporesult)
                respuesta.append(dat)  
    else:
        a=-1
        for i in exp1:
            a+=1
            b=-1
            for j in exp2:
                b+=1
                dat = 0
                print("i: ",tipoE1[a]," j: ",tipoE2[b])
                if (tipoE1[a]==TIPO_DATO.BIT and tipoE2[b]==TIPO_DATO.INT) :
                    dat = int(i - j)
                    tiporesult = TIPO_DATO.INT
                elif (tipoE1[a]==TIPO_DATO.BIT and tipoE2[b]==TIPO_DATO.DECIMAL):
                    dat = round(float(i - j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif (tipoE1[a]==TIPO_DATO.INT and tipoE2[b]==TIPO_DATO.BIT) :
                    dat = int(i - j)
                    tiporesult = TIPO_DATO.INT
                elif (tipoE1[a]==TIPO_DATO.INT and tipoE2[b]==TIPO_DATO.INT):
                    dat = int(i - j)
                    tiporesult = TIPO_DATO.INT
                elif (tipoE1[a]==TIPO_DATO.INT and tipoE2[b]==TIPO_DATO.DECIMAL) :
                    dat = round(float(i - j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif (tipoE1[a]==TIPO_DATO.DECIMAL and tipoE2[b]==TIPO_DATO.BIT) :
                    dat = round(float(i - j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif (tipoE1[a]==TIPO_DATO.DECIMAL and tipoE2[b]==TIPO_DATO.INT) :
                    dat = round(float(i - j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif (tipoE1[a]==TIPO_DATO.DECIMAL and tipoE2[b]==TIPO_DATO.DECIMAL) :
                    dat = round(float(i - j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                else:
                    print("Error: no se puede restar los valores "+str(i)+" y "+str(j))
                    return {"respuesta":"no se puede restar los valores "+str(i)+" y "+str(j),"tipo":"ERROR"}
                    
                tipres.append(tiporesult)
                respuesta.append(dat)   

    
    print("respuesta: ",respuesta,"tipo:",tipres)
    return {"respuesta":respuesta,"tipo":tipres}

def multiplicacion_op(exp1,exp2,tipoE1,tipoE2):
    tiporesult=""
    respuesta = []
    tipres=[]
    if len(exp1)>1 and len(exp2)>1:
        for i, j,tipo1,tipo2 in zip(exp1, exp2,tipoE1,tipoE2):
                print("i: ",tipo1," j: ",tipo2)
                dat = 0
                if (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.BIT) :
                    dat = i and j
                    tiporesult = TIPO_DATO.BIT
                elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.INT) :
                    dat = int(i * j)
                    tiporesult = TIPO_DATO.INT
                elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.DECIMAL) :
                    dat = round(float(i * j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.BIT) :
                    dat = int(i * j)
                    tiporesult = TIPO_DATO.INT
                elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.INT) :
                    dat = int(i * j)
                    tiporesult = TIPO_DATO.INT
                elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.DECIMAL) :
                    dat = round(float(i * j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.BIT) :
                    dat = round(float(i * j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.INT) :
                    dat = round(float(i * j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.DECIMAL) :
                    dat = round(float(i * j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.DATE or tipo2==TIPO_DATO.DATETIME )) :
                    dat = str(i) + str(j)
                    tiporesult=TIPO_DATO.VARCHAR
                elif ((tipo1==TIPO_DATO.DATE or tipo1==TIPO_DATO.DATETIME) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR )) :
                    dat = str(i) + str(j)
                    tiporesult=TIPO_DATO.VARCHAR
                else:
                    print("Error: no se puede multiplicar los valores "+str(i)+" y "+str(j))
                    return {"respuesta":"no se puede multiplicar los valores "+str(i)+" y "+str(j),"tipo":"ERROR"}
                    
                tipres.append(tiporesult)
                respuesta.append(dat)  
    else:
        a=-1
        for i in exp1:
            a+=1
            b=-1
            for j in exp2:
                b+=1
                print("i: ",tipoE1[a]," j: ",tipoE2[b])
                dat = 0
                if (tipoE1[a]==TIPO_DATO.BIT and tipoE2[b]==TIPO_DATO.BIT):
                    dat = i and j
                    tiporesult = TIPO_DATO.BIT
                elif (tipoE1[a]==TIPO_DATO.BIT and tipoE2[b]==TIPO_DATO.INT) :
                    dat = int(i * j)
                    tiporesult = TIPO_DATO.INT
                elif (tipoE1[a]==TIPO_DATO.BIT and tipoE2[b]==TIPO_DATO.DECIMAL) :
                    dat = round(float(i * j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif (tipoE1[a]==TIPO_DATO.INT and tipoE2[b]==TIPO_DATO.BIT) :
                    dat = int(i * j)
                    tiporesult = TIPO_DATO.INT
                elif (tipoE1[a]==TIPO_DATO.INT and tipoE2[b]==TIPO_DATO.INT) :
                    dat = int(i * j)
                    tiporesult = TIPO_DATO.INT
                elif (tipoE1[a]==TIPO_DATO.INT and tipoE2[b]==TIPO_DATO.DECIMAL):
                    dat = round(float(i * j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif (tipoE1[a]==TIPO_DATO.DECIMAL and tipoE2[b]==TIPO_DATO.BIT) :
                    dat = round(float(i * j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif (tipoE1[a]==TIPO_DATO.DECIMAL and tipoE2[b]==TIPO_DATO.INT) :
                    dat = round(float(i * j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif (tipoE1[a]==TIPO_DATO.DECIMAL and tipoE2[b]==TIPO_DATO.DECIMAL) :
                    dat = round(float(i * j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif ((tipoE1[a]==TIPO_DATO.CHAR or tipoE1[a]==TIPO_DATO.VARCHAR) and (tipoE2[b]==TIPO_DATO.DATE or tipoE2[b]==TIPO_DATO.DATETIME )):
                    dat = str(i) + str(j)
                    tiporesult=TIPO_DATO.VARCHAR
                elif ((tipoE1[a]==TIPO_DATO.DATE or tipoE1[a]==TIPO_DATO.DATETIME) and (tipoE2[b]==TIPO_DATO.CHAR or tipoE2[b]==TIPO_DATO.VARCHAR )) :
                    dat = str(i) + str(j)
                    tiporesult=TIPO_DATO.VARCHAR
                else:
                    print("Error: no se puede multiplicar los valores "+str(i)+" y "+str(j))
                    return {"respuesta":"no se puede multiplicar los valores "+str(i)+" y "+str(j),"tipo":"ERROR"}
                    
                tipres.append(tiporesult)
                respuesta.append(dat)   

    
    print("respuesta: ",respuesta,"tipo:",tipres)
    return {"respuesta":respuesta,"tipo":tipres}

def division_op(exp1,exp2,tipoE1,tipoE2):
    tiporesult=""
    tipres=[]
    respuesta = []
    if len(exp1)>1 and len(exp2)>1:
        for i, j,tipo1,tipo2 in zip(exp1, exp2,tipoE1,tipoE2):
            print("i: ",tipo1," j: ",tipo2)
            try:
                dat = 0
                if (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.INT):
                    dat = int(i / j)
                    tiporesult = TIPO_DATO.INT
                elif (tipo1==TIPO_DATO.BIT and tipo2==TIPO_DATO.DECIMAL):
                    dat = round(float(i / j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.BIT) :
                    dat = int(i / j)
                    tiporesult = TIPO_DATO.INT
                elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.INT) :
                    dat = int(i / j)
                    tiporesult = TIPO_DATO.INT
                elif (tipo1==TIPO_DATO.INT and tipo2==TIPO_DATO.DECIMAL):
                    dat = round(float(i / j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.BIT):
                    dat = round(float(i / j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.INT):
                    dat = round(float(i / j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif (tipo1==TIPO_DATO.DECIMAL and tipo2==TIPO_DATO.DECIMAL) :
                    dat = round(float(i / j),2)
                    tiporesult = TIPO_DATO.DECIMAL
                elif ((tipo1==TIPO_DATO.CHAR or tipo1==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.DATE or tipo2==TIPO_DATO.DATETIME )):
                    dat = str(i) + str(j)
                    tiporesult=TIPO_DATO.VARCHAR
                elif ((tipo1==TIPO_DATO.DATE or tipo1==TIPO_DATO.DATETIME) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR )) :
                    dat = str(i) + str(j)
                    tiporesult=TIPO_DATO.VARCHAR
                else:
                    print("Error: no se puede dividir los valores "+str(i)+" y "+str(j))
                    return {"respuesta":"no se puede dividir los valores "+str(i)+" y "+str(j),"tipo":"ERROR"}
                    
                tipres.append(tiporesult)
                respuesta.append(dat) 
            except ZeroDivisionError:
                print("¡Error! División por cero.") 
                return {"respuesta":"No es valida la division por 0","tipo":"ERROR"}
    else:
        a=-1
        for i in exp1:
            a+=1
            b=-1
            try:
                for j in exp2:
                    b+=1
                    print("i: ",tipoE1[a]," j: ",tipoE2[b])
                    dat = 0
                    if (tipoE1[a]==TIPO_DATO.BIT and tipoE2[b]==TIPO_DATO.INT) :
                        dat = int(i / j)
                        tiporesult = TIPO_DATO.INT
                    elif (tipoE1[a]==TIPO_DATO.BIT and tipoE2[b]==TIPO_DATO.DECIMAL) :
                        dat = round(float(i / j),2)
                        tiporesult = TIPO_DATO.DECIMAL
                    elif (tipoE1[a]==TIPO_DATO.INT and tipoE2[b]==TIPO_DATO.BIT) :
                        dat = int(i / j)
                        tiporesult = TIPO_DATO.INT
                    elif (tipoE1[a]==TIPO_DATO.INT and tipoE2[b]==TIPO_DATO.INT) :
                        dat = int(i / j)
                        tiporesult = TIPO_DATO.INT
                    elif (tipoE1[a]==TIPO_DATO.INT and tipoE2[b]==TIPO_DATO.DECIMAL) :
                        dat = round(float(i / j),2)
                        tiporesult = TIPO_DATO.DECIMAL
                    elif (tipoE1[a]==TIPO_DATO.DECIMAL and tipoE2[b]==TIPO_DATO.BIT) :
                        dat = round(float(i / j),2)
                        tiporesult = TIPO_DATO.DECIMAL
                    elif (tipoE1[a]==TIPO_DATO.DECIMAL and tipoE2[b]==TIPO_DATO.INT) :
                        dat = round(float(i / j),2)
                        tiporesult = TIPO_DATO.DECIMAL
                    elif (tipoE1[a]==TIPO_DATO.DECIMAL and tipoE2[b]==TIPO_DATO.DECIMAL) :
                        dat = round(float(i / j),2)
                        tiporesult = TIPO_DATO.DECIMAL
                    elif ((tipoE1[a]==TIPO_DATO.CHAR or tipoE1[a]==TIPO_DATO.VARCHAR) and (tipoE2[b]==TIPO_DATO.DATE or tipoE2[b]==TIPO_DATO.DATETIME )) :
                        dat = str(i) + str(j)
                        tiporesult=TIPO_DATO.VARCHAR
                    elif ((tipoE1[a]==TIPO_DATO.DATE or tipoE1[a]==TIPO_DATO.DATETIME) and (tipoE2[b]==TIPO_DATO.CHAR or tipoE2[b]==TIPO_DATO.VARCHAR )) :
                        dat = str(i) + str(j)
                        tiporesult=TIPO_DATO.VARCHAR
                    else:
                        print("Error: no se puede dividir los valores "+str(i)+" y "+str(j))
                        return {"respuesta":"no se puede dividir los valores "+str(i)+" y "+str(j),"tipo":"ERROR"}
                            
                    tipres.append(tiporesult)
                    respuesta.append(dat) 
            except ZeroDivisionError:
                print("¡Error! División por cero.") 
                return {"respuesta":"No es valida la division por 0","tipo":"ERROR"}
            
    print("respuesta: ",respuesta,"tipo:",tipres)
    return {"respuesta":respuesta,"tipo":tipres}



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