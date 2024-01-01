from Expresiones.Where import *
from Entornos.Entorno import *

def CicloW(instrucciones, entorno, lsimbolos, xml, basedatos):
    print("instruccion: ", instrucciones)
    comprobador.ciclo=True
    condicion = procesar_where1(instrucciones.get('condicion'),basedatos,"",entorno,lsimbolos)
    respuesta = None
    print("entra: ", condicion)

    while condicion[0] == 1:
        from Separar.Locales import Local
        entornoL = Entorno(entorno, None)
        entornoL.setRetorno(entorno.retorno)
        respuesta = Local(instrucciones.get('instrucciones'), entornoL, xml, basedatos, lsimbolos)

        condicion = procesar_where1(instrucciones.get('condicion'),basedatos,"",entorno,lsimbolos)
        print("salida: ", condicion)

    return respuesta
    