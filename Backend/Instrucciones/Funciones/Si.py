from Expresiones.Where import *
from Entornos.Entorno import *


def Si(instrucciones, entorno, lsimbolos, xml, basedatos,imprimir):
    print("instruccion: ", instrucciones)

    
    condicion = procesar_where1(instrucciones.get('condicion'),basedatos,"",entorno,lsimbolos,imprimir)

    #print("condicion: ", condicion)

    if condicion[0] == 1:
        from Separar.Locales import Local
        entornoL = Entorno(entorno, None)
        entornoL.setRetorno(entorno.retorno)
        respuesta = Local(instrucciones.get('verdadero'), entornoL, xml, basedatos, lsimbolos,imprimir)
        return respuesta
    else:
        if instrucciones.get('falso') != None:
            from Separar.Locales import Local
            entornoL = Entorno(entorno, None)
            entornoL.setRetorno(entorno.retorno)
            respuesta = Local(instrucciones.get('falso'), entornoL, xml, basedatos, lsimbolos,imprimir)
            return respuesta
        else:
           return None


