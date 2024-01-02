

from Entornos.Simbolo import *
from Expresiones.Where import *
from Analizadores.instrucciones import *

def DeclararVariables(instruccion, entorno, entornoNombre, simbolo,imprimir):
    #print("instruccion: ", instruccion)
    valor = None
    if instruccion.get('tipodato').get('tipo') == TIPO_DATO.INT  :
        valor = 0
    elif instruccion.get('tipodato').get('tipo') == TIPO_DATO.CHAR or instruccion.get('tipodato').get('tipo') == TIPO_DATO.VARCHAR :
        valor = "" 
    elif instruccion.get('tipodato').get('tipo') == TIPO_DATO.DECIMAL :
        valor = 0.0
    elif instruccion.get('tipodato').get('tipo') == TIPO_DATO.BIT :
        valor = 0
    elif instruccion.get('tipodato').get('tipo') == TIPO_DATO.DATE:
        valor = '00-00-0000'
    elif instruccion.get('tipodato').get('tipo') == TIPO_DATO.DATETIME:
        valor = '00-00-0000 00:00:00'

    if instruccion.get('valor') != None:
        resultado = procesar_where1(instruccion.get('valor'),"", "", entorno, simbolo,imprimir)
        #si resultado no es una lista
        print("comillas: ", resultado)
        valor = resultado
       

    nuevo = Simbolo(instruccion.get('id'),valor, instruccion.get('tipodato'))

    entorno.addSimbolo(nuevo.id, nuevo)
    simbolo.add(instruccion.get('id'), valor, instruccion.get('tipodato'), entornoNombre)
  
    return None