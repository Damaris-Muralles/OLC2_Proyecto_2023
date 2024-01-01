from Expresiones.Where import *
from Entornos.Entorno import *

def Caso(instruccion, entorno, simbolos, xml, BaseDatos):
    print("caso: ", instruccion)

    for caso in instruccion.get('sentencias'):

        if caso.get('condicion') != None:
            condicion = procesar_where1(caso.get('condicion'),BaseDatos,"",entorno,simbolos)

            if condicion[0] == 1:
                from Separar.Locales import Local
                entornoL = Entorno(entorno, None)
                entornoL.setRetorno(entorno.retorno)
                respuesta = Local(caso.get('resultado'), entornoL, xml, BaseDatos, simbolos)
                return respuesta
        else:
            from Separar.Locales import Local
            entornoL = Entorno(entorno, None)
            entornoL.setRetorno(entorno.retorno)
            respuesta = Local(caso.get('resultado'), entornoL, xml, BaseDatos, simbolos)
            return respuesta

