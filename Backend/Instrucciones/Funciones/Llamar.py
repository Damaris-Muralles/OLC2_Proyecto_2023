from Entornos.Entorno import *

from Analizadores.instrucciones import *
from Instrucciones.Funciones.DeclararParametro import *
def Llama (instruccion, entorno, lsimbolos, xml, basedatos):
    print("llamr: ", instruccion)
    salida = ""
    buscar = entorno.getMetodo(instruccion.get('id'))
 

    if buscar != None :
        from Separar.Locales import Local
        entornoL = Entorno(entorno, instruccion.get('id'))
        
        entornoL.setRetorno(buscar.retorna)
        Salidareturn = False
        if buscar.retorna == None :
            Salidareturn = True
        else :
            for instr in buscar.instrucciones :
                if instr.get('tipo') == TIPO_INSTRUCCION.RETORNAR : Salidareturn = True

        if Salidareturn == True :
            if instruccion.get('parametros') != None :
                if (instruccion.get('parametros')) and (len(instruccion.get('parametros')) == len(buscar.parametros)) :
                    print("parametrosid: ", buscar.parametros )

                    for i in range(len(instruccion.get('parametros'))) :
                        declarar = Parametro(buscar.parametros[i].get('id'), buscar.parametros[i].get('tipodato'), instruccion.get('parametros')[i])
                        error = DeclararP(declarar, entornoL, lsimbolos, entornoL.nombre, xml, basedatos)

                    respuesta  = Local(buscar.instrucciones, entornoL, xml, basedatos, lsimbolos)
            else:
                respuesta  = Local(buscar.instrucciones, entornoL, xml, basedatos, lsimbolos)    


                      
                    

        print("soyres:",respuesta)
        

    return None