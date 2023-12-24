from Expresiones.Where import *
def asignarVariable(instruccion, entorno, simbolo):
    #print("instruccion: ", instruccion)

    resultado = procesar_where1(instruccion.get('valor'),"", "", entorno)
   
    resultado = resultado
    


    temp = entorno.getSimboloE(instruccion.get('id'))
    variable = temp.get('resultado')
    variable.valor = resultado
    entorno.actualizar(instruccion.get('id'), variable)
    simbolo.update(instruccion.get('id'), temp.get('entorno'), resultado)