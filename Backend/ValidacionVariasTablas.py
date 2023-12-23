
class ComprobarTabla():
    def __init__(self):
        self.tabla = []
    def agregar(self, tabla):
        self.tabla.extend(tabla)
    def comprobar(self,columevaluar,xml,ActualBaseDatos):
        if self.tabla==None:
            print("Error: no se ha especificado una tabla")
            return -1,False,False
        igualcolum=0
        tabref=""
        columnascomprobadas=0
        print("+++++++++++++++++++++++++++")
        print("columna a buscar :",columevaluar)
        for tab in self.tabla:
            if ("." in columevaluar)!=True:
                
                com=xml.buscar_columna(ActualBaseDatos,tab,columevaluar)
                if com=="ERROR":
                    print("1")
                    print("+++++++++++++++++++++++++++")
                    return -1,False,False
                # buscar en el xml si existe la columna para la tabla actual
                if com==True:
                    igualcolum=igualcolum+1
                    tabref=tab
            else:
                
                #separar el nombre de la tabla y la columna
                tab1=columevaluar.split(".")[0]
                col1=columevaluar.split(".")[1]
                # recorrer self.tabla para ver si la tabla que se quiere buscar existe
                comt=(tab1 in self.tabla)
                if comt==False:
                    print("la tabla ",tab1," no se ha espeficiado en el from")
                    print("+++++++++++++++++++++++++++")
                    return -1,False,False
                if tab1==tab :
                    
                    com=xml.buscar_columna(ActualBaseDatos,tab1,col1)
                    if com=="ERROR":
                        print("3")
                        print("+++++++++++++++++++++++++++")
                        return -1,False,False
                    # buscar en el xml si existe la columna para la tabla actual
                    if com!=True:
                        print("Error: la columna ",col1," no existe en la tabla ",tab1)
                        print("+++++++++++++++++++++++++++")
                        return -1,False,False
                    columnascomprobadas+=1
                    
        print("tablas con la misma:",igualcolum,"ultima tabla que la contiene: ",tabref,"columnascomprobadas",columnascomprobadas)
        print("+++++++++++++++++++++++++++")
        return igualcolum,tabref,columnascomprobadas
            
                        
            