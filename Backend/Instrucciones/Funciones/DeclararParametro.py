
from Expresiones.Where import *
from Entornos.Simbolo import *
def DeclararP(instruccion, entorno, simbolo, entornoN, xml, basedatos):
    print("decparam: ", instruccion)

    valor = procesar_where1(instruccion.get('valor'),"","",entorno,simbolo)
    print("resultado: ", valor)
    nuevo = Simbolo(instruccion.get('id'),valor, instruccion.get('tipodato'))

    entorno.addSimbolo(nuevo.id, nuevo)
    simbolo.add(instruccion.get('id'), valor, instruccion.get('tipodato'), entornoN)

    return None
