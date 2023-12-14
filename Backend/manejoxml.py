import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from instrucciones import *


class XMLManejador:
    def __init__(self, filepath):
        self.filepath = filepath
        self.arbol = ET.parse(filepath)
        self.raiz = self.arbol.getroot()

    def prettify(self, elem):
        rough_string = ET.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return '\n'.join([line for line in reparsed.toprettyxml(indent="  ").split('\n') if line.strip()])


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
    
    def add_database(self, database):
        

        # Comprueba si el nombre de la base de datos ya existe
        baseEncontrada = self.Existe_basedatos(database)
        if baseEncontrada[0]:
            return "La base de datos ya existe."
        
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
        
        return "Base de datos creada con éxito."
    
    def add_table_info(self, database, table):


        # Buscar la base de datos
        baseEncontrada = self.Existe_basedatos(database)
        if not baseEncontrada[0]:
            return "La base de datos no existe."
        root = baseEncontrada[1]
        database_element = baseEncontrada[2]


        


        # Buscar o crear la etiqueta <tablas> dentro de la base de datos
        tablas_element = database_element.find('tablas')
        if tablas_element is None:
            tablas_element = ET.SubElement(database_element, "tablas")

        # Validar que no exista una tabla con el mismo nombre
        existing_tables = [tabla.find('nombre').text for tabla in tablas_element.findall('tabla')]
        if table.get("id") in existing_tables:
            return "Ya existe una tabla con el mismo nombre."

        # Crear una nueva etiqueta <tabla> con la etiqueta <nombre> dentro
        new_table_element = ET.SubElement(tablas_element, "tabla")
        nombre_element = ET.SubElement(new_table_element, "nombre")
        nombre_element.text = table.get("id")
        # Crear una nueva etiqueta <columnas> dentro de la etiqueta <tabla>
        columnas_element = ET.SubElement(new_table_element, "columnas")


        # crear una etiqueta <columna> por cada columna de la tabla
        listacolumnas = []
        for columna in table.get("columnas"):

            # comprobacion de que no exista una columna con el mismo nombre
            if listacolumnas.count(columna.get("id")) > 0:
                return "No se pudo crear tabla: Ya existe una columna con el mismo nombre."
            
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
            atributo_tablaref_element = ET.SubElement(new_columna_element, "tablaref")
            atributo_columnaref_element = ET.SubElement(new_columna_element, "columnaref")
            
            if columna.get("atributo") != None:
                tipo_atributo_element.text = str(columna.get("atributo").get("tipo").value)               
                if columna.get("atributo").get("tipo").value == 2:
                    atributo_tablaref_element.text = columna.get("atributo").get("idtabla_ref")          
                    atributo_columnaref_element.text = columna.get("atributo").get("idcolumna_ref")
            
            tipo_atributo_element = ET.SubElement(new_columna_element, "inputs")
            

        # Guardar los cambios en el archivo
        pretty_xml = self.prettify(root)

        with open(self.filepath, 'w') as f:
            f.write(pretty_xml)

        return "Información de la tabla agregada con éxito."
    
    def insert_data(self,database,table):

        baseEncontrada = self.Existe_basedatos(database)
        if not baseEncontrada[0]:
            return "La base de datos no existe."
        root = baseEncontrada[1]
        database_element = baseEncontrada[2]

        # valores a insertar
        idtabla = table.get("id")
        columnas = table.get("columnas")
        valores = table.get("valores")
        
        # buscar si en columnas se encuentra *, si se encuentra retorna error
        for columna in columnas:
            if columna == "*":
                return "No se puede insertar con *"
        
        #buscar si existe la tabla con el idtabla, si no existe retorna error
        tablas_element = database_element.find('tablas')
        if tablas_element is None:
            return "No se puede insertar: No existe la tabla."
        tablas_element = tablas_element.findall('tabla')
        existe = False
        tabla_element = None
        for tabla in tablas_element:
            if tabla.find('nombre').text == idtabla:
                existe = True
                tabla_element = tabla
                break
        if not existe:
            return "No se puede insertar: No existe la tabla."
        
        # recorrer todas las columnas en la etiqueta columnas de esa tabla
        columnas_element = tabla_element.find('columnas')
        columnas_element = columnas_element.findall('columna')
        for columna in columnas_element:
            # buscar si existe la columna en la lista de columnas a insertar
            existe = False
            for col in columnas:
                if columna.find('id').text == col:
                    existe = True
                    break
            if not existe:
                return "No se puede insertar: No existe la columna " + columna.find('id').text + " en la lista de columnas."

            for col in columnas:
                if columna.find('id').text == col:
                    existe = True
                    # encontrar el tipodato de la columna y la longitud
                    tipodato = int(columna.find('tipo').find('tipodato').text)
                    longitud = columna.find('tipo').find('longitud').text
                    if longitud != "None":
                        longitud = int(longitud)
                    # buscar atributo
                    atributo = int(columna.find('atributo').text)
                    # verificar cuantos inputs tiene la columna
                    inputs_e = columna.find('inputs')
                    inputs = inputs_e.findall('input')



                    # si atributo es foranea, buscar si existe la tablaref y la columnaref
                    if atributo== TIPO_ATRIBUTO.FOREIGN_KEY:
                        tablaref = columna.find('tablaref').text
                        columnaref = columna.find('columnaref').text
                        # buscar si existe la tablaref
                        tablas_element = database_element.find('tablas')
                        if tablas_element is None:
                            return "No se puede insertar: No existe la tabla de referencia."
                        tablas_element = tablas_element.findall('tabla')
                        existe = False
                        for tabla in tablas_element:
                            if tabla.find('nombre').text == tablaref:
                                existe = True
                                break
                        if not existe:
                            return "No se puede insertar: No existe la tabla de referencia."
                        # buscar si existe la columnaref
                        columnas_element = tabla.find('columnas')
                        columnas_element = columnas_element.findall('columna')
                        existe = False
                        for columna in columnas_element:
                            if columna.find('id').text == columnaref:
                                existe = True
                                break
                        if not existe:
                            return "No se puede insertar: No existe la columna de referencia."
                        # optener el tipo de dato y longitud de la columna de referencia
                        tipodato_ref = int(columna.find('tipo').find('tipodato').text)
                        longitud_ref = int(columna.find('tipo').find('longitud').text)
                        # si no  verificar que el tipo de dato y la longitud coincidan
                        if tipodato != tipodato_ref or longitud != longitud_ref:
                            return "No se puede insertar: El tipo de dato o la longitud no coinciden con la columna de referencia."
                        # recorrer los inputs de la columna de referencia
                        inputs_element = columna.find('inputs')
                        inputs_element = inputs_element.findall('input')

                        # si la cantidad de inputs_element es menor a inputs+1, retornar error
                        if len(inputs_element) < len(inputs)+1:
                            return "No se puede insertar: Faltan datos en la columna de referencia."
                        
                        # si no  tomar el valor de la columna de referencia y agregar un input con ese valor
                        
                        posicion=0
                        for input in inputs_element:
                            posicion+=1
                            if posicion== len(inputs)+1:
                                input_element = ET.SubElement(inputs_e, "input")
                                input_element.text = input.text
                                break
                            
                    else:
                        # si valores no es vacio
                        if len(valores) == 0:
                            # verificamos si su atributo es not null, en este caso es error
                            if atributo == TIPO_ATRIBUTO.NOT_NULL:  
                                return "No se puede insertar: La columna no acepta valores null."
                            # agregamos un input con el valor null
                            input_element = ET.SubElement(inputs, "input")
                            input_element.text = "null"
                        else:
                        
                            # verificamos que el tipo de dato sea el mismo que el valor a insertar
                            if tipodato == TIPO_DATO.INT or tipodato == TIPO_DATO.BIT:
                                if not isinstance(valores[0], int):
                                    return "No se puede insertar: El tipo de dato no coincide con la columna." 
                            elif tipodato == TIPO_DATO.DECIMAL:
                                if not isinstance(valores[0], float):
                                    return "No se puede insertar: El tipo de dato no coincide con la columna."
                            elif tipodato == TIPO_DATO.CHAR or tipodato == TIPO_DATO.VARCHAR:
                                if not isinstance(valores[0], str):
                                    return "No se puede insertar: El tipo de dato no coincide con la columna." 
                                else:
                                    if len(valores[0]) > longitud:
                                        return "No se puede insertar: La logintud del valor a insertar no coincide."

                            # verificamos si el valor a insertar es null y si el atributo es not null, en este caso es error
                            if valores[0] == "null" and atributo == TIPO_ATRIBUTO.NOT_NULL:  
                                return "No se puede insertar: La columna no acepta valores null."
                            
                           
                            # agregar un nuevo elemento 'input' a cada 'input' existente
                            input_element = ET.SubElement(inputs_e, "input")
                            input_element.text = str(valores[0])

                            # eliminar el valor de la lista de valores
                            valores.pop(0)

                    break
        # agregar datos a xml
        pretty_xml = self.prettify(root)
        with open(self.filepath, 'w') as f:
            f.write(pretty_xml)

        return "Fila insertada con éxito."
    
    def drop_column(self, database, instruccion):
        baseDatosEncontrada = self.Existe_basedatos(database)
        if not baseDatosEncontrada[0]:
            return "La base de datos no existe."
        root = baseDatosEncontrada[1]
        database_element = baseDatosEncontrada[2]

        idtabla = instruccion.get("idtabla")
        idcolumna = instruccion.get("idcolumna")

        tablas_element = database_element.find('tablas')
        if tablas_element is None:
            return "No se puede insertar: No existe la tabla."
        tablas_element = tablas_element.findall('tabla')
        existe = False
        tabla_element = None
        for tabla in tablas_element:
            if tabla.find('nombre').text == idtabla:
                existe = True
                tabla_element = tabla
                break
        if not existe:
            return "No se puede insertar: No existe la tabla."

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

        return "Columna eliminada con éxito."

    def add_column(self, database, instruccion):
        baseDatosEncontrada = self.Existe_basedatos(database)
        if not baseDatosEncontrada[0]:
            return "La base de datos no existe."
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
            return "No se puede insertar: No existe la tabla."
        tablas_element = tablas_element.findall('tabla')
        existe = False
        tabla_element = None
        for tabla in tablas_element:
            if tabla.find('nombre').text == idtabla:
                existe = True
                tabla_element = tabla
                break
        if not existe:
            return "No se puede insertar: No existe la tabla."
        
        # recorrer todas las columnas en la etiqueta columnas de esa tabla
        columnas_element = tabla_element.find('columnas')

        # comprobacion de que no exista una columna con el mismo nombre
        listacolumnas = []
        columna_element = columnas_element.findall('columna')
        for columna in columna_element:
            listacolumnas.append(columna.find('id').text)
        if listacolumnas.count(idcolumna) > 0:
            return "No se puede insertar: Ya existe una columna con el mismo nombre."
        
        # crear una etiqueta <columna> por cada columna de la tabla
        new_columna_element = ET.SubElement(columnas_element, "columna")
        nombre = ET.SubElement(new_columna_element, "id")
        nombre.text = idcolumna
        tipo_element = ET.SubElement(new_columna_element, "tipo")
        tipo_dato_element = ET.SubElement(tipo_element, "tipodato")
        tipo_dato_element.text = str(tipodato)
        longitud_dato = ET.SubElement(tipo_element, "longitud")
        longitud_dato.text = str(longitud)
        tipo_atribut_element = ET.SubElement(new_columna_element, "atributo")
        atributo_tablaref_element = ET.SubElement(new_columna_element, "tablaref")
        atributo_columnaref_element = ET.SubElement(new_columna_element, "columnaref")
        tipo_atributo_element = ET.SubElement(new_columna_element, "inputs")
        contador = 0

        if instruccion.get("atributo") != None:
            atributo = instruccion.get("atributo")
            tipoatributo = atributo.get("tipo").value

            tipo_atribut_element.text = str(tipoatributo)               
            if tipoatributo == 2:
                tablaref = atributo.get("idtabla_ref")
                columnaref = atributo.get("idcolumna_ref")
                atributo_tablaref_element.text = tablaref          
                atributo_columnaref_element.text = columnaref
       
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

        return "Columna agregada con éxito."
    
    def drop_table(self, database, instruccion):
        baseDatosEncontrada = self.Existe_basedatos(database)
        if not baseDatosEncontrada[0]:
            return "La base de datos no existe."
        root = baseDatosEncontrada[1]
        database_element = baseDatosEncontrada[2]

        idtabla = instruccion.get("id")

        tablass_element = database_element.find('tablas')
        if tablass_element is None:
            return "No se puede insertar: No existe la tabla."
        tablas_element = tablass_element.findall('tabla')
        existe = False
        tabla_element = None
        for tabla in tablas_element:
            if tabla.find('nombre').text == idtabla:
                existe = True
                tabla_element = tabla
                break
        if not existe:
            return "No se puede insertar: No existe la tabla."

        tablass_element.remove(tabla_element)

        pretty_xml = self.prettify(root)
        with open(self.filepath, 'w') as f:
            f.write(pretty_xml)

        return "Tabla eliminada con éxito."
    
    def truncate_table(self, database, instruccion):
        baseDatosEncontrada = self.Existe_basedatos(database)
        if not baseDatosEncontrada[0]:
            return "La base de datos no existe."
        root = baseDatosEncontrada[1]
        database_element = baseDatosEncontrada[2]

        idtabla = instruccion.get("id")

        tablass_element = database_element.find('tablas')
        if tablass_element is None:
            return "No se puede insertar: No existe la tabla."
        tablas_element = tablass_element.findall('tabla')
        existe = False
        tabla_element = None
        for tabla in tablas_element:
            if tabla.find('nombre').text == idtabla:
                existe = True
                tabla_element = tabla
                break
        if not existe:
            return "No se puede insertar: No existe la tabla."

        columnas_element = tabla_element.find('columnas')
        columna_element = columnas_element.findall('columna')
        for columna in columna_element:
            inputs_element = columna.find('inputs')
            inputs_element.clear()

        pretty_xml = self.prettify(root)
        with open(self.filepath, 'w') as f:
            f.write(pretty_xml)

        return "Tabla truncada con éxito."

        
        



        




