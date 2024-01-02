# classe que guarde una cadena de texto para mostrarla en la consola

class SalidaConsola:
    def __init__(self):
        self.salida = ""

    def agregar(self, texto):
        if self.salida == "":
            self.salida += texto
        else:
            self.salida += "\n\n\n"+texto  

    def agregarTabla(self, tabla,fil,col):
        valorcolum = []
        rows=[]
        cadena = ""
        for colum in tabla:
            longitud = len(str(colum[0]))
            rows.append(len(colum[1]))
            for row in colum[1]:
                if longitud < len(str(row)):
                    longitud = len(str(row))
            valorcolum.append(longitud)

   
        # revisar que todos los elementos en rows sean iguales o que los que no sean iguales sean valor  1
        mayor=0
        for i in range(0,len(rows)):
            if rows[i]>mayor:
                mayor=rows[i]
            if rows[i]!=1:
                for j in range(0,len(rows)):
                    if rows[i]!=rows[j] and rows[j]!=1:
                        self.agregar("ERROR:\nConsulta: Select Fila: "+str(fil)+" Columna: "+str(col)+"\nNo se puede imprimir la tabla")
        

        
        num=len(tabla)
        for i in range(0,num):
            cadena+="|"+str(tabla[i][0]).center(valorcolum[i]).upper()
            if i==num-1:
                cadena+="| \n"

        seguir=True
        cont=0

        while seguir:
            
            for i in range(0,num):
                if cont>rows[i]:
                    cadena+="|"+str(tabla[i][1][0]).ljust(valorcolum[i])
                else:
                    cadena+="|"+str(tabla[i][1][cont]).ljust(valorcolum[i])
                if i==num-1:
                    cadena+="| \n"
                if cont==mayor-1:
                    seguir=False
            cont+=1
        self.agregar(cadena)
            

    def getSalida(self):
        return self.salida