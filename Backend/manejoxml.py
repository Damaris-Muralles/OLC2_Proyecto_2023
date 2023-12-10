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

