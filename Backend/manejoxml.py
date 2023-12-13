import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

def prettify(elem):
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return '\n'.join([line for line in reparsed.toprettyxml(indent="  ").split('\n') if line.strip()])

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

    def add_data(self, data):
        


        tree = ET.parse(self.filepath)
        root = tree.getroot()



        new_element = ET.Element("data")
        new_element.text = data
        root.append(new_element)
        tree.write(self.filepath)
    
    def add_database(self, database):
        tree = ET.parse(self.filepath)
        root = tree.getroot()

        # Comprueba si el nombre de la base de datos ya existe
        for element in root.findall('basedatos'):
            if element.find('nombre').text == database:
                return "La base de datos ya existe."


        new_element = ET.Element("basedatos")
        nombre = ET.SubElement(new_element, "nombre")
        nombre.text = database
        tablas = ET.SubElement(new_element, "tablas")
        funciones = ET.SubElement(new_element, "funciones")
        procedimientos = ET.SubElement(new_element, "procedimientos")
        
        root.append(new_element)

        # Aquí es donde se realiza la conversión a una cadena con formato
        pretty_xml = prettify(root)

        with open(self.filepath, 'w') as f:
            f.write(pretty_xml)
        
        return
    
    def add_table_info(self, database, table):
        tree = ET.parse(self.filepath)
        root = tree.getroot()

        # Buscar la base de datos
        database_element = None
        for element in root.findall('basedatos'):
            if element.find('nombre').text == database:
                database_element = element
                break

        if database_element is None:
            return "La base de datos no existe."

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
        for columna in table.get("columnas"):
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
            print("atributo")
            
            print(columna.get("atributo"))
            
                 
            if columna.get("atributo") != None:
                tipo_atributo_element.text = str(columna.get("atributo").get("tipo").value)               
                if columna.get("atributo").get("tipo").value == 2:
                    print("entro FORANEAS")
                    atributo_tablaref_element.text = columna.get("atributo").get("idtabla_ref")          
                    atributo_columnaref_element.text = columna.get("atributo").get("idcolumna_ref")
            
            tipo_atributo_element = ET.SubElement(new_columna_element, "inputs")
            

        # Guardar los cambios en el archivo
        pretty_xml = self.prettify(root)

        with open(self.filepath, 'w') as f:
            f.write(pretty_xml)

        return "Información de la tabla agregada con éxito."