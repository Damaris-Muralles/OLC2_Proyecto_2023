from Entornos.Metodo import *

def DeclararMetodos(instruccion, entorno, metodo):
    #print("instruccione: ", instruccion)
    #print("funpara: ", instruccion.get('parametros'))
    nuevo = Metodo(instruccion.get('id'), instruccion.get('parametros'), instruccion.get('instrucciones'), None)
    #print("nuevo: ", nuevo.id)
    entorno.addMetodo(nuevo.id, nuevo)
    metodo.add(instruccion.get('id'), 'Void')

    return None