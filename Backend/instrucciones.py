class Instruccion:
    '''This is an abstract class'''

class Inst_If(Instruccion) : 

    def __init__(self, expLogica, instrucciones = []) :
        self.expLogica = expLogica
        self.instrucciones = instrucciones

class Select(Instruccion) :

    def __init__(self, campos, tablas, where = None) :
        self.campos = campos
        self.tablas = tablas
        self.where = where
        



from enum import Enum

class OPERACION_ARITMETICA(Enum) :
    MAS = 1
    MENOS = 2
    POR = 3
    DIVIDIDO = 4

class OPERACION_LOGICA(Enum) :
    MAYOR_QUE = 1
    MENOR_QUE = 2
    IGUAL = 3
    DIFERENTE = 4



class ExpresionNumerica:
    '''
        Esta clase representa una expresión numérica
    '''
    
class ExpresionBinaria(ExpresionNumerica) :
    
    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

class ExpresionNegativo(ExpresionNumerica) :
 
    def __init__(self, exp) :
        self.exp = exp

class ExpresionNumero(ExpresionNumerica) :
   
    def __init__(self, val = 0) :
        self.val = val

class ExpresionIdentificador(ExpresionNumerica) :

    def __init__(self, id = "") :
        self.id = id




class ExpresionCadena :
    '''
        Esta clase representa una Expresion de tipo cadena.
    '''

class ExpresionConcatenar(ExpresionCadena) :
   

    def __init__(self, exp1, exp2) :
        self.exp1 = exp1
        self.exp2 = exp2

class ExpresionDobleComilla(ExpresionCadena) :


    def __init__(self, val) :
        self.val = val

class ExpresionCadenaNumerico(ExpresionCadena) :
  
    def __init__(self, exp) :
        self.exp = exp




class ExpresionLogica() :
  
    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador