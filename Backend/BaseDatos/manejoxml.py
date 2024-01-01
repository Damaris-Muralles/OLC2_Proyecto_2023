import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from Analizadores.instrucciones import *
import re 

class XMLManejador:
    def __init__(self, filepath):
        self.filepath = filepath
        self.arbol = ET.parse(filepath)
        self.raiz = self.arbol.getroot()

    def prettify(self, elem):
        rough_string = ET.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return '\n'.join([line for line in reparsed.toprettyxml(indent="  ").split('\n') if line.strip()])

    def recorridoarbol(self):
        tree = ET.parse(self.filepath)
        root = tree.getroot()
        lista = []
       
        #recorrer el arbol de xml
        
        for elemento in root:
            # buscar la etiqueta basedatos
            talas=[]
            funciones=[]
            procedimientos=[]
            diccionario = {
            'name': 1,
            'tables': [],
            'procedures': [],
            'functions': []
            }
            if elemento.tag == "basedatos":
                # buscar la etiqueta nombre
                for subelemento in elemento:
                    if subelemento.tag == "nombre":
                       
                        diccionario['name'] = subelemento.text
                    if subelemento.tag == "tablas":
                        for tabla in subelemento:
                            talas.append(tabla.find('nombre').text)
                    # recorrer las funciones
                    if subelemento.tag == "funciones":
                        for funcion in subelemento:
                            funciones.append(funcion.find('nombre').text)
                    # recorrer los procedimientos
                    if subelemento.tag == "procedimientos":
                        for procedimiento in subelemento:
                            procedimientos.append(procedimiento.find('nombre').text)
                diccionario['tables'] = talas
                diccionario['procedures'] = procedimientos
                diccionario['functions'] = funciones
                lista.append(diccionario)        
        return lista                      

    def read_xml(self):
        tree = ET.parse(self.filepath)
        root = tree.getroot()
        return root

    def Existe_basedatos(self, database):
        root = self.read_xml()

        for element in root.findall('basedatos'):
            if element.find('nombre').text == database:
                return [True,root,element]

        return [False,root,None]
    
    def buscar_columna(self,database,tab,col):
        baseDatosEncontrada = self.Existe_basedatos(database)
        if not baseDatosEncontrada[0]:
            print("ERROR: No existe la base de datos")
            return "ERROR"
        root = baseDatosEncontrada[1]
        database_element = baseDatosEncontrada[2]
        tablas_element = database_element.find('tablas')
        if tablas_element is None:
            print("ERROR: No existe la tabla")
            return "ERROR"
        tablas_element = tablas_element.findall('tabla')
        existe = False
        tabla_element = None
        for tabla in tablas_element:
            if tabla.find('nombre').text == tab:
                existe = True
                tabla_element = tabla
                break
        if not existe:
            print("ERROR: No existe la tabla")
            return "ERROR"
        columnas_element = tabla_element.find('columnas')
        columnas_element = columnas_element.findall('columna')
        for columna in columnas_element:
            if columna.find('id').text == col:
                return True
        return False

    def obtener_registros(self, database, table,colum):
        
        baseDatosEncontrada = self.Existe_basedatos(database)
        if not baseDatosEncontrada[0]:
            return {"dato":"Base de datos no existe.","tipo":"ERROR"}
        root = baseDatosEncontrada[1]
        database_element = baseDatosEncontrada[2]
        #buscar si existe la tabla con el idtabla, si no existe retorna error
        tablass_element = database_element.find('tablas')
        if tablass_element is None:
            return {"dato":"No se pueden obtener los datos: no existe la tabla.","tipo":"ERROR"}
        tablas_element = tablass_element.findall('tabla')
        existe = False
        tabla_element = None
        for tabla in tablas_element:
            if tabla.find('nombre').text == table:
                existe = True
                tabla_element = tabla
                break
        if not existe:
            return {"dato":"No se pueden obtener los datos: no existe la tabla.","tipo":"ERROR"} 

        columnas_element = tabla_element.find('columnas')
        columna_element = columnas_element.findall('columna')
        
        # buscar que exista la columna colum
        if colum == "*todo*":
            # obtener una lista con los valores de la primera columna
            lista = []
            tipolist = []
            listaids = []
            
            for columna in columna_element:
                # buscar el tipo de dato de la columna
                listaids.append(columna.find('id').text)
                tipodato = columna.find('tipo').find('tipodato').text
                if tipodato != None:
                    tipodato = int(tipodato)
                
                # buscar todos los inputs de la columna y retornarlos como lista
                listacolumnas = []
                listtipo=[] 
                listainputs = columna.find('inputs')
                listainputs = listainputs.findall('input')
                if len(listainputs) == 0:
                    return {"dato":"No hay registros","tipo":"ERROR"}
                for input in listainputs:
                    listacolumnas.append(input.text)
                    listtipo.append(TIPO_DATO(tipodato))
                lista.append(listacolumnas)
                tipolist.append(listtipo)
            return {"dato":lista,"tipo":tipolist,"ids":listaids}
        for columna in columna_element:
            if columna.find('id').text == colum:
                # buscar el tipo de dato de la columna
                tipodato = columna.find('tipo').find('tipodato').text
                if tipodato != None:
                    tipodato = int(tipodato)
                

                # buscar todos los inputs de la columna y retornarlos como lista
                inputs_element = columna.find('inputs')
                inputs_element = inputs_element.findall('input')
                lista = []
                tipolist = []   
                if len(inputs_element) == 0:
                    return {"dato":"No hay registros","tipo":"ERROR"}
                for input in inputs_element:
                    if tipodato == TIPO_DATO.INT.value or tipodato == TIPO_DATO.BIT.value:
                        lista.append(int(input.text))
                    elif tipodato == TIPO_DATO.DECIMAL.value:
                        lista.append(float(input.text))
                    else:
                        lista.append(input.text)
                    tipolist.append(TIPO_DATO(tipodato))

                  
                return {"dato":lista,"tipo":tipolist}
            
        return {"dato":"No se pueden obtener los datos: no existe la columna.","tipo":"ERROR"}
    
    def add_database(self, database):
        

        # Comprueba si el nombre de la base de datos ya existe
        baseEncontrada = self.Existe_basedatos(database)
        if baseEncontrada[0]:
            return {"dato":"La base de datos ya existe.","tipo":"ERROR"}
        
        root = baseEncontrada[1]
        
        # Crea etiquetas para la nueva base de datos
        new_element = ET.Element("basedatos")
        elemento = ET.SubElement(new_element, "nombre")
        elemento.text = database
        elemento = ET.SubElement(new_element, "tablas")
        elemento = ET.SubElement(new_element, "funciones")
        elemento = ET.SubElement(new_element, "procedimientos")
        
        root.append(new_element)


        # Aquí es donde se realiza la conversión a una cadena con formato
        pretty_xml = self.prettify(root)

        with open(self.filepath, 'w') as f:
            f.write(pretty_xml)
        
        return {"dato":"Base de datos creada con éxito.","tipo":"."}

    def eliminardb(self, database):
        baseEncontrada = self.Existe_basedatos(database)
        if not baseEncontrada[0]:
            return {"dato":"La base de datos no existe.","tipo":"ERROR"}
        root = baseEncontrada[1]
        database_element = baseEncontrada[2]
        root.remove(database_element)

        pretty_xml = self.prettify(root)
        with open(self.filepath, 'w') as f:
            f.write(pretty_xml)
        
        return {"dato":"Base de datos eliminada con éxito.","tipo":"."}         
    def add_table_info(self, database, table):


        # Buscar la base de datos
        baseEncontrada = self.Existe_basedatos(database)
        if not baseEncontrada[0]:
            return {"dato":"La base de datos no existe.","tipo":"ERROR"}
        root = baseEncontrada[1]
        database_element = baseEncontrada[2]


        


        # Buscar o crear la etiqueta <tablas> dentro de la base de datos
        tablas_element = database_element.find('tablas')
        if tablas_element is None:
            tablas_element = ET.SubElement(database_element, "tablas")

        # Validar que no exista una tabla con el mismo nombre
        existing_tables = [tabla.find('nombre').text for tabla in tablas_element.findall('tabla')]
        if table.get("id") in existing_tables:
            return {"dato":"Ya existe una tabla con el mismo nombre.","tipo":"ERROR"}

        # Crear una nueva etiqueta <tabla> con la etiqueta <nombre> dentro
        new_table_element = ET.SubElement(tablas_element, "tabla")
        nombre_element = ET.SubElement(new_table_element, "nombre")
        nombre_element.text = table.get("id")
        # Crear una nueva etiqueta <columnas> dentro de la etiqueta <tabla>
        columnas_element = ET.SubElement(new_table_element, "columnas")


        # crear una etiqueta <columna> por cada columna de la tabla
        listacolumnas = []
        primary=0
        for columna in table.get("columnas"):

            # comprobacion de que no exista una columna con el mismo nombre
            if listacolumnas.count(columna.get("id")) > 0:
                return {"dato":"No se pudo crear tabla: Ya existe una columna con el mismo nombre.","tipo":"ERROR"}
            
            listacolumnas.append(columna.get("id"))

            new_columna_element = ET.SubElement(columnas_element, "columna")
            nombre = ET.SubElement(new_columna_element, "id")
            nombre.text = columna.get("id")
            tipo_element = ET.SubElement(new_columna_element, "tipo")
            tipo_dato_element = ET.SubElement(tipo_element, "tipodato")
            tipo_dato_element.text =str(columna.get("tipodato").get("tipo").value)
            
            longitud_dato = ET.SubElement(tipo_element, "longitud")
            longitud_dato.text = str(columna.get("tipodato").get("longitud"))

            tipo_atributo_element = ET.SubElement(new_columna_element, "atributo")
            # etiquetas nulo,nonulo, primaria, foranea, idtabla_ref, idcolumna_ref
            atributo_primaria_element = ET.SubElement(tipo_atributo_element, "primaria")
            atributo_foranea_element = ET.SubElement(tipo_atributo_element, "foranea")
            atributo_nulo_element = ET.SubElement(tipo_atributo_element, "nulo")
            atributo_nonulo_element = ET.SubElement(tipo_atributo_element, "nonulo")
            tablaref = ET.SubElement(tipo_atributo_element, "tablaref")
            columnaref = ET.SubElement(tipo_atributo_element, "columnaref")
            
            
            null_d=False
            notnull_d=False
            primarykey_d=False
            foranea_d=False
            if columna.get("atributo") != None:
                if len(columna.get("atributo"))<3:
                    for atributo in columna.get("atributo"):
                        atribevaluar= str(atributo.get("tipo").value)
                        if atribevaluar == "1":
                            primarykey_d=True
                            primary+=1
                            atributo_primaria_element.text = str(primarykey_d)
                        if atribevaluar == "3":
                            notnull_d=True
                            atributo_nonulo_element.text = str(notnull_d)
                        if atribevaluar == "4":
                            null_d=True
                            atributo_nulo_element.text = str(null_d)
                        if primarykey_d and null_d:
                            return {"dato":"No se pudo crear tabla: Una columna no puede ser primary key y null.","tipo":"ERROR"}
                        if null_d and notnull_d:
                            return {"dato":"No se pudo crear tabla: Una columna no puede ser null y not null.","tipo":"ERROR"}
                        if atribevaluar == "2":
                            if foranea_d:
                                return {"dato":"No se pudo crear tabla: Una columna no puede tener mas de un atributo de llave foranea.","tipo":"ERROR"}
                            foranea_d=True
                            atributo_foranea_element.text = str(foranea_d)
                            tablaref.text = atributo.get("idtabla_ref")
                            columnaref.text = atributo.get("idcolumna_ref")
                else:
                    return {"dato":"No se pudo crear tabla: Una columna no puede tener mas de dos atributo.","tipo":"ERROR"}
                
            tipo_atributo_element = ET.SubElement(new_columna_element, "inputs")
            
        if primary<1:
            return {"dato":"No se pudo crear tabla: Debe haber al menos una columna primary key.","tipo":"ERROR"}

        # Guardar los cambios en el archivo
        pretty_xml = self.prettify(root)

        with open(self.filepath, 'w') as f:
            f.write(pretty_xml)

        return {"dato":"Información de la tabla agregada con éxito.","tipo":"."}
    
    def drop_column(self, database, instruccion):
        baseDatosEncontrada = self.Existe_basedatos(database)
        if not baseDatosEncontrada[0]:
            return {"dato":"La base de datos no existe.","tipo":"ERROR"}
        root = baseDatosEncontrada[1]
        database_element = baseDatosEncontrada[2]

        idtabla = instruccion.get("idtabla")
        idcolumna = instruccion.get("idcolumna")

        tablas_element = database_element.find('tablas')
        if tablas_element is None:
            return {"dato":"No se puede eliminar columna: No existe la tabla.","tipo":"ERROR"}
        
        tablas_element = tablas_element.findall('tabla')
        existe = False
        tabla_element = None
        for tabla in tablas_element:
            if tabla.find('nombre').text == idtabla:
                existe = True
                tabla_element = tabla
                break
        if not existe:
            return {"dato":"No se puede eliminar columna: No existe la tabla.","tipo":"ERROR"}
            
        # recorrer todas las columnas en la etiqueta columnas de esa tabla
        columnas_todo = tabla_element.find('columnas')
        columnas_element = columnas_todo.findall('columna')

        for columna in columnas_element:

            if columna.find('id').text == idcolumna:
                # Use parent to remove the columna element
                print(columna)
                columnas_todo.remove(columna)
                print(columna)
                break

        pretty_xml = self.prettify(root)
        with open(self.filepath, 'w') as f:
            f.write(pretty_xml)

        return  {"dato":"Columna eliminada con éxito.","tipo":"."}
      
    def add_column(self, database, instruccion):
        baseDatosEncontrada = self.Existe_basedatos(database)
        if not baseDatosEncontrada[0]:
            return {"dato":"La base de datos no existe.","tipo":"ERROR"}
        root = baseDatosEncontrada[1]
        database_element = baseDatosEncontrada[2]

        print(instruccion)
        idtabla = instruccion.get("idtabla")
        idcolumna = instruccion.get("idcolumna")

        tipo = instruccion.get("tipodato")
        tipodato = tipo.get("tipo").value
        longitud = tipo.get("longitud")

        

        tablas_element = database_element.find('tablas')
        if tablas_element is None:
            return {"dato":"No se puede insertar columna: no existe la tabla","tipo":"ERROR"}
        tablas_element = tablas_element.findall('tabla')
        existe = False
        tabla_element = None
        for tabla in tablas_element:
            if tabla.find('nombre').text == idtabla:
                existe = True
                tabla_element = tabla
                break
        if not existe:
            return {"dato":"No se puede insertar columna: no existe la tabla","tipo":"ERROR"}
        
        # recorrer todas las columnas en la etiqueta columnas de esa tabla
        columnas_element = tabla_element.find('columnas')

        # comprobacion de que no exista una columna con el mismo nombre
        listacolumnas = []
        columna_element = columnas_element.findall('columna')
        for columna in columna_element:
            listacolumnas.append(columna.find('id').text)
        if listacolumnas.count(idcolumna) > 0:
            return {"dato":"No se puede insertar: Ya existe una columna con el mismo nombre.","tipo":"ERROR"}
        
        # crear una etiqueta <columna> por cada columna de la tabla
        new_columna_element = ET.SubElement(columnas_element, "columna")
        nombre = ET.SubElement(new_columna_element, "id")
        nombre.text = idcolumna
        tipo_element = ET.SubElement(new_columna_element, "tipo")
        tipo_dato_element = ET.SubElement(tipo_element, "tipodato")
        tipo_dato_element.text = str(tipodato)
        longitud_dato = ET.SubElement(tipo_element, "longitud")
        longitud_dato.text = str(longitud)
        tipo_atributo_element = ET.SubElement(new_columna_element, "atributo")
        # etiquetas nulo,nonulo, primaria, foranea, idtabla_ref, idcolumna_ref
        atributo_primaria_element = ET.SubElement(tipo_atributo_element, "primaria")
        atributo_foranea_element = ET.SubElement(tipo_atributo_element, "foranea")
        atributo_nulo_element = ET.SubElement(tipo_atributo_element, "nulo")
        atributo_nonulo_element = ET.SubElement(tipo_atributo_element, "nonulo")
        tablaref = ET.SubElement(tipo_atributo_element, "tablaref")
        columnaref = ET.SubElement(tipo_atributo_element, "columnaref")
        tipo_atributo_element = ET.SubElement(new_columna_element, "inputs")
        contador = 0

        null_d=False
        notnull_d=False
        primarykey_d=False

        if instruccion.get("atributo") != None:
            if len(instruccion.get("atributo"))<3:
                for atributo in instruccion.get("atributo"):
                    atribevaluar= str(atributo.get("tipo").value)
                    if atribevaluar == "1":
                        primarykey_d=True
                        atributo_primaria_element.text = str(primarykey_d)
                    if atribevaluar == "3":
                        notnull_d=True
                        atributo_nonulo_element.text = str(notnull_d)
                    if atribevaluar == "4":
                        null_d=True
                        atributo_nulo_element.text = str(null_d)
                    if primarykey_d and null_d:
                        return {"dato":"No se pudo insertar columna: Una columna no puede ser primary key y null.","tipo":"ERROR"}
                    if null_d and notnull_d:
                        return {"dato":"No se pudo insertar columna: Una columna no puede ser null y not null.","tipo":"ERROR"}
                    if atribevaluar == "2":
                        atributo_foranea_element.text = str(True)
                        tablaref.text = atributo.get("idtabla_ref")
                        columnaref.text = atributo.get("idcolumna_ref")
            else:
                return {"dato":"No se pudo insertar tabla: Una columna no puede tener mas de dos atributo.","tipo":"ERROR"}
            
       
        #Ver si las demas columnas tienen input en inputs
        for columna in columna_element:
            inputs_element = columna.find('inputs')
            for input in inputs_element:
                contador += 1
            break

        for agregar in range(contador):
            input_element = ET.SubElement(tipo_atributo_element, "input")
            input_element.text = "null"

        pretty_xml = self.prettify(root)
        with open(self.filepath, 'w') as f:
            f.write(pretty_xml)

        return {"dato":"Columna agregada con éxito.","tipo":"."}

    def drop_table(self, database, instruccion):
        baseDatosEncontrada = self.Existe_basedatos(database)
        if not baseDatosEncontrada[0]:
            return {"dato":"La base de datos no existe.","tipo":"ERROR"}
        root = baseDatosEncontrada[1]
        database_element = baseDatosEncontrada[2]

        idtabla = instruccion.get("id")

        tablass_element = database_element.find('tablas')
        if tablass_element is None:
            return {"dato":"No se puede eliminar la tabla: No existe tabla","tipo":"ERROR"}
        
        tablas_element = tablass_element.findall('tabla')
        existe = False
        tabla_element = None
        for tabla in tablas_element:
            if tabla.find('nombre').text == idtabla:
                existe = True
                tabla_element = tabla
                break
        if not existe:
            return {"dato":"No se puede eliminar la tabla: No existe tabla","tipo":"ERROR"}

        tablass_element.remove(tabla_element)

        pretty_xml = self.prettify(root)
        with open(self.filepath, 'w') as f:
            f.write(pretty_xml)

        return {"dato":"Tabla eliminada con exito","tipo":"."}
        
    def truncate_table(self, database, instruccion):
        baseDatosEncontrada = self.Existe_basedatos(database)
        if not baseDatosEncontrada[0]:
            return {"dato":"La base de datos no existe.","tipo":"ERROR"}
        root = baseDatosEncontrada[1]
        database_element = baseDatosEncontrada[2]

        idtabla = instruccion.get("id")

        tablass_element = database_element.find('tablas')
        if tablass_element is None:
            return {"dato":"No se pueden borrar registros por que no existe la tabla","tipo":"ERROR"}
        tablas_element = tablass_element.findall('tabla')
        existe = False
        tabla_element = None
        for tabla in tablas_element:
            if tabla.find('nombre').text == idtabla:
                existe = True
                tabla_element = tabla
                break
        if not existe:
            return {"dato":"No se pueden borrar registros por que no existe la tabla","tipo":"ERROR"}

        columnas_element = tabla_element.find('columnas')
        columna_element = columnas_element.findall('columna')
        for columna in columna_element:
            inputs_element = columna.find('inputs')
            inputs_element.clear()

        pretty_xml = self.prettify(root)
        with open(self.filepath, 'w') as f:
            f.write(pretty_xml)

        return {"dato":"Tabla truncada con exito","tipo":"."}

    def insert_data(self,database,table,columnas,valores):

        baseEncontrada = self.Existe_basedatos(database)
        if not baseEncontrada[0]:
            return {"dato":"La base de datos no existe.","tipo":"ERROR"}
        root = baseEncontrada[1]
        database_element = baseEncontrada[2]

        # valores a insertar
        idtabla = table

        if valores == None:
            return {"dato":"No se especificaron valores a insertar","tipo":"ERROR"}
        
        for i in range(len( valores)):
            if isinstance(valores[i], str):
                valores[i] = str(valores[i]).replace("'","").replace('"','')
            if isinstance(valores[i], int):
                valores[i] = int(str(valores[i]).replace("'","").replace('"',''))
            if isinstance(valores[i], float):
                valores[i] = float(str(valores[i]).replace("'","").replace('"',''))
        
        #buscar si existe la tabla con el idtabla, si no existe retorna error
        tablas_element = database_element.find('tablas')
        if tablas_element is None:
            return {"dato":"Tabla no existe no se puede insertar registro","tipo":"ERROR"}
        tablas_element = tablas_element.findall('tabla')
        existe = False
        tabla_element = None
        for tabla in tablas_element:
            if tabla.find('nombre').text == idtabla:
                existe = True
                tabla_element = tabla
                break
        if not existe:
            return {"dato":"Tabla no existe no se pueden insertar registros","tipo":"ERROR"}
        
        # recorrer todas las columnas en la etiqueta columnas de esa tabla
        columnas_element = tabla_element.find('columnas')
        columnas_element = columnas_element.findall('columna')
        # buscar si existe la columna en la lista de columnas a insertar
        if columnas is not None:
            # buscar si en columnas se encuentra *, si se encuentra retorna error
            for columna in columnas:
                if columna == "*":
                    return {"dato":"No se puede insertar con *","tipo":"ERROR"}
        
        
            existe = False
            for col in columnas:
                for columna in columnas_element:
                   
                    if columna.find('id').text == col:
                        existe = True
                        break
            if not existe:
                return {"dato":"No se puede insertar: No existe la columna " + columna.find('id').text + " en la lista de columnas.","tipo":"ERROR"}
        # RECOORER TODAS LAS COLUMNAS DE LA TABLA Y LOS INPUTS DE CADA COLUMNA QUE SEA PRIMARY KEY COLOCARLOS EN UNA LISTA
        listacolumnas = 0
        for columna in columnas_element:
            # buscar en atributo si la etiqueta primaria es true
            atributo = columna.find('atributo')
            if atributo.find('primaria').text=="True":
                listacolumnas+=1

        #llave compleja
        contador = 0
        for columna in columnas_element:
            # encontrar el tipodato de la columna y la longitud
            tipodato = int(columna.find('tipo').find('tipodato').text)
            longitud = columna.find('tipo').find('longitud').text
            if longitud != "None":
                longitud = int(longitud)
            # buscar atribut
            atributo = columna.find('atributo')
            
            # verificar cuantos inputs tiene la columna
            inputs_e = columna.find('inputs')
            inputs = inputs_e.findall('input')

            existe8 = False
         
            
            if columnas is not None:
                # revisar que la cantidad de columnas sea igual a la cantidad de valores
                if len(columnas) != len(valores):
                    return {"dato":"No se puede insertar: La cantidad de columnas no coincide con la cantidad de valores.","tipo":"ERROR"}
            
                if columnas.count(columna.find('id').text) > 1:
                    return {"dato":"No se puede insertar: No se puede insertar dos columnas con el mismo nombre.","tipo":"ERROR"}
            
                for col in columnas:
                    if columna.find('id').text == col:
                        existe8 = True

                        # si valores no es vacio
                        if len(valores) != 0:
                            
                            if valores[columnas.index(col)] != "null":
                                # verificamos que el tipo de dato sea el mismo que el valor a insertar
                                if tipodato == TIPO_DATO.INT.value or tipodato == TIPO_DATO.BIT.value:
                                    if isinstance(valores[columnas.index(col)], str):
                                        return {"dato":f"No se puede insertar: El tipo de dato no coincide con la columna {col}." ,"tipo":"ERROR"}
                                    #convertir a int
                                    valores[columnas.index(col)] = int(valores[columnas.index(col)])   
                                    
                                elif tipodato == TIPO_DATO.DECIMAL.value:
                                    
                                    if isinstance(valores[columnas.index(col)], str):
                                        return {"dato":f"No se puede insertar: Esta insertando un dato que no es {TIPO_DATO.DECIMAL.name} a la columna {col}","tipo":"ERROR"}
                                    #convertir a float
                                    valores[columnas.index(col)] = round(float(valores[columnas.index(col)]),2)
                                elif tipodato == TIPO_DATO.CHAR.value or tipodato == TIPO_DATO.VARCHAR.value:
                                    if not isinstance(valores[columnas.index(col)], str):
                                        return {"dato":f"No se puede insertar: El tipo de dato no coincide con la columna {col}." ,"tipo":"ERROR"}
                                    else:
                                        if len(valores[columnas.index(col)]) > longitud:
                                            return {"dato":"No se puede insertar: La logintud del valor a insertar no coincide.","tipo":"ERROR"}
                                        else:
                                            # si es un char agregar espacios necesarios para que sea del tamaño de la longitud
                                            if tipodato == TIPO_DATO.CHAR.value:
                                                valores[columnas.index(col)] = valores[columnas.index(col)].ljust(longitud)
                                elif tipodato == TIPO_DATO.DATE.value  :
                                    # verificar que el valor a insertar sea una fecha con formato de dd-mm-yyyy
                                    if not isinstance(valores[columnas.index(col)], str) or not re.match(r'\d{2}-\d{2}-\d{4}', valores[columnas.index(col)]):
                                        return {"dato":f"No se puede insertar: Esta insertando un dato que no es {TIPO_DATO.DATE.name} a la columna {col}","tipo":"ERROR"}
                                elif tipodato == TIPO_DATO.DATETIME.value:
                                    if not isinstance(valores[columnas.index(col)], str) or not re.match(r'\d{2}-\d{2}-\d{4} \d{2}:\d{2}:\d{2}', valores[columnas.index(col)]):
                                        return {"dato":f"No se puede insertar: Esta insertando un dato que no es {TIPO_DATO.DATETIME.name} a la columna {col}","tipo":"ERROR"}
                                    

             
                            # verificamos si el valor a insertar es null y si el atributo es not null, en este caso es error
                            if valores[columnas.index(col)] == "null" and atributo.find('nonulo').text=="True":  
                                return {"dato":f"No se puede insertar: La columna {col} no acepta valores null.","tipo":"ERROR"}
                            if str(valores[columnas.index(col)]) == "null" and atributo.find('primaria').text=="True":  
                                return {"dato":"No se puede insertar: una columna primary key no acepta valores null.","tipo":"ERROR"} 
                        
                            
                       

                            # verificamos si el atributo es primary key y validamos posibilidades
                            if atributo.find('primaria').text=="True":
                                # buscar si existe el valor en la columna
                                inputs_element = columna.find('inputs')
                                inputs_element = inputs_element.findall('input')
                                existe = False
                                for input in inputs_element:
                                    if input.text == str(valores[columnas.index(col)]):
                                        existe = True
                                        break
                                if existe:
                                    contador += 1
                        
                        
                        
                            if atributo.find('foranea').text=="True":
                                tablaref = atributo.find('tablaref').text
                                columnaref = atributo.find('columnaref').text
                                # buscar si existe la tablaref
                                tablas_element1 = database_element.find('tablas')
                                if tablas_element1 is None:
                                    return {"dato":"No se puede insertar: No existe la tabla de referencia.","tipo":"ERROR"}
                                tablas_element1 = tablas_element1.findall('tabla')
                                existe1 = False
                                columnas_element1=""
                                for tabla1 in tablas_element1:
                                    if tabla1.find('nombre').text == tablaref:
                                        existe1 = True
                                        columnas_element1 = tabla1.find('columnas')
                                        break
                                if not existe1:
                                    
                                    return {"dato":"No se puede insertar: No existe la tabla de referencia.","tipo":"ERROR"}
                                # buscar si existe la columnaref
                                
                                columnas_element1 = columnas_element1.findall('columna')
                                existe1 = False
                                atributo_ref1 =""
                                tipodato_ref1 = ""
                                longitud_ref1 = ""
                                inputs_element1 = ""
                           
                                for columna1 in columnas_element1:
                                    if columna1.find('id').text == columnaref:
                                        existe1 = True
                                        atributo_ref1 = columna1.find('atributo')
                                        tipodato_ref1 = int(columna1.find('tipo').find('tipodato').text)
                                        longitud_ref1 = columna1.find('tipo').find('longitud').text
                                        inputs_element1 = columna1.find('inputs')
                                        break
                                if not existe1:
                                    return {"dato":"No se puede insertar: No existe la columna de referencia.","tipo":"ERROR"}
                                # el atributo de la tabla de referencia debe ser primary key
                               
                                if atributo_ref1.find('primaria').text!="True"  :
                                    return  {"dato":"No se puede insertar: La columna de referencia debe ser primary key.","tipo":"ERROR"}
                                
                                
                                # optener el tipo de dato y longitud de la columna de referencia
                                
                                if longitud_ref1 != "None":
                                    longitud_ref1 = int(longitud_ref1)
                                # si no  verificar que el tipo de dato y la longitud coincidan
                                if tipodato != tipodato_ref1 or longitud != longitud_ref1:
                                    return {"dato":"No se puede insertar: El tipo de dato o la longitud no coinciden con la columna de referencia.","tipo":"ERROR"}
                                 
                                # recorrer los inputs de la columna de referencia
                                
                                inputs_element1 = inputs_element1.findall('input')

                                # buscar si existe el valor en la columna de referencia
                                existe4 = False
                                for input1 in inputs_element1:
                                    if input1.text == str(valores[columnas.index(col)]):
                                        existe4 = True
                                        break

                                if not existe4:
                                    return {"dato":"No se puede insertar: No existe el valor en la columna de referencia.","tipo":"ERROR"}  
                                 
                            # agregar un nuevo elemento 'input' a cada 'input' existente
                            input_element = ET.SubElement(inputs_e, "input")
                            input_element.text = str(valores[columnas.index(col)])

                            # eliminar el valor de la lista de valores valores.pop(columnas.index(col))
                        
                        break

            
            if not existe8:
                
                    # verificamos si su atributo es not null, en este caso es error
                    if atributo.find('nonulo').text=="True" or atributo.find('primaria').text=="True" or atributo.find('foranea').text=="True":  
                        return {"dato":f"No se puede insertar: La columna {columna.find('id').text} no acepta valores null.","tipo":"ERROR"}
                    
                    # agregamos un input con el valor null
                    input_element = ET.SubElement(inputs_e, "input")
                    input_element.text = "null" 
        print(" comprobacion de llave primaria")
        print(contador,listacolumnas)
        if contador == listacolumnas:
            return {"dato":f"No se puede insertar: el valor a insertar en la columna primaria ya existe.","tipo":"ERROR"}
        # agregar datos a xml
        pretty_xml = self.prettify(root)
        with open(self.filepath, 'w') as f:
            f.write(pretty_xml)

        return {"dato":"Fila insertada con exito","tipo":"."}
    
    def delete_registro(self,database,table,eliminar):

        baseDatosEncontrada = self.Existe_basedatos(database)
        if not baseDatosEncontrada[0]:
            return {"dato":"La base de datos no existe.","tipo":"ERROR"}
        root = baseDatosEncontrada[1]
        database_element = baseDatosEncontrada[2]
         #buscar si existe la tabla con el idtabla, si no existe retorna error
        tablass_element = database_element.find('tablas')
        if tablass_element is None:
            return {"dato":"No se puede eliminar registro porque no existe tabla.","tipo":"ERROR"}
        tablas_element = tablass_element.findall('tabla')
        existe = False
        tabla_element = None
        for tabla in tablas_element:
            if tabla.find('nombre').text == table:
                existe = True
                tabla_element = tabla
                break
        if not existe:
            return {"dato":"No se puede eliminar registro porque no existe tabla.","tipo":"ERROR"}




        if eliminar == None:
            return {"dato":"No se puede eliminar: ningun valor cumple las condiciones.","tipo":"ERROR"}
        
        columnas_element = tabla_element.find('columnas')
        columna_element = columnas_element.findall('columna')
        index=-1
        for col in eliminar:
            index+=1
            #recorrer todas las columnas de la tabla
            for columna in columna_element:
                # buscar todos los inputs de la columna
                inputs_element11 = columna.find('inputs')
                inputs_element = list(inputs_element11)
                # eliminar el input que coincida con la posicion col
                if col==1:
                    inputs_element11.remove(inputs_element[index])



        pretty_xml = self.prettify(root)
        with open(self.filepath, 'w') as f:
            f.write(pretty_xml)

        return {"dato":"Registro eliminado con exito.","tipo":"."}
            
    def UpdateTable(self, database, table, sets, listset, where ):
        baseDatosEncontrada = self.Existe_basedatos(database)
        if not baseDatosEncontrada[0]:
            return "La base de datos no existe."
        root = baseDatosEncontrada[1]
        database_element = baseDatosEncontrada[2]
         #buscar si existe la tabla con el idtabla, si no existe retorna error
        tablas_element = database_element.find('tablas')
        if tablas_element is None:
            return "No se puede eliminar : No existe la tabla." 
        
        tabla_element = tablas_element.findall('tabla')
        existe = False
        for tabla in tabla_element:
            if tabla.find('nombre').text == table:
                existe = True
                tabla_element = tabla
                break
        
        if not existe:
            return "No se puede actualizar la tabla : No existe la tabla."

        columnas_element = tabla_element.find('columnas')
        columna_element = columnas_element.findall('columna')


        intset = -1
        #print("sets ",sets)
        #print("listset ",listset)
        for col in sets:
            #print("col ",col)
            intset += 1
            #print("intset ",listset[intset])
            index=-1
            nombrecol = col.get("exp1")
            #recorrer todas las columnas de la tabla
            for columna in columna_element:
                #print("columna ",nombrecol)
                tipodato = int(columna.find('tipo').find('tipodato').text)
                longitud = columna.find('tipo').find('longitud').text
                if longitud != "None":
                    longitud = int(longitud)
                if columna.find('id').text == nombrecol:
                    #print("intset3 ",listset[intset])
                    # buscar todos los inputs de la columna
                    inputs_element11 = columna.find('inputs')
                    for input in inputs_element11:
                        index+=1
                      
                        if (not isinstance(listset[intset], list)) and (where[index] == 1):
                            #print("no lista: ",listset[intset])                     
                            valor = listset[intset]
  
                            if valor != "null":

                                # verificamos que el tipo de dato sea el mismo que el valor a insertar
                                if tipodato == TIPO_DATO.INT.value or tipodato == TIPO_DATO.BIT.value:
                                    if not isinstance(valor, int):
                                        return {"dato":f"No se puede insertar: El tipo de dato no coincide con la columna {col}." ,"tipo":"ERROR"}
                                    
                                    
                                elif tipodato == TIPO_DATO.DECIMAL.value:
                                    if not isinstance(valor, float):
                                        return {"dato":f"No se puede insertar: Esta insertando un dato que no es {TIPO_DATO.DECIMAL.name} a la columna {col}","tipo":"ERROR"}
                                elif tipodato == TIPO_DATO.CHAR.value or tipodato == TIPO_DATO.VARCHAR.value:
 
                                    if not isinstance(valor, str):
                                        return {"dato":f"No se puede insertar: El tipo de dato no coincide con la columna {col}." ,"tipo":"ERROR"}
                                    else:
                                        if len(valor) > longitud:
                                            return {"dato":"No se puede insertar: La logintud del valor a insertar no coincide.","tipo":"ERROR"}
                                        else:
                                            # si es un char agregar espacios necesarios para que sea del tamaño de la longitud
                                            if tipodato == TIPO_DATO.CHAR.value:
                                                valor = valor.ljust(longitud)
                                elif tipodato == TIPO_DATO.DATE.value  :
                                    # verificar que el valor a insertar sea una fecha con formato de dd-mm-yyyy
                                    if not isinstance(valor, str) or not re.match(r'\d{2}-\d{2}-\d{4}', valor):
                                        return {"dato":f"No se puede insertar: Esta insertando un dato que no es {TIPO_DATO.DATE.name} a la columna {col}","tipo":"ERROR"}
                                elif tipodato == TIPO_DATO.DATETIME.value:
                                    if not isinstance(valor, str) or not re.match(r'\d{2}-\d{2}-\d{4} \d{2}:\d{2}:\d{2}', valor):
                                        return {"dato":f"No se puede insertar: Esta insertando un dato que no es {TIPO_DATO.DATETIME.name} a la columna {col}","tipo":"ERROR"}
                            valor = str(valor).replace("'","").replace('"','')   
                            input.text = valor
                        elif(where[index] == 1):
                            #print("lista else ",listset)
                            listset2 = listset[intset]
                            #print("lista2 ",listset2)
                            if len(listset2) > 1:            
                                # eliminar el input que coincida con la posicion col
                                valor = listset2[index]

                                if valor != "null":
                                # verificamos que el tipo de dato sea el mismo que el valor a insertar
                                    if tipodato == TIPO_DATO.INT.value or tipodato == TIPO_DATO.BIT.value:
                                        if not isinstance(valor, int):
                                            return {"dato":f"No se puede insertar: El tipo de dato no coincide con la columna {col}." ,"tipo":"ERROR"}
                                        
                                        
                                    elif tipodato == TIPO_DATO.DECIMAL.value:
                                        if not isinstance(valor, float):
                                            return {"dato":f"No se puede insertar: Esta insertando un dato que no es {TIPO_DATO.DECIMAL.name} a la columna {col}","tipo":"ERROR"}
                                    elif tipodato == TIPO_DATO.CHAR.value or tipodato == TIPO_DATO.VARCHAR.value:
                                        if not isinstance(valor, str):
                                            return {"dato":f"No se puede insertar: El tipo de dato no coincide con la columna {col}." ,"tipo":"ERROR"}
                                        else:
                                            if len(valor) > longitud:
                                                return {"dato":"No se puede insertar: La logintud del valor a insertar no coincide.","tipo":"ERROR"}
                                            else:
                                                # si es un char agregar espacios necesarios para que sea del tamaño de la longitud
                                                if tipodato == TIPO_DATO.CHAR.value:
                                                    valor = valor.ljust(longitud)
                                    elif tipodato == TIPO_DATO.DATE.value  :
                                        # verificar que el valor a insertar sea una fecha con formato de dd-mm-yyyy
                                        if not isinstance(valor, str) or not re.match(r'\d{2}-\d{2}-\d{4}', valor):
                                            return {"dato":f"No se puede insertar: Esta insertando un dato que no es {TIPO_DATO.DATE.name} a la columna {col}","tipo":"ERROR"}
                                    elif tipodato == TIPO_DATO.DATETIME.value:
                                        if not isinstance(valor, str) or not re.match(r'\d{2}-\d{2}-\d{4} \d{2}:\d{2}:\d{2}', valor):
                                            return {"dato":f"No se puede insertar: Esta insertando un dato que no es {TIPO_DATO.DATETIME.name} a la columna {col}","tipo":"ERROR"}
                                valor = str(valor).replace("'","").replace('"','')
                                input.text = valor
                            else:
                                valor = listset2[0]

                                if valor != "null":
                                    # verificamos que el tipo de dato sea el mismo que el valor a insertar
                                    if tipodato == TIPO_DATO.INT.value or tipodato == TIPO_DATO.BIT.value:
                                        if not isinstance(valor, int):
                                            return {"dato":f"No se puede insertar: El tipo de dato no coincide con la columna {col}." ,"tipo":"ERROR"}
                                        
                                        
                                    elif tipodato == TIPO_DATO.DECIMAL.value:
                                        if not isinstance(valor, float):
                                            return {"dato":f"No se puede insertar: Esta insertando un dato que no es {TIPO_DATO.DECIMAL.name} a la columna {col}","tipo":"ERROR"}
                                    elif tipodato == TIPO_DATO.CHAR.value or tipodato == TIPO_DATO.VARCHAR.value:
                                        if not isinstance(valor, str):
                                            return {"dato":f"No se puede insertar: El tipo de dato no coincide con la columna {col}." ,"tipo":"ERROR"}
                                        else:
                                            if len(valor) > longitud:
                                                return {"dato":"No se puede insertar: La logintud del valor a insertar no coincide.","tipo":"ERROR"}
                                            else:
                                                # si es un char agregar espacios necesarios para que sea del tamaño de la longitud
                                                if tipodato == TIPO_DATO.CHAR.value:
                                                    valor = valor.ljust(longitud)
                                    elif tipodato == TIPO_DATO.DATE.value  :
                                        # verificar que el valor a insertar sea una fecha con formato de dd-mm-yyyy
                                        if not isinstance(valor, str) or not re.match(r'\d{2}-\d{2}-\d{4}', valor):
                                            return {"dato":f"No se puede insertar: Esta insertando un dato que no es {TIPO_DATO.DATE.name} a la columna {col}","tipo":"ERROR"}
                                    elif tipodato == TIPO_DATO.DATETIME.value:
                                        if not isinstance(valor, str) or not re.match(r'\d{2}-\d{2}-\d{4} \d{2}:\d{2}:\d{2}', valor):
                                            return {"dato":f"No se puede insertar: Esta insertando un dato que no es {TIPO_DATO.DATETIME.name} a la columna {col}","tipo":"ERROR"}
                                valor = str(valor).replace("'","").replace('"','')
                                input.text = valor

                


        pretty_xml = self.prettify(root)
        with open(self.filepath, 'w') as f:
            f.write(pretty_xml)


        return {"dato":"Tabla actualizada con exito","tipo":"."}
    
    def AgregarFuncion(self,database, instruccion):
        baseDatosEncontrada = self.Existe_basedatos(database)
        if not baseDatosEncontrada[0]:
            return {"dato":"La base de datos no existe.","tipo":"ERROR"}
        root = baseDatosEncontrada[1]
        database_element = baseDatosEncontrada[2]
        funciones_element = database_element.find('funciones')

        funcion_element = ET.SubElement(funciones_element, "funcion")
        funcion_nombre = ET.SubElement(funcion_element, "nombre")

        funcion_nombre.text = instruccion.get("id")
        # Guardar los cambios en el archivo
        pretty_xml = self.prettify(root)

        with open(self.filepath, 'w') as f:
            f.write(pretty_xml)

        return {"dato":"Funcion Creada Con Exito.","tipo":"."}

    def AgregarPorcedure(self,database, instruccion):
        baseDatosEncontrada = self.Existe_basedatos(database)
        if not baseDatosEncontrada[0]:
            return {"dato":"La base de datos no existe.","tipo":"ERROR"}
        root = baseDatosEncontrada[1]
        database_element = baseDatosEncontrada[2]
        funciones_element = database_element.find('procedimientos')

        funcion_element = ET.SubElement(funciones_element, "procedure")
        funcion_nombre = ET.SubElement(funcion_element, "nombre")

        funcion_nombre.text = instruccion.get("id")
        # Guardar los cambios en el archivo
        pretty_xml = self.prettify(root)

        with open(self.filepath, 'w') as f:
            f.write(pretty_xml)

        return {"dato":"Funcion Creada Con Exito.","tipo":"."}
    
    

    



    


        




