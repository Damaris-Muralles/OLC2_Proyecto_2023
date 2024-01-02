from datetime import datetime
from Analizadores.instrucciones import *


def funcion_case(listacase): 
    tiporesult = []
    respuesta = []
   
  
    
    if listacase != None:
        
         # crear una lista con el mismo tamaño de los casos en la lista de casos
        case= listacase[0]
        val = case[0]
        for i in range(len(val)):
            respuesta.append(0)
            tiporesult.append(0)
       
        for case in listacase:
            if len(case) == 2:
                # es un else
                for i in range(len(respuesta)):
                    if respuesta[i]==0:
                        respuesta[i] = case[0][0]
                        tiporesult[i] = case[1][0]
            else:
                # es un when    listacase.append([exp1,exp2,tipoE1,tipoE2])
                for i in range(len(respuesta)):
                    if case[0][i] == 1 and case[2][i]==TIPO_DATO.BIT:
                        respuesta[i] = case[1][0]
                        tiporesult[i] = case[3][0]
                    elif case[0][i] == 0 and case[2][i]==TIPO_DATO.BIT:
                        pass
                    else:
                        print("Error: No se puede realizar la operacion case")
                        return {"respuesta":"No se puede realizar la operacion case","tipo":"ERROR"}
                
                    
    else:
        print("Error: No se ha ingresado una lista de casos")
        return {"respuesta":"No se ha ingresado una lista de casos","tipo":"ERROR"}
    
    print ("respuesta: ",respuesta," tipo: ",tiporesult)
    return {"respuesta":respuesta,"tipo":tiporesult}