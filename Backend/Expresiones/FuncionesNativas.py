from datetime import datetime
from Analizadores.instrucciones import *


def funcion_hoy():
    fecha_hora_actual = datetime.now()
    fecha_hora_formateada = fecha_hora_actual.strftime("\'%d-%m-%Y %H:%M:%S\'")
    print("respuesta: ",fecha_hora_formateada,"tipo:",TIPO_DATO.DATETIME)
    return {"respuesta: ",fecha_hora_formateada,"tipo:",TIPO_DATO.DATETIME}

def funcion_concatena(exp1,exp2,tipoE1,tipoE2):
    respuesta = []
    tiporesult=[]
    if len(exp1)>1 and len(exp2)>1:
        for i, j,tipo1,tipo2 in zip(exp1, exp2,tipoE1,tipoE2):
            print("i: ",tipo1," j: ",tipo2)
            if i is None or j is None:
                print("Error: no se puede concatenar con un valor nulo")
                return {"respuesta":"ERROR","tipo":"ERROR"}
            # si tienen formato de fecha o fecha hora, error
            elif is_date_or_datetime(i) or is_date_or_datetime(j):
                print("Error: no se puede concatenar con un valor de tipo fecha o fecha hora")
                return {"respuesta":"ERROR","tipo":"ERROR"}
            # si son int o float, error
            elif tipo1==TIPO_DATO.INT or tipo1==TIPO_DATO.DECIMAL or tipo2==TIPO_DATO.INT or tipo2==TIPO_DATO.DECIMAL:
                print("Error: no se puede concatenar con un valor de tipo entero o decimal")
                return {"respuesta":"ERROR","tipo":"ERROR"}
            
            c1=str(i)
            c2=str(j)
            # añadir a la respuesta
            respuesta.append(f"\'{c1+c2}\'")
            tiporesult.append(TIPO_DATO.VARCHAR)
            
    else:
        a=-1
        for i in exp1:
            a+=1
            b=-1
            for j in exp2:
                b+=1
                print("i: ",tipoE1[a]," j: ",tipoE2[b])
                if i is None or j is None:
                    print("Error: no se puede concatenar con un valor nulo")
                    return {"respuesta":"ERROR","tipo":"ERROR"}
                # si tienen formato de fecha o fecha hora, error
                elif is_date_or_datetime(i) or is_date_or_datetime(j):
                    print("Error: no se puede concatenar con un valor de tipo fecha o fecha hora")
                    return {"respuesta":"ERROR","tipo":"ERROR"}
                # si son int o float, error
                elif tipoE1[a]==TIPO_DATO.INT or tipoE1[a]==TIPO_DATO.DECIMAL or tipoE2[b]==TIPO_DATO.INT or tipoE2[b]==TIPO_DATO.DECIMAL:
                    print("Error: no se puede concatenar con un valor de tipo entero o decimal")
                    return {"respuesta":"ERROR","tipo":"ERROR"}
                
                c1=str(i)
                c2=str(j)
                # añadir a la respuesta
                respuesta.append(f"{c1+c2}")
                tiporesult.append(TIPO_DATO.VARCHAR)
    
    print("respuesta: ",respuesta,"tipo:",tiporesult)
    return {"respuesta":respuesta,"tipo":tiporesult}

def funcion_substraer(exp1,exp2,exp3,tipoE2,tipoE3):
    respuesta = []
    tiporesult=[]

    if len(exp1)>1 and len(exp2)>1 and len(exp3)>1:
        for i, j,k,tipo2,tipo3 in zip(exp1, exp2,exp3,tipoE2,tipoE3 ):
            if i is None :
                print("Error: no se puede substraer de un valor nulo")
                return {"respuesta":"ERROR","tipo":"ERROR"}
            # si tienen formato de fecha o fecha hora, error
            elif is_date_or_datetime(i) :
                print("Error: no se puede substraer de un valor de tipo fecha o fecha hora")
                return {"respuesta":"ERROR","tipo":"ERROR"}
            # si son int o float, error
            elif isinstance(i,int) or isinstance(i,float):
                print("Error: no se puede substraer de un valor de tipo entero o decimal")
                return {"respuesta":"ERROR","tipo":"ERROR"}
            elif tipo2 != TIPO_DATO.INT or tipo3 != TIPO_DATO.INT:
                print("Error: Para substraer se necesita de dos valores enteros como parametros")
                return {"respuesta":"ERROR","tipo":"ERROR"}
            
            # substraer  cadena,inicio,fin
            c1= i[j:k]
            tiporesult.append(TIPO_DATO.VARCHAR)
            # añadir a la respuesta
            respuesta.append(f"{c1}")
                
    else:
        for i in exp1:  
            if i is None :
                print("Error: no se puede substraer de un valor nulo")
                return {"respuesta":"ERROR","tipo":"ERROR"}
            # si tienen formato de fecha o fecha hora, error
            elif is_date_or_datetime(i) :
                print("Error: no se puede substraer de un valor de tipo fecha o fecha hora")
                return {"respuesta":"ERROR","tipo":"ERROR"}
            # si son int o float, error
            elif isinstance(i,int) or isinstance(i,float):
                print("Error: no se puede substraer de un valor de tipo entero o decimal")
                return {"respuesta":"ERROR","tipo":"ERROR"}
            elif tipoE2[0] != TIPO_DATO.INT or tipoE3[0] != TIPO_DATO.INT:
                print("Error: Para substraer se necesita de dos valores enteros como parametros")
                return {"respuesta":"ERROR","tipo":"ERROR"}
            
            c1=i[exp2[0]:exp3[0]]
            
            # añadir a la respuesta
            respuesta.append(f"{c1}")
            tiporesult.append(TIPO_DATO.VARCHAR)
    
    print("respuesta: ",respuesta,"tipo:",tiporesult)
    return {"respuesta":respuesta,"tipo":tiporesult}  

def funcion_cast(exp1,tipoE1,tipo2,longitud):
    respuesta = []
    tiporesult=[]

    if len(exp1)>=1:
        for i in range(len(exp1)):
            print("i: ",tipoE1[i]," tipo2: ",tipo2)
            if exp1[i] is None :
                print("Error: no se puede castear un valor nulo")
                return {"respuesta":"ERROR","tipo":"ERROR"}
            elif (tipoE1[i]==TIPO_DATO.INT or tipoE1[i]==TIPO_DATO.DECIMAL) and tipo2==TIPO_DATO.BIT:
                if int(exp1[i])==0 :
                    respuesta.append(0)
                else:
                    respuesta.append(1)
            elif (tipoE1[i]==TIPO_DATO.INT or tipoE1[i]==TIPO_DATO.DECIMAL) and tipo2==TIPO_DATO.INT:
                respuesta.append(int(exp1[i]))
            elif (tipoE1[i]==TIPO_DATO.INT or tipoE1[i]==TIPO_DATO.DECIMAL) and tipo2==TIPO_DATO.DECIMAL:
                respuesta.append(round(float(exp1[i]),2))
            elif (tipoE1[i]==TIPO_DATO.INT or tipoE1[i]==TIPO_DATO.DECIMAL) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR):
                if 0<=int(exp1[i])<=255:
                    if tipo2==TIPO_DATO.CHAR:
                        #justificar con espacios al final  
                        respuesta.append(chr(int(exp1[i])).ljust(longitud))
                    else:
                        respuesta.append(chr(int(exp1[i])))
                else:
                    respuesta.append(None)
            elif tipoE1[i]==TIPO_DATO.BIT and tipo2==TIPO_DATO.INT:
                respuesta.append(int(exp1[i]))
            elif tipoE1[i]==TIPO_DATO.BIT and tipo2==TIPO_DATO.DECIMAL:
                respuesta.append(round(float(exp1[i]),2))
            elif tipoE1[i]==TIPO_DATO.BIT and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR):
                if tipo2==TIPO_DATO.CHAR:
                    #justificar con espacios al fexp1[i]al  
                    respuesta.append(str(i).ljust(longitud))
                else:
                    respuesta.append(str(exp1[i]))
            elif (tipoE1[i]==TIPO_DATO.CHAR or tipoE1[i]==TIPO_DATO.VARCHAR) and tipo2==TIPO_DATO.INT:
                sumaassii=0
                for j in exp1[i]:
                    sumaassii+=ord(j)
                respuesta.append(sumaassii)
            elif (tipoE1[i]==TIPO_DATO.CHAR or tipoE1[i]==TIPO_DATO.VARCHAR) and tipo2==TIPO_DATO.DECIMAL:
                sumaassii=0
                for j in exp1[i]:
                    sumaassii+=ord(j)
                respuesta.append(round(float(sumaassii),2))
            elif (tipoE1[i]==TIPO_DATO.CHAR or tipoE1[i]==TIPO_DATO.VARCHAR) and tipo2==TIPO_DATO.BIT:
                sumaassii=0
                for j in exp1[i]:
                    sumaassii+=ord(j)
                if sumaassii==0:
                    respuesta.append(0)
                else:
                    respuesta.append(1)
            elif (tipoE1[i]==TIPO_DATO.CHAR or tipoE1[i]==TIPO_DATO.VARCHAR) and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR):
                if len(str(exp1[i]))>longitud:
                    respuesta.append(str(exp1[i])[:longitud])
                else:
                    if tipo2>TIPO_DATO.CHAR:
                        #completar con espacios al final jstifi
                        respuesta.append(str(exp1[i]).ljust(longitud))
                    else:
                        # igual
                        respuesta.append(str(exp1[i]))
            elif (tipoE1[i]==TIPO_DATO.CHAR or tipoE1[i]==TIPO_DATO.VARCHAR) and tipo2==TIPO_DATO.DATE:
                error=False
                try:
                    fecha=datetime.strptime(exp1[i], '%d/%m/%Y').strftime('%d-%m-%Y')
                    
                except ValueError:
                    error=True
                try:
                    
                    fecha=datetime.strptime(exp1[i], '%d/%m/%Y %H:%M:%S').strftime('%d-%m-%Y')
                    error=False
                except ValueError:
                    error=True
                
                if error:
                    print("Error: no se puede castear el valor "+str(exp1[i])+" a tipo DATE")
                    return {"respuesta":"ERROR","tipo":"ERROR"}
                else:
                    respuesta.append(str(fecha))        
            elif (tipoE1[i]==TIPO_DATO.CHAR or tipoE1[i]==TIPO_DATO.VARCHAR) and tipo2==TIPO_DATO.DATETIME:
                error=False
                fecha=""
                try:
                    fecha=datetime.strptime(exp1[i], '%d/%m/%Y').strftime('%d-%m-%Y %H:%M:%S')
                    
                except ValueError:
                    error=True
                try:
                    
                    fecha=datetime.strptime(exp1[i], '%d/%m/%Y %H:%M:%S').strftime('%d-%m-%Y %H:%M:%S')
                    error=False
                except ValueError:
                    error=True
                
                if error:
                    print("Error: no se puede castear el valor "+str(exp1[i])+" a tipo DATETIME")
                    return {"respuesta":"ERROR","tipo":"ERROR"}
                else:
                    respuesta.append(str(fecha))
            elif tipoE1[i]==TIPO_DATO.DATE and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR):
                fecha=""
                try:
                    fecha=datetime.strptime(exp1[i], '%d-%m-%Y')
                    
                except ValueError:
                    print("Error: no se puede castear el valor "+str(exp1[i])+" a tipo ",tipo2.name)
                    return {"respuesta":"ERROR","tipo":"ERROR"}
                if len(str(fecha))>longitud:
                    respuesta.append(str(fecha)[:longitud])
                else:
                    #completar con espacios al final jstifi
                    if tipo2>TIPO_DATO.CHAR:
                        respuesta.append(str(fecha).ljust(longitud))
                    else:
                        respuesta.append(str(fecha))
            elif tipoE1[i]==TIPO_DATO.DATE and tipo2==TIPO_DATO.DATETIME:
                fecha=""
                try:
                    fecha=datetime.strptime(exp1[i], '%d-%m-%Y').strftime('%d-%m-%Y %H:%M:%S')
                    
                except ValueError:
                    print("Error: no se puede castear el valor "+str(exp1[i])+" a tipo DATETIME")
                    return {"respuesta":"ERROR","tipo":"ERROR"}
                respuesta.append(str(fecha))
            elif tipoE1[i]==TIPO_DATO.DATETIME and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR):
                fecha=""
                try:
                    fecha=datetime.strptime(exp1[i], '%d-%m-%Y %H:%M:%S')
                    
                except ValueError:
                    print("Error: no se puede castear el valor "+str(exp1[i])+" a tipo ",tipo2.name)
                    return {"respuesta":"ERROR","tipo":"ERROR"}
                if len(str(fecha))>longitud:
                    respuesta.append(str(fecha)[:longitud])
                else:
                    #completar con espacios al final jstifi
                    if tipo2>TIPO_DATO.CHAR:
                        respuesta.append(str(fecha).ljust(longitud))
                    else:
                        respuesta.append(str(fecha))
            elif tipoE1[i]==TIPO_DATO.DATETIME and tipo2==TIPO_DATO.DATE:
                fecha=""
                try:
                    fecha=datetime.strptime(exp1[i], '%d-%m-%Y %H:%M:%S').strftime('%d-%m-%Y')
                    
                except ValueError:
                    print("Error: no se puede castear el valor "+str(exp1[i])+" a tipo DATE")
                    return {"respuesta":"ERROR","tipo":"ERROR"}
                respuesta.append(str(fecha))
            else:
                print("Error: no se puede castear el valor "+str(exp1[i])+" a tipo "+str(tipo2))
                return {"respuesta":"ERROR","tipo":"ERROR"}

            
            tiporesult.append(tipo2)
    
    print("respuesta: ",respuesta,"tipo:",tiporesult)
    return {"respuesta":respuesta,"tipo":tiporesult}

def funcion_sumar():
    pass

def funcion_contar():
    pass

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