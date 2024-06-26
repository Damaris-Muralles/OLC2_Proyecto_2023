from datetime import datetime
from Analizadores.instrucciones import *
from BaseDatos.manejoxml import *
from Expresiones.Relacionales import *
from Expresiones.ELogicas import *
from Expresiones.OpBasicas import *
from Expresiones.Ifs import *
from Expresiones.FuncionesNativas import *
from Expresiones.ExpCase import *
from ValidacionVariasTablas import *
from Instrucciones.Funciones.Llamar import *
from Reportes.salidaconsola import *

xml = XMLManejador("./BaseDatos/BasesDatos.xml") 
comprobador=ComprobarTabla()

basedata = ""
table = ""
listatipodatos = []
imprim=SalidaConsola()
def procesar_where1(instr,base,tabla, entorno,lsimbolo,imprimir):
    global basedata
    basedata = base
    global table
    table = tabla
    global listatipodatos
    global imprim
    imprim=imprimir

    if isinstance(instr, dict):
        if instr.get("tipo") == TIPO_OPERACION.MAYOR_QUE:
            # procesando expresiones
            exp1,exp2=procesar_expresiones(instr, base, tabla, entorno,lsimbolo,imprimir)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            # imprimiendo expresiones
            print("")
            print(exp1," > ",exp2)

            # obteniendo valores y tipos
            exp1,exp2,tipoE1,tipoE2=procesar_datos(exp1, exp2, entorno)
            print("exp1: ",exp1," exp2: ",exp2)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            # realizar operacion mayor que
            resultado = mayor_que(exp1,exp2,tipoE1,tipoE2)
            listatipodatos.append(resultado.get("tipo"))
            if listatipodatos and listatipodatos[-1] == "ERROR":
                imprim.agregar("ERROR:""Operacion: Mayor que "+f"\n{resultado.get('respuesta')}\n")
                return "ERROR"
            return resultado.get("respuesta")
        elif instr.get("tipo") == TIPO_OPERACION.MENOR_QUE:
            # procesando expresiones
            exp1,exp2=procesar_expresiones(instr, base, tabla, entorno,lsimbolo,imprimir)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            # imprimiendo expresiones
            print("")
            print(exp1," < ",exp2)

            # obteniendo valores y tipos
            exp1,exp2,tipoE1,tipoE2=procesar_datos(exp1, exp2, entorno)
            print("exp1: ",exp1," exp2: ",exp2)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            # realizar operacion mayor que
            resultado = menor_que(exp1,exp2,tipoE1,tipoE2)
            listatipodatos.append(resultado.get("tipo"))
            if listatipodatos and listatipodatos[-1] == "ERROR":
                imprim.agregar("ERROR:""Operacion: Menor que "+f"\n{resultado.get('respuesta')}\n")
                return "ERROR"
            return resultado.get("respuesta")
        elif instr.get("tipo") == TIPO_OPERACION.IGUAL_IGUAL or instr.get("tipo") == TIPO_OPERACION.IGUAL:
            
            # procesando expresiones
            exp1,exp2=procesar_expresiones(instr, base, tabla, entorno,lsimbolo,imprimir)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            # imprimiendo expresiones
            print("")
            print(exp1," == ",exp2)

            # obteniendo valores y tipos
            exp1,exp2,tipoE1,tipoE2=procesar_datos(exp1, exp2, entorno)
            print("exp1: ",exp1," exp2: ",exp2)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            # realizar operacion mayor que
            resultado = igual_que(exp1,exp2,tipoE1,tipoE2)
            listatipodatos.append(resultado.get("tipo"))
            if listatipodatos and listatipodatos[-1] == "ERROR":
                imprim.agregar("ERROR:""Operacion: Igual que "+f"\n{resultado.get('respuesta')}\n")
                return "ERROR"
            return resultado.get("respuesta")
        elif instr.get("tipo") == TIPO_OPERACION.NO_IGUAL:
            # procesando expresiones
            exp1,exp2=procesar_expresiones(instr, base, tabla, entorno,lsimbolo,imprimir)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            # imprimiendo expresiones
            print("")
            print(exp1," != ",exp2)

            # obteniendo valores y tipos
            exp1,exp2,tipoE1,tipoE2=procesar_datos(exp1, exp2, entorno)
            print("exp1: ",exp1," exp2: ",exp2)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            # realizar operacion mayor que
            resultado = diferente_que(exp1,exp2,tipoE1,tipoE2)
            listatipodatos.append(resultado.get("tipo"))
            if listatipodatos and listatipodatos[-1] == "ERROR":
                imprim.agregar("ERROR:""Operacion: Diferente que "+f"\n{resultado.get('respuesta')}\n")
                return "ERROR"
            return resultado.get("respuesta")          
        elif instr.get("tipo") == TIPO_OPERACION.MAYOR_IGUAL:
            
            # procesando expresiones
            exp1,exp2=procesar_expresiones(instr, base, tabla, entorno,lsimbolo,imprimir)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            # imprimiendo expresiones
            print("")
            print(exp1," >= ",exp2)

            # obteniendo valores y tipos
            exp1,exp2,tipoE1,tipoE2=procesar_datos(exp1, exp2, entorno)
            print("exp1: ",exp1," exp2: ",exp2)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            # realizar operacion mayor que
            resultado = mayor_igual_que(exp1,exp2,tipoE1,tipoE2)
            listatipodatos.append(resultado.get("tipo"))
            if listatipodatos and listatipodatos[-1] == "ERROR":
                imprim.agregar("ERROR:""Operacion: Mayor igual que "+f"\n{resultado.get('respuesta')}\n")
                return "ERROR"
            return resultado.get("respuesta")
        elif instr.get("tipo") == TIPO_OPERACION.MENOR_IGUAL:
            # procesando expresiones
            exp1,exp2=procesar_expresiones(instr, base, tabla, entorno,lsimbolo,imprimir)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            # imprimiendo expresiones
            print("")
            print(exp1," <= ",exp2)

            # obteniendo valores y tipos
            exp1,exp2,tipoE1,tipoE2=procesar_datos(exp1, exp2, entorno)
            print("exp1: ",exp1," exp2: ",exp2)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            # realizar operacion mayor que
            resultado = menor_igual_que(exp1,exp2,tipoE1,tipoE2)
            listatipodatos.append(resultado.get("tipo"))
            if listatipodatos and listatipodatos[-1] == "ERROR":
                imprim.agregar("ERROR:""Operacion: Menor igual que "+f"\n{resultado.get('respuesta')}\n")
                return "ERROR"
            return resultado.get("respuesta")
        elif instr.get("tipo") == TIPO_OPERACION.AND:
            
            # procesando expresiones
            exp1,exp2=procesar_expresiones(instr, base, tabla, entorno,lsimbolo,imprimir)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            # imprimiendo expresiones
            print("")
            print(exp1," && ",exp2)

            # obteniendo valores y tipos
            exp1,exp2,tipoE1,tipoE2=procesar_datos(exp1, exp2, entorno)
            print("exp1: ",exp1," exp2: ",exp2)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            # realizar operacion mayor que
            resultado = and_logico(exp1,exp2)
            listatipodatos.append(resultado.get("tipo"))
            if listatipodatos and listatipodatos[-1] == "ERROR":
                imprim.agregar("ERROR:""Operacion: And logico "+f"\n{resultado.get('respuesta')}\n")
                return "ERROR"
            return resultado.get("respuesta")
        elif instr.get("tipo") == TIPO_OPERACION.OR:
          
            # procesando expresiones
            exp1,exp2=procesar_expresiones(instr, base, tabla, entorno,lsimbolo,imprimir)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            # imprimiendo expresiones
            print("")
            print(exp1," || ",exp2)

            # obteniendo valores y tipos
            exp1,exp2,tipoE1,tipoE2=procesar_datos(exp1, exp2, entorno)
            print("exp1: ",exp1," exp2: ",exp2)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            # realizar operacion mayor que
            resultado = or_logico(exp1,exp2)
            listatipodatos.append(resultado.get("tipo"))
            if listatipodatos and listatipodatos[-1] == "ERROR":
                imprim.agregar("ERROR:""Operacion: Or logico "+f"\n{resultado.get('respuesta')}\n")
                return "ERROR"
            return resultado.get("respuesta")            
        elif instr.get("tipo") == TIPO_OPERACION.NOT:
            
            exp1=procesar_where1(instr.get("exp1"), base, tabla, entorno,lsimbolo,imprimir)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()

            print("")
            print("!", exp1)

            exp1 = Obtener_valor(exp1, entorno)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            tipoE1=listatipodatos.pop()
            if isinstance(exp1, dict):
                tipE1 = exp1.get("tipo")
                exp1 = exp1.get("dato")

            print("exp1: ",exp1)
            # realizar operacion mayor que
            resultado = not_logico(exp1)
            listatipodatos.append(resultado.get("tipo"))
            if listatipodatos and listatipodatos[-1] == "ERROR":
                imprim.agregar("ERROR:""Operacion: Not logico "+f"\n{resultado.get('respuesta')}\n")
                return "ERROR"
            return resultado.get("respuesta")
        elif instr.get("tipo") == TIPO_OPERACION.BETWEEN:
            
            exp1=procesar_where1(instr.get("exp1"), base, tabla, entorno,lsimbolo,imprimir)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            exp2=procesar_where1(instr.get("exp2").get("exp1"), base, tabla, entorno,lsimbolo,imprimir)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            exp3=procesar_where1(instr.get("exp2").get("exp2"), base, tabla, entorno,lsimbolo,imprimir)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()

            print("")
            print(exp1, "esta entre", exp2 , " y ", exp3)

            exp1 = Obtener_valor(exp1, entorno)
            exp2 = Obtener_valor(exp2, entorno)
            exp3 = Obtener_valor(exp3, entorno)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            tipoE3=listatipodatos.pop()
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            tipoE2=listatipodatos.pop()
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            tipoE1=listatipodatos.pop()

            if isinstance(exp1, dict):
                tipoE1 = exp1.get("tipo")
                exp1 = exp1.get("dato")
            if isinstance(exp2, dict):
                tipoE2 = exp2.get("tipo")
                exp2 = exp2.get("dato")
            if isinstance(exp3, dict):
                tipoE3 = exp3.get("tipo")
                exp3 = exp3.get("dato")

            print("exp1: ",exp1," exp2: ",exp2," exp3: ",exp3)
            
            # realizar operacion 
            resultado = procesar_beetwen(exp1,exp2,exp3,tipoE1,tipoE2,tipoE3)
            listatipodatos.append(resultado.get("tipo"))
            if listatipodatos and listatipodatos[-1] == "ERROR":
                imprim.agregar("ERROR:""Operacion: Between "+f"\n{resultado.get('respuesta')}\n")
                return "ERROR"
            return resultado.get("respuesta")
        elif instr.get("tipo") == TIPO_OPERACION.SUMA:
           
            # procesando expresiones
            exp1,exp2=procesar_expresiones(instr, base, tabla, entorno,lsimbolo,imprimir)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            # imprimiendo expresiones
            print("")
            print(exp1," + ",exp2)

            # obteniendo valores y tipos
            exp1,exp2,tipoE1,tipoE2=procesar_datos(exp1, exp2, entorno)
            print("exp1: ",exp1," exp2: ",exp2)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            # realizar operacion mayor que
            resultado = suma_op(exp1,exp2,tipoE1,tipoE2)
            
            listatipodatos.append(resultado.get("tipo"))
            if listatipodatos and listatipodatos[-1] == "ERROR":
                imprim.agregar("ERROR:""Operacion: Suma "+f"\n{resultado.get('respuesta')}\n")
                return "ERROR"
            return resultado.get("respuesta") 
        elif instr.get("tipo") == TIPO_OPERACION.RESTA:
            
            # procesando expresiones
            exp1,exp2=procesar_expresiones(instr, base, tabla, entorno,lsimbolo,imprimir)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            # imprimiendo expresiones
            print("")
            print(exp1," - ",exp2)

            # obteniendo valores y tipos
            exp1,exp2,tipoE1,tipoE2=procesar_datos(exp1, exp2, entorno)
            print("exp1: ",exp1," exp2: ",exp2)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            # realizar operacion mayor que
            resultado = resta_op(exp1,exp2,tipoE1,tipoE2)
            listatipodatos.append(resultado.get("tipo"))
            if listatipodatos and listatipodatos[-1] == "ERROR":
                imprim.agregar("ERROR:""Operacion: Resta "+f"\n{resultado.get('respuesta')}\n")
                return "ERROR"
            return resultado.get("respuesta") 
        elif instr.get("tipo") == TIPO_OPERACION.MULTIPLICACION:
            
            # procesando expresiones
            exp1,exp2=procesar_expresiones(instr, base, tabla, entorno,lsimbolo,imprimir)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            # imprimiendo expresiones
            print("")
            print(exp1," * ",exp2)

            # obteniendo valores y tipos
            exp1,exp2,tipoE1,tipoE2=procesar_datos(exp1, exp2, entorno)
            print("exp1: ",exp1," exp2: ",exp2)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            # realizar operacion mayor que
            resultado = multiplicacion_op(exp1,exp2,tipoE1,tipoE2)
            listatipodatos.append(resultado.get("tipo"))
            if listatipodatos and listatipodatos[-1] == "ERROR":
                imprim.agregar("ERROR:""Operacion: Multiplicacion "+f"\n{resultado.get('respuesta')}\n")
                return "ERROR"
            return resultado.get("respuesta") 
        elif instr.get("tipo") == TIPO_OPERACION.DIVISION:
        
            # procesando expresiones
            exp1,exp2=procesar_expresiones(instr, base, tabla, entorno,lsimbolo,imprimir)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            # imprimiendo expresiones
            print("")
            print(exp1," / ",exp2)

            # obteniendo valores y tipos
            exp1,exp2,tipoE1,tipoE2=procesar_datos(exp1, exp2, entorno)
            print("exp1: ",exp1," exp2: ",exp2)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            # realizar operacion mayor que
            resultado =division_op(exp1,exp2,tipoE1,tipoE2)
            listatipodatos.append(resultado.get("tipo"))
            if listatipodatos and listatipodatos[-1] == "ERROR": 
                imprim.agregar("ERROR:""Operacion: Division "+f"\n{resultado.get('respuesta')}\n")
                return "ERROR"
            return resultado.get("respuesta") 
        elif instr.get("tipo")==TIPO_INSTRUCCION.HOY:
            resultado = funcion_hoy()
            listatipodatos.append(resultado.get("tipo"))
            return resultado.get("respuesta")
        elif instr.get("tipo")==TIPO_INSTRUCCION.CONTATENACION:
            
            # procesando expresiones
            exp1=procesar_where1(instr.get("cadena1"), base, tabla, entorno,lsimbolo,imprimir)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            exp2=procesar_where1(instr.get("cadena2"), base, tabla, entorno,lsimbolo,imprimir)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            # imprimiendo expresiones
            print("")
            print(exp1," concatenado ",exp2)

            # obteniendo valores y tipos
            exp1,exp2,tipoE1,tipoE2=procesar_datos(exp1, exp2, entorno)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            print("exp1: ",exp1," exp2: ",exp2)

            # realizar operacion mayor que
            resultado = funcion_concatena(exp1,exp2,tipoE1,tipoE2)
            listatipodatos.append(resultado.get("tipo"))
            if listatipodatos and listatipodatos[-1] == "ERROR": 
                imprim.agregar("ERROR:""Operacion: Concatenacion "+f"\n{resultado.get('respuesta')}\n")
                return "ERROR"
            return resultado.get("respuesta")       
        elif instr.get("tipo")==TIPO_INSTRUCCION.SUBSTRER:
            
            exp1=procesar_where1(instr.get("cadena"), base, tabla, entorno,lsimbolo,imprimir)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            exp2=procesar_where1(instr.get("inicio"), base, tabla, entorno,lsimbolo,imprimir)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            exp3=procesar_where1(instr.get("fin"), base, tabla, entorno,lsimbolo,imprimir)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()

            print("")
            print(exp1, " substraer ", exp2,exp3)
            exp1 = Obtener_valor(exp1, entorno)
            exp2 = Obtener_valor(exp2, entorno)
            exp3 = Obtener_valor(exp3, entorno)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            tipoE3 = listatipodatos.pop()
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            tipoE2 = listatipodatos.pop()
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            tipoE1 = listatipodatos.pop()


            if isinstance(exp1, dict):
                tipoE1 = exp1.get("tipo")
                exp1 = exp1.get("dato")
            if isinstance(exp2, dict):
                tipoE2 = exp2.get("tipo")
                exp2 = exp2.get("dato")
            if isinstance(exp3, dict):
                tipoE3 = exp3.get("tipo")
                exp3 = exp3.get("dato")
            print("exp1: ",exp1," exp2: ",exp2," exp3: ",exp3)
            # realizar operacion mayor que
            resultado = funcion_substraer(exp1,exp2,exp3,tipoE1,tipoE2,tipoE3)
            listatipodatos.append(resultado.get("tipo"))
            if listatipodatos and listatipodatos[-1] == "ERROR": 
                imprim.agregar("ERROR:""Operacion: Substraer "+f"\n{resultado.get('respuesta')}\n")
                return "ERROR"
            return resultado.get("respuesta")
        elif instr.get("tipo")==TIPO_INSTRUCCION.CAST:
            
            exp1=procesar_where1(instr.get("columna"), base, tabla, entorno,lsimbolo,imprimir)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            castear_a=instr.get("tipodato").get("tipo")
            longitud=instr.get("tipodato").get("longitud")
            print("")
            print(exp1, " castear a ",castear_a )
            exp1 = Obtener_valor(exp1, entorno)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            tipoE1 = listatipodatos.pop()


            if isinstance(exp1, dict):
                tipoE1 = exp1.get("tipo")
                exp1 = exp1.get("dato")
                
            print("exp1: ",exp1)
            # realizar operacion mayor que
            resultado = funcion_cast(exp1,tipoE1,castear_a,longitud)
            listatipodatos.append(resultado.get("tipo"))
            if listatipodatos and listatipodatos[-1] == "ERROR": 
                imprim.agregar("ERROR:""Operacion: Cast "+f"\n{resultado.get('respuesta')}\n")
                return "ERROR"
            return resultado.get("respuesta")
        elif instr.get("tipo")==TIPO_INSTRUCCION.IF:
            
            exp1=procesar_where1(instr.get("condicion"), base, tabla, entorno,lsimbolo,imprimir)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            exp2=procesar_where1(instr.get("verdadero"), base, tabla, entorno,lsimbolo,imprimir)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            exp3=procesar_where1(instr.get("falso"), base, tabla, entorno,lsimbolo,imprimir)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                return ["ERROR"]
            if listatipodatos and listatipodatos[-1] == "noinstr":
                listatipodatos.pop()
            
            print("")
            print("if ",exp1)
            exp1 = Obtener_valor(exp1, entorno)
            exp2 = Obtener_valor(exp2, entorno)
            exp3 = Obtener_valor(exp3, entorno)
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            tipoE3 = listatipodatos.pop()
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            tipoE2 = listatipodatos.pop()
            if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
            tipoE1 = listatipodatos.pop()

            if isinstance(exp1, dict):
                tipoE1 = exp1.get("tipo")
                exp1 = exp1.get("dato")
               
            if isinstance(exp2, dict):
                tipoE2 = exp2.get("tipo")
                exp2 = exp2.get("dato")
               
            if isinstance(exp3, dict):
                tipoE3 = exp3.get("tipo")
                exp3 = exp3.get("dato")
                
            print("exp1: ",exp1," V: ",exp2," F: ",exp3)
            # realizar operacion mayor que
            resultado = if_simple(exp1,exp2,exp3,tipoE1,tipoE2,tipoE3)
            listatipodatos.append(resultado.get("tipo"))
            return resultado.get("respuesta")
        elif instr.get("tipo")==TIPO_INSTRUCCION.CASE:
            print("")
            print("case ")
            listacase=[]
            for sentencia in instr.get("sentencias"):
                
                if sentencia.get("tipodato")==TIPO_INSTRUCCION.WHEN:
                    exp1=procesar_where1(sentencia.get("condicion"), base, tabla, entorno,lsimbolo,imprimir)
                    if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
                    if listatipodatos and listatipodatos[-1] == "noinstr":
                        listatipodatos.pop()
                    exp2=procesar_where1(sentencia.get("resultado"), base, tabla, entorno,lsimbolo,imprimir)
                    if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
                    if listatipodatos and listatipodatos[-1] == "noinstr":
                        listatipodatos.pop()
                    print("")
                    print("when ",exp1," then ",exp2)
                    exp1 = Obtener_valor(exp1, entorno)
                    exp2 = Obtener_valor(exp2, entorno)
                    if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
                    tipoE2 = listatipodatos.pop()
                    if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
                    tipoE1 = listatipodatos.pop()
                    if isinstance(exp1, dict):
                        tipoE1 = exp1.get("tipo")
                        exp1 = exp1.get("dato")
                    if isinstance(exp2, dict):
                        tipoE2 = exp2.get("tipo")
                        exp2 = exp2.get("dato")
                    print("exp1: ",exp1," exp2: ",exp2)
                    listacase.append([exp1,exp2,tipoE1,tipoE2])
                elif sentencia.get("tipodato")==TIPO_INSTRUCCION.ELSE:
                    exp1=procesar_where1(sentencia.get("resultado"), base, tabla, entorno,lsimbolo,imprimir)
                    if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
                    if listatipodatos and listatipodatos[-1] == "noinstr":
                        listatipodatos.pop()
                    print("")
                    print("else ",exp1)
                    exp1 = Obtener_valor(exp1, entorno)
                    if listatipodatos and listatipodatos[-1] == "ERROR":
                        return ["ERROR"]
                    tipoE1 = listatipodatos.pop()

                    if isinstance(exp1, dict):
                        tipoE1 = exp1.get("tipo")
                        exp1 = exp1.get("dato")
                    print("exp1: ",exp1)
                    listacase.append([exp1,tipoE1])

            # realizar funcion case
            resultado = funcion_case(listacase)
            listatipodatos.append(resultado.get("tipo"))
            if listatipodatos and listatipodatos[-1] == "ERROR": 
                imprim.agregar("ERROR:""Operacion: Case "+f"\n{resultado.get('respuesta')}\n")
                return "ERROR"
            return resultado.get("respuesta")                  
        
        

        else:
            print("Error: instruccion no valida")
            listatipodatos.append("ERROR")
            return ["ERROR"]
    else:
        listatipodatos.append("noinstr")
        return instr

def procesar_expresiones(instr, base, tabla, entorno,lsimbolo,imprimir):
    global listatipodatos
    # procesando expresion derecha y validando que no sea error
    exp1=procesar_where1(instr.get("exp1"), base, tabla, entorno,lsimbolo,imprimir)
    if listatipodatos and listatipodatos[-1] == "ERROR":
        return ["ERROR"],""
    if listatipodatos and listatipodatos[-1] == "noinstr":
        listatipodatos.pop()

    # procesando expresion izquierda y validando que no sea error
    exp2=procesar_where1(instr.get("exp2"), base, tabla, entorno,lsimbolo,imprimir)
    if listatipodatos and listatipodatos[-1] == "ERROR":
        return ["ERROR"],""
    if listatipodatos and listatipodatos[-1] == "noinstr":
        listatipodatos.pop()

    return exp1, exp2

def procesar_datos(exp1, exp2, entorno):
    exp1 = Obtener_valor(exp1, entorno)
    exp2 = Obtener_valor(exp2, entorno)

    if listatipodatos and listatipodatos[-1] == "ERROR":
        return ["ERROR"],"", "", "" 
    tipo2=listatipodatos.pop()

    if listatipodatos and listatipodatos[-1] == "ERROR":
        return ["ERROR"],"", "", ""
    tipo1=listatipodatos.pop()
    
    if isinstance(exp1, dict):
        tipo1 = exp1.get("tipo")
        
        exp1 = exp1.get("dato")
    if isinstance(exp2, dict):
        tipo2 = exp2.get("tipo")
        exp2 = exp2.get("dato")

    return exp1, exp2, tipo1, tipo2

def Obtener_valor(cadena, entorno):
    # si expresion contine comillas dobles o simples escribir algo

    if isinstance(cadena, str):
        
        if cadena.startswith('@'):
            variable=obtener_variable(cadena, entorno)
            listatipodatos.append(variable.get("tipo"))
            #print("variable tip: ", variable.get("tipo"))
            if variable.get("tipo")[0]==TIPO_DATO.VARCHAR or variable.get("tipo")[0]==TIPO_DATO.CHAR:
                variable.get("dato")[0] = (variable.get("dato")[0])[1:-1]
           
            return variable
        elif not cadena.startswith('\"') and not cadena.startswith('\''):
            # se tiene que buscar en la tabla la columna correspondiente
            # ver si tiene un punto, si es asi dividirlo
            
            
            colum=obtener_id(basedata,table,cadena)
            print("colum: ",colum)
            listatipodatos.append(colum.get("tipo"))
            return colum    
        else:
            # quitar las comillas
            if cadena.startswith('\"') and cadena.endswith('\"'):
                cadena = cadena[1:-1]
            tip=TIPO_DATO.VARCHAR
            try:
                # Intenta convertir la cadena en una fecha
                datetime.strptime(cadena, '%d-%m-%Y')
                tip=TIPO_DATO.DATE
            except ValueError:
                pass

            try:
                # Intenta convertir la cadena en una fecha con hora
                datetime.strptime(cadena, '%d-%m-%Y %H:%M:%S')
                tip=TIPO_DATO.DATETIME
            except ValueError:
                pass
            
            listatipodatos.append([tip])
            return [cadena]
    else:
        tip=""
        if isinstance(cadena, list):
            return cadena
        else:
            if isinstance(cadena, int):
                tip = TIPO_DATO.INT
            else:
                tip=TIPO_DATO.DECIMAL
            listatipodatos.append([tip])
            return [cadena]

def obtener_variable(variable,entorno):

    valor = entorno.getSimbolo(variable)
    print("valor: ",valor)
    #ver que valor.valor sea una lista
    if isinstance(valor.valor, list) and isinstance(valor.tipo.get("tipo"), list):
        return {"dato": valor.valor, "tipo": valor.tipo.get("tipo")}
    elif isinstance(valor.valor, list):
        return {"dato": valor.valor, "tipo": [valor.tipo.get("tipo")]}
    elif isinstance(valor.tipo.get("tipo"), list):
        return {"dato": [valor.valor], "tipo": valor.tipo.get("tipo")}
    else:
        return {"dato": [valor.valor], "tipo": [valor.tipo.get("tipo")]}


def obtener_id(data,tabla,cadena):
        
        igualcolum=0
        tabref=""
        comp1=0
        print("cadena: ",cadena)
        print("tabla: ",tabla)
        print("data: ",data)
        igualcolum,tabref,comp1=comprobador.comprobar(cadena,xml,data,imprim)
        
        if igualcolum==-1:
                print("ERROR: al buscar columna ",cadena," en las tablas")
                return {"dato": ["ERROR"], "tipo": "ERROR"}
        
        if comp1==1:
            tabla=cadena.split(".")[0]
            cadena=cadena.split(".")[1]
        elif comp1==0:
            if igualcolum==1:
                tabla=tabref
            elif igualcolum>1:
                print("Error: la columna ",cadena," existe en mas de una de las tablas especificadas")
                imprim.agregar("ERROR:"+f"\nError: la columna {cadena} existe en mas de una de las tablas especificadas")
                return {"dato": ["ERROR"], "tipo": "ERROR"}
            else:
                print("Error: la columna ",cadena," no existe en las tablas")
                imprim.agregar("ERROR:"+f"\nError: la columna {cadena} no existe en las tablas")
                return {"dato": ["ERROR"], "tipo": "ERROR"}

              
       
        colum=xml.obtener_registros(data,tabla,cadena)
        if colum.get('tipo')=="ERROR":
            imprim.agregar("ERROR:"+f"\n{colum.get('dato')}")
            return {"dato": ["ERROR"], "tipo": "ERROR"}
        return colum