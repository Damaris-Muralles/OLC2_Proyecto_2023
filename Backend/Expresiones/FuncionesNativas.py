from datetime import datetime
from Analizadores.instrucciones import *


def funcion_hoy():
    fecha_hora_actual = datetime.now()
    fecha_hora_formateada = fecha_hora_actual.strftime("\'%d-%m-%Y %H:%M:%S\'")
    print("respuesta: ",fecha_hora_formateada,"tipo:",TIPO_DATO.DATETIME)
    return {"respuesta":fecha_hora_formateada,"tipo":TIPO_DATO.DATETIME}

def funcion_concatena(exp1,exp2,tipoE1,tipoE2):
    respuesta = []
    tiporesult=[]
    if len(exp1)>1 and len(exp2)>1:
        for i, j,tipo1,tipo2 in zip(exp1, exp2,tipoE1,tipoE2):
            print("i: ",tipo1," j: ",tipo2)
            if i is None or j is None:
                print("Error: no se puede concatenar con un valor nulo")
                return {"respuesta":"no se puede concatenar con un valor nulo","tipo":"ERROR"}
            # si tienen formato de fecha o fecha hora, error
            elif is_date_or_datetime(i) or is_date_or_datetime(j):
                print("Error: no se puede concatenar con un valor de tipo fecha o fecha hora")
                return {"respuesta":"no se puede concatenar con un valor de tipo fecha o fecha hora","tipo":"ERROR"}
            # si son int o float, error
            elif tipo1==TIPO_DATO.INT or tipo1==TIPO_DATO.DECIMAL or tipo2==TIPO_DATO.INT or tipo2==TIPO_DATO.DECIMAL:
                print("Error: no se puede concatenar con un valor de tipo entero o decimal")
                return {"respuesta":"no se puede concatenar con un valor de tipo entero o decimal","tipo":"ERROR"}
            
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
                    return {"respuesta":"no se puede concatenar con un valor nulo","tipo":"ERROR"}
                # si tienen formato de fecha o fecha hora, error
                elif is_date_or_datetime(i) or is_date_or_datetime(j):
                    print("Error: no se puede concatenar con un valor de tipo fecha o fecha hora")
                    return {"respuesta":"no se puede concatenar con un valor de tipo fecha o fecha hora","tipo":"ERROR"}
                # si son int o float, error
                elif tipoE1[a]==TIPO_DATO.INT or tipoE1[a]==TIPO_DATO.DECIMAL or tipoE2[b]==TIPO_DATO.INT or tipoE2[b]==TIPO_DATO.DECIMAL:
                    print("Error: no se puede concatenar con un valor de tipo entero o decimal")
                    return {"respuesta":"no se puede concatenar con un valor de tipo entero o decimal","tipo":"ERROR"}
                
                c1=str(i)
                c2=str(j)
                # añadir a la respuesta
                respuesta.append(f"{c1+c2}")
                tiporesult.append(TIPO_DATO.VARCHAR)
    
    print("respuesta: ",respuesta,"tipo:",tiporesult)
    return {"respuesta":respuesta,"tipo":tiporesult}

def funcion_substraer(exp1,exp2,exp3,tipoE1,tipoE2,tipoE3):
    respuesta = []
    tiporesult=[]

    if len(exp1)>1 and len(exp2)>1 and len(exp3)>1:
        for i, j,k,tipo1,tipo2,tipo3 in zip(exp1, exp2,exp3,tipoE1,tipoE2,tipoE3 ):
            if i is None :
                print("Error: no se puede substraer de un valor nulo")
                return {"respuesta":"no se puede substraer de un valor nulo","tipo":"ERROR"}
            # si tienen formato de fecha o fecha hora, error
            elif is_date_or_datetime(i) :
                print("Error: no se puede substraer de un valor de tipo fecha o fecha hora")
                return {"respuesta":"no se puede substraer de un valor de tipo fecha o fecha hora","tipo":"ERROR"}
            elif tipo1 == TIPO_DATO.INT or tipo1 == TIPO_DATO.DECIMAL:
                print("Error: no se puede substraer de un valor de tipo entero o decimal")
                return {"respuesta":"no se puede substraer de un valor de tipo entero o decimal","tipo":"ERROR"}
            # si son int o float, error
            elif isinstance(i,int) or isinstance(i,float):
                print("Error: no se puede substraer de un valor de tipo entero o decimal")
                return {"respuesta":"no se puede substraer de un valor de tipo entero o decimal","tipo":"ERROR"}
            
            elif tipo2 != TIPO_DATO.INT or tipo3 != TIPO_DATO.INT:
                print("Error: Para substraer se necesita de dos valores enteros como parametros")
                return {"respuesta":"Para substraer se necesita de dos valores enteros como parametros","tipo":"ERROR"}
            
            try:
                if j-1<0:
                    print("Error: no se puede substraer el valor "+str(j)+" esta fuera de rango")
                    return {"respuesta":"no se puede substraer el valor "+str(j)+" esta fuera de rango","tipo":"ERROR"}
                c1=i[j-1:k]
                
                # añadir a la respuesta
                respuesta.append(f"{c1}")
                tiporesult.append(TIPO_DATO.VARCHAR)
            except:
                print("Error: no se puede substraer de desde el caracter "+str(j)+" hasta el caracter "+str(k)+" de la cadena "+str(i))
                return {"respuesta":"no se puede substraer de desde el caracter "+str(j)+" hasta el caracter "+str(k)+" de la cadena "+str(i),"tipo":"ERROR"}
                
    else:
        cont=-1
        for i in exp1:  
            cont+=1
            if i is None :
                print("Error: no se puede substraer de un valor nulo")
                return {"respuesta":"no se puede substraer de un valor nulo","tipo":"ERROR"}
            # si tienen formato de fecha o fecha hora, error
            elif is_date_or_datetime(i) :
                print("Error: no se puede substraer de un valor de tipo fecha o fecha hora")
                return {"respuesta":"no se puede substraer de un valor de tipo fecha o fecha hora","tipo":"ERROR"}
            elif tipoE1[cont] == TIPO_DATO.INT or tipoE1[cont] == TIPO_DATO.DECIMAL:
                print("Error: no se puede substraer de un valor de tipo entero o decimal")
                return {"respuesta":"no se puede substraer de un valor de tipo entero o decimal","tipo":"ERROR"}
            # si son int o float, error
            elif isinstance(i,int) or isinstance(i,float):
                print("Error: no se puede substraer de un valor de tipo entero o decimal")
                return {"respuesta":"no se puede substraer de un valor de tipo entero o decimal","tipo":"ERROR"}
            
            elif tipoE2[0] != TIPO_DATO.INT or tipoE3[0] != TIPO_DATO.INT:
                print("Error: Para substraer se necesita de dos valores enteros como parametros")
                return {"respuesta":"Para substraer se necesita de dos valores enteros como parametros","tipo":"ERROR"}
            try:
                if exp2[0]-1<0:
                    print("Error: no se puede substraer el valor "+str(exp2[0])+" esta fuera de rango")
                    return {"respuesta":"no se puede substraer el valor "+str(exp2[0])+" esta fuera de rango","tipo":"ERROR"}
                c1=i[exp2[0]-1:exp3[0]]
                
                # añadir a la respuesta
                respuesta.append(f"{c1}")
                tiporesult.append(TIPO_DATO.VARCHAR)
            except:
                print("Error: no se puede substraer de desde el caracter "+str(exp2[0])+" hasta el caracter "+str(exp3[0])+" de la cadena "+str(i))
                return {"respuesta":"no se puede substraer de desde el caracter "+str(exp2[0])+" hasta el caracter "+str(exp3[0])+" de la cadena "+str(i),"tipo":"ERROR"}
    
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
                return {"respuesta":"no se puede castear un valor nulo","tipo":"ERROR"}
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
                    return {"respuesta":"no se puede castear el valor "+str(exp1[i])+" a tipo DATE","tipo":"ERROR"}
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
                    return {"respuesta":"no se puede castear el valor "+str(exp1[i])+" a tipo DATETIME","tipo":"ERROR"}
                else:
                    respuesta.append(str(fecha))
            elif tipoE1[i]==TIPO_DATO.DATE and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR):
                fecha=""
                try:
                    fecha=datetime.strptime(exp1[i], '%d-%m-%Y')
                    
                except ValueError:
                    print("Error: no se puede castear el valor "+str(exp1[i])+" a tipo ",tipo2.name)
                    return {"respuesta":"no se puede castear el valor "+str(exp1[i])+" a tipo "+tipo2.name,"tipo":"ERROR"}
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
                    return {"respuesta":"no se puede castear el valor "+str(exp1[i])+" a tipo DATETIME","tipo":"ERROR"}
                respuesta.append(str(fecha))
            elif tipoE1[i]==TIPO_DATO.DATETIME and (tipo2==TIPO_DATO.CHAR or tipo2==TIPO_DATO.VARCHAR):
                fecha=""
                try:
                    fecha=datetime.strptime(exp1[i], '%d-%m-%Y %H:%M:%S')
                    
                except ValueError:
                    print("Error: no se puede castear el valor "+str(exp1[i])+" a tipo ",tipo2.name)
                    return {"respuesta":"no se puede castear el valor "+str(exp1[i])+" a tipo "+tipo2.name,"tipo":"ERROR"}
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
                    return {"respuesta":"no se puede castear el valor "+str(exp1[i])+" a tipo DATE","tipo":"ERROR"}
                respuesta.append(str(fecha))
            else:
                print("Error: no se puede castear el valor "+str(exp1[i])+" a tipo "+str(tipo2))
                return {"respuesta":"no se puede castear el valor "+str(exp1[i])+" a tipo "+str(tipo2),"tipo":"ERROR"}

            
            tiporesult.append(tipo2)
    
    print("respuesta: ",respuesta,"tipo:",tiporesult)
    return {"respuesta":respuesta,"tipo":tiporesult}

def funcion_sumar(exp1,condicion,basedatos,tab,xml):
    respuesta = []
    tiporesult=[]
    tabla=""
    print("exp1: ",exp1," condicion: ",condicion)
    
    
    if exp1 =="*":
        return {"respuesta":["ERROR"],"tipo":"ERROR"}
    else:
        igualcolum=0
        tabref=""
        comp1=0
        
        igualcolum,tabref,comp1=tab.comprobar(exp1,xml,basedatos)
        
        if igualcolum==-1:
                print("ERROR: al buscar columna ",exp1," en las tablas")
                return {"respuesta": ["ERROR"], "tipo": "ERROR"}
        
        if comp1==1:
            tabla=exp1.split(".")[0]
            exp1=exp1.split(".")[1]
        elif comp1==0:
            if igualcolum==1:
                tabla=tabref
            elif igualcolum>1:
                print("Error: la columna ",exp1," existe en mas de una de las tablas especificadas")
                return {"respuesta": ["ERROR"], "tipo": "ERROR"}
            else:
                print("Error: la columna ",exp1," no existe en las tablas")
                return {"respuesta": ["ERROR"], "tipo": "ERROR"}


        suma=0
        exp1=xml.obtener_registros(basedatos,tabla,exp1)
        if exp1.get("tipo")=="ERROR":
            return {"respuesta":["ERROR"],"tipo":"ERROR"}
        tipoE1=exp1.get("tipo")
        exp1=exp1.get("dato")
        if len(condicion)!=0:
            for i,tipo1,j in zip(exp1,tipoE1,condicion):
                if i is None:
                    print("Error: no se puede sumar un valor nulo")
                    return {"respuesta":["ERROR"],"tipo":"ERROR"}
                if tipo1==TIPO_DATO.INT or tipo1==TIPO_DATO.DECIMAL or tipo1==TIPO_DATO.BIT:
                    if j==1:
                        suma+=round(float(i),2)
                else:
                    print("Error: no se puede sumar un valor de tipo ",tipo1.name)
                    return {"respuesta":["ERROR"],"tipo":"ERROR"}
        else:
            for i,tipo1 in zip(exp1,tipoE1):
                if i is None:
                    print("Error: no se puede sumar un valor nulo")
                    return {"respuesta":["ERROR"],"tipo":"ERROR"}
                if tipo1==TIPO_DATO.INT or tipo1==TIPO_DATO.DECIMAL or tipo1==TIPO_DATO.BIT:
                    suma+=round(float(i),2)
                else:
                    if i!="null":
                        print("Error: no se puede sumar un valor de tipo ",tipo1.name)
                        return {"respuesta":["ERROR"],"tipo":"ERROR"}
        respuesta.append(suma)
        tiporesult.append(TIPO_DATO.DECIMAL)
            
    print("respuesta: ",respuesta,"tipo:",tiporesult)
    return {"respuesta":respuesta,"tipo":tiporesult}

def funcion_contar(exp1,condicion,basedatos,tabla,xml):
    respuesta = []
    tiporesult=[]
    print("exp1: ",exp1," condicion: ",condicion)
    
    if exp1 =="*":
        
        suma=0
        exp1=xml.obtener_registros(basedatos,tabla,"*todo*")
        print("exp1: ",exp1)
        if exp1.get("tipo")=="ERROR":
            return {"respuesta":["ERROR"],"tipo":"ERROR"}
        exp1=exp1.get("dato")[0]
        if len(condicion)!=0:
            if len(exp1)==0:
                print("Error: no hay registros para contar")
                return {"respuesta":["ERROR"],"tipo":"ERROR"}
            if len(exp1)==len(condicion):
                suma=condicion.count(1)  
        else:
            if len(exp1)==0:
                print("Error: no hay registros para contar")
                return {"respuesta":["ERROR"],"tipo":"ERROR"}
            suma=len(exp1)
                   
        respuesta.append(suma)
        tiporesult.append(TIPO_DATO.INT)
    else:
        return{"respuesta":["ERROR"],"tipo":"ERROR"}
            
    print("respuesta: ",respuesta,"tipo:",tiporesult)
    return {"respuesta":respuesta,"tipo":tiporesult}

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