from Expresiones.Where import *
def RetornarI(instruccion, entorno, simbolo, xml, BaseDatos):
    print("instruccion: ", instruccion)
    if instruccion.get('valor') != None :

        if not isinstance(instruccion.get('valor'), dict):
            if instruccion.get('valor').startswith('@'):
                variable = obtener_variable(instruccion.get('valor'),entorno)
                if variable.get("tipo")[0]==TIPO_DATO.VARCHAR or variable.get("tipo")[0]==TIPO_DATO.CHAR:
                    variable.get("dato")[0] = (variable.get("dato")[0])[1:-1]
                retorna = variable.get("dato")
                return retorna
            else:
                retorna = procesar_where1(instruccion.get('valor'),BaseDatos,"",entorno)
                return retorna
        else:
            retorna = procesar_where1(instruccion.get('valor'),BaseDatos,"",entorno)
            return retorna
    else :
        retorna = None