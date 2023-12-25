import Analizadores.gramar as g
from Analizadores.instrucciones import *
from BaseDatos.manejoxml import *
from Entornos.Entorno import *
from Entornos.ListaMetodo import *
from Entornos.ListaSimbolos import *

from Separar.Globales import *

xml = XMLManejador("./BaseDatos/BasesDatos.xml")  
lsimbolo = ListaSimbolo()
lmetodo = ListaMetodo()

def procesar_instrucciones(instrucciones) :
    ## lista de instrucciones recolectadas
    entornoG = Entorno(None, "global")
    Globales(instrucciones, entornoG, xml, lsimbolo, lmetodo)

    
    
    

#f = open("./entrada.txt", "r")

#input = f.read()
# otras pruebas de entrada


input = """


USE intento;
update Tabla1 set nombre == "hola" where ide == 3;
        


"""

instrucciones = g.parse(input.lower())
if instrucciones!=None:

    procesar_instrucciones(instrucciones)



