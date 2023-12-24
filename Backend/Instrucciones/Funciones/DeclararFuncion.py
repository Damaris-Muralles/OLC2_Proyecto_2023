from Entornos.Metodo import *

def DeclararFuncion(instruccion, entorno, metodo):
    #print("instruccione: ", instruccion)
    #print("funpara: ", instruccion.get('parametros'))
    nuevo = Metodo(instruccion.get('id'), instruccion.get('parametros'), instruccion.get('instrucciones'), instruccion.get('retornar'))
    #print("nuevo: ", nuevo.id)
    entorno.addMetodo(nuevo.id, nuevo)
    metodo.add(instruccion.get('id'), instruccion.get('retornar'))

    return None