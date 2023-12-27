from Expresiones.Where import *
from Analizadores.instrucciones import *


def procesar_insert(instr,ActualBaseDatos,xml):#arreglar lo de atributos
    
    valoreslist=instr.get("valores")
    for i in range(len(valoreslist)):
        if str(valoreslist[i]).startswith('@'):
            valor=obtener_variable(valoreslist[i])
            if valor.get("tipo")=="ERROR":
                return {"datos": "Error en la variable", "tipo": "ERROR"}
            else:
                if valor.get("tipo")==TIPO_DATO.CHAR or valor.get("tipo")==TIPO_DATO.VARCHAR or valor.get("tipo")==TIPO_DATO.DATE or valor.get("tipo")==TIPO_DATO.DATETIME:
                    valoreslist[i]=str(valor.get("dato"))
                elif valor.get("tipo")==TIPO_DATO.DECIMAL:
                    valoreslist[i]=round(float(valor.get("dato")),2)
                else:
                    valoreslist[i]=int(valor.get("dato"))
  
    print(xml.insert_data(ActualBaseDatos,instr.get("id"),instr.get("columnas"),valoreslist))

def procesar_delete(instr,ActualBaseDatos,xml, entorno): # si esta referenciada en otra tabla
    print("lista de tipos actual: ",listatipodatos)
    eliminar=procesar_where1(instr.get("where"),ActualBaseDatos, instr.get("id"), entorno)
   
    if listatipodatos and listatipodatos[-1] == "ERROR":
        return {"datos": "Error en sentenica where", "tipo": "ERROR"}
    else:
        datos=listatipodatos.pop()
        #si todos los elementos en la lista son tipo_dato.bit ejectua el xml si no, error de tipos
        if all(x == TIPO_DATO.BIT for x in datos):

            print(xml.delete_registro(ActualBaseDatos, instr.get("id"),eliminar))
        else:
            return {"datos": "La condicion en where debe ser de tipo boolean", "tipo": "ERROR"}
          

def procesar_update(instr,ActualBaseDatos,xml, entorno):
    print(instr)
    if instr.get("id")!=None:
        comprobador.agregar([instr.get("id")])
    whereupdate = procesar_where1(instr.get("where"),ActualBaseDatos, instr.get("id"), entorno)
    listset = []
    if listatipodatos and listatipodatos[-1] == "ERROR":
        return {"datos": "Error en sentenica where", "tipo": "ERROR"}
    tipodatolist=listatipodatos.pop()
    for i in instr.get("set"):
        if isinstance(i.get("exp2"),dict):
            
             listset.append(procesar_where1(i.get("exp2"), ActualBaseDatos, instr.get("id"), entorno))
        else:
            #If que valide que no sea tipo int o float
            print (not(type(i.get("exp2"))) == int)
            if type(i.get("exp2")) != int and type(i.get("exp2")) != float:
                print(type(i.get("exp2")))
                if i.get("exp2").startswith('@'):
                    variable=obtener_variable(i.get("exp2"),entorno)
                    print("error: ", variable)
                    if variable.get("tipo")[0]==TIPO_DATO.VARCHAR or variable.get("tipo")[0]==TIPO_DATO.CHAR:
                        variable.get("dato")[0] = (variable.get("dato")[0])[1:-1]
                        
                    resultado =variable.get("dato")
                    listset.append(resultado)
                else:
                    listset.append(procesar_where1(i.get("exp2"), ActualBaseDatos, instr.get("id"), entorno))
            else:
                listset.append(procesar_where1(i.get("exp2"), ActualBaseDatos, instr.get("id"), entorno))
            
    if listatipodatos and listatipodatos[-1] == "ERROR":
        return {"datos": "Error en sentenica where", "tipo": "ERROR"}    
        
    #print(listset)

    print(xml.UpdateTable(ActualBaseDatos, instr.get("id"),instr.get("set"), listset,whereupdate))

def procesar_select(instr,ActualBaseDatos,xml, entorno):
    print("lista de tipos actual: ",listatipodatos)
    columna=instr.get("columna")  
    tabla=instr.get("tablas")
    where=instr.get("where") 
    print("columna: ",columna)
    print("tabla: ",tabla)

    # ver si hay * en las columnas, no esta permitido cuando hay mas de una columna
    if len(columna)==0: # en teoria nunca entra aqui
        print ("no hay datos a mostrar")
    else:
        if len(columna)>1 :
            c=0
            for j in columna:
                if j.get("colum")=="*":
                    c=c+1
            if c>0:
                print("Error en select, no se puede usar * con otras columnas")
                return

    if tabla!=None:
        comprobador.agregar(tabla)

    # vermos si hay mas de una tabla 
    if tabla!=None and len(tabla)>1:
        # ver si hay columnas con el mismo nombre en las tablas
        columnascomprobadas=0
        for col in columna:
            igualcolum=0
            tabref=""
            comp1=0
            if isinstance(col.get("colum"),dict):
                columnascomprobadas+=1
            else:
                igualcolum,tabref,comp1=comprobador.comprobar(col.get("colum"),xml,ActualBaseDatos)
            if igualcolum==-1:
                print("ERROR")
                return
            columnascomprobadas+=comp1
            if igualcolum>1:
                print("Error en el select, la columna ",col.get("colum")," esta en mas de una de las tablas usadas")
                return
            elif igualcolum==1:
                
                if ("." in col.get("colum"))!=True:
                    columnascomprobadas+=1
                    # si existe se agrega de la forma tabla.columna en la misma posicion
                    nombrecol=col.get("colum")
                    col["colum"] = tabref + "." + nombrecol
            
        
        print("columnas comprobadas: ",columnascomprobadas," columnas: ",len(columna))
        if columnascomprobadas!=len(columna):
            print("Error en el select, no se encontraron todas las columnas")
            return    

    

    
    condiciones=[]
    if where!=None and tabla==None:
        print("Error en sentenica where")
    if where!=None and tabla!=None:
        condiciones=procesar_where1(where,ActualBaseDatos,tabla[0], entorno)
        if listatipodatos and listatipodatos[-1] == "ERROR":
            print("Error en sentenica where")
    
    # obtener los datos de la tabla
    
    tablarespuesta=[]
   
    
    for i in columna:
        print("------------------------------------")
        print("instruccion del select ",i.get("colum"))
        print("")

        if i.get("colum")=="*" and tabla!=None and len(tabla)==1:
            result=[]
            result1=xml.obtener_registros(ActualBaseDatos,tabla[0],"*todo*")
            if result1.get("tipo") == "ERROR":
                print("ERROR")
                return
            for j,k,l in zip(result1.get("dato"),result1.get("tipo"),result1.get("ids")):
                
                if where!=None:
                    resl=[]
                    tps=[]
                    for condicion in range(len(condiciones)):
                        if condiciones[condicion]==1:
                            resl.append(j[condicion])
                            tps.append(k[condicion])
                    tablarespuesta.append([l,resl,tps])
                else:
                    tablarespuesta.append([l,j,k])
        
        elif i.get("colum")!="*":
            if isinstance(i.get("colum"),dict):
                #encabezado
                encabezado=i.get("colum").get("tipo").name
                if i.get("encabezado")!=None:
                    encabezado=i.get("encabezado")

                if i.get("colum").get("tipo")==TIPO_INSTRUCCION.SUMA:  
                    tipodsuma=[]
                    if tabla==None:
                        print("Se requiere de un from para sumar la columna ")
                        return "ERROR"
                    result=funcion_sumar( i.get("colum").get("columna"),condiciones,ActualBaseDatos,comprobador,xml)
                    if result.get("tipo") == "ERROR":
                            print("ERROR")
                            return
                    tipodsuma=result.get("tipo")
                    result=result.get("respuesta")
                    tablarespuesta.append([encabezado,result,tipodsuma])
                elif i.get("colum").get("tipo")==TIPO_INSTRUCCION.CONTAR: 
                    tipodcont=[]
                    if tabla==None and len(tabla)!=1:
                        print("ERROR: Se requiere 1 tabla de referencia para sumar la columna ")
                        return "ERROR"
                    result=funcion_contar( i.get("colum").get("columna"),condiciones,ActualBaseDatos,tabla[0],xml)
                    if result.get("tipo") == "ERROR":
                            print("ERROR")
                            return
                    tipodsuma=result.get("tipo")
                    result=result.get("respuesta")
                    tablarespuesta.append([encabezado,result,tipodsuma])
                else:
                    t=tabla
                    if tabla!=None:
                        t=tabla[0]
                   
                    result=procesar_where1( i.get("colum"),ActualBaseDatos,t, entorno)
                    
                    if isinstance(result,list):
                        result=result
                    else:
                        result=[result]
                    
                    ttipo=[]
                    if listatipodatos and listatipodatos[-1] == "ERROR":
                            print("ERROR")
                            return
                    else:
                        ttipo=listatipodatos.pop()
                    
                    if where!=None:
                        resl=[]
                        tipod=[]
                        for condicion in range(len(condiciones)):
                            if condiciones[condicion]==1:
                                if len(result)==len(condiciones):
                                    resl.append(result[condicion])
                                    tipod.append(ttipo[condicion])
                        if len(resl)==0:
                            resl.append(result)
                            tipod.append(ttipo)

                        
                        tablarespuesta.append([encabezado,resl,tipod])
                    else:
                        tablarespuesta.append([encabezado,result,ttipo])
                    
            elif tabla!=None:
                colum=obtener_id(ActualBaseDatos,tabla,i.get("colum")) 

                encabezado=i.get("colum")
                if i.get("encabezado")!=None:
                    encabezado=i.get("encabezado")
                if colum.get("tipo")!="ERROR":
                    print("colum: ",colum) 
                    print("condiciones: ",condiciones)
                    if where!=None:
                        resl=[]
                        td=[]
                        for condicion in range(len(condiciones)):
                            if condiciones[condicion]==1:
                                resl.append(colum.get("dato")[condicion])
                                td.append(colum.get("tipo")[condicion])
                        tablarespuesta.append([encabezado,resl,td])
                    else:
                        tablarespuesta.append([encabezado,colum.get("dato"),colum.get("tipo")])
                else:
                    print("ERROR:No es posible realizar el select")
                    return   
            else:
                print("Se requiere de un from para la columna ",i.get("colum"))
                return
        
        
        
        
        
        else:
            print("ERROR:No es posible realizar el select")
            return
        print("------------------------------------") 





    print("tabla respuesta: ",tablarespuesta)