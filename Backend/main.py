import Analizadores.gramar as g
from Analizadores.instrucciones import *
from BaseDatos.manejoxml import *
from Entornos.Entorno import *
from Entornos.ListaMetodo import *
from Entornos.ListaSimbolos import *
from Separar.Globales import *

from flask import Flask, request, jsonify
from flask_cors import CORS


xml = XMLManejador("./BaseDatos/BasesDatos.xml")  
lsimbolo = ListaSimbolo()
lmetodo = ListaMetodo()

def procesar_instrucciones(instrucciones) :
    ## lista de instrucciones recolectadas
    entornoG = Entorno(None, "global")
    Globales(instrucciones, entornoG, xml, lsimbolo, lmetodo)
    return "Procesamiento exitoso"
    
    
    
"""

CREATE DATA BASE intento;

USE intento;

Create Table Tabla1(
    ide int PRIMARY KEY,
    nombre nvarchar(100),
    edad int
);

Create Procedure Valores()
AS
Begin

    DECLARE @IVA INT;
    DECLARE @ENTERO INT = 5+5;
    DECLARE @Palabra nVARCHAR(100);

    SET @IVA = 2 + @ENTERO;

    insert into Tabla1(ide, nombre, edad) values (1, 'Juan', 20);
    insert into Tabla1(ide, nombre, edad) values (2, 'Antonio', 32);
    insert into Tabla1(ide, nombre, edad) values (3, 'Maria', 25);
    insert into Tabla1(ide, nombre, edad) values (4, 'Jose', 28);
    insert into Tabla1(ide, nombre, edad) values (5, 'Pedro', 30);
end;


Create Procedure actualizar(@Prueba nVARCHAR(15), @Prueba2 nVARCHAR(15))
AS
Begin
    
    DECLARE @Limite INT = 29;
    DECLARE @comienzo INT;
    DECLARE @IVA INT;
    DECLARE @ENTERO INT = 100;
    DECLARE @Palabra nVARCHAR(100) ;
    DECLARE @Palabra2 nVARCHAR(100) = 'PRUEBA';
    DECLARE @Fecha DATE = '04-10-2020';

    set @comienzo = 2;
    set @Palabra = 'Global';
    SET @IVA = 2 + 2;


    while @comienzo < 5 
    begin
        update Tabla1 set nombre == @Prueba where ide == @comienzo;
        set @comienzo = @comienzo + 1;
    end;

    CASE 
            WHEN @IVA > 3 && @Prueba2 == 'Prueba1'
				THEN SET @Palabra = 'SoyCase1';
			WHEN @IVA > 3 && @Prueba2 == 'Pruebas2'
				THEN SET @Palabra = 'SoyCase2';					
			ELSE 
				THEN SET @Palabra = 'SoyElse';
	END;

    update Tabla1 set nombre == @Palabra where nombre == 'datosnuevo';

    


end;

Valores();
actualizar('datosnuevo', 'Pruebas2');
"""


app = Flask(__name__)
CORS(app)
@app.route('/a', methods=['POST'])
def procesar():
    global lsimbolo

      
    global lmetodo
    lsimbolo = ListaSimbolo()
    lmetodo = ListaMetodo()
    imprimir=""
    Errorlexico=""
    ErrorSintactico=""
    Gramatical=""
    tablasimbolo=""
    tablametodo=""
    arbol=""
    lista1=[]

    
    try:

        data = request.get_json()
        entrada = data['entrada']
        da=g.lexico(entrada.lower())
        print("tokens::::::::::::::::::::::::::::::::::")
        print(da[0])
        Gramatical=da[0]
        print("errores::::::::::::::::::::::::::::::::::")
        print(da[1])
        Errorlexico=da[1]
            

        instrucciones = g.parse(entrada.lower())
        ErrorSintactico=instrucciones[1]
        if instrucciones[0]!=None:
             
            imprimir = procesar_instrucciones(instrucciones[0])
    except Exception as e:
        print(">>>>> entro en la excepcion")
        return jsonify({'message': 'Procesamiento fallido','lista':lista1,'imprimir':imprimir,'Errorlexico':Errorlexico,'ErrorSintactico':ErrorSintactico,'Gramatical':Gramatical,'tablasim':tablasimbolo,'tablamet':tablametodo,'arbol':arbol})


    #lista1=xml.recorridoarbol()
    return jsonify({'message': 'Procesado con éxito','lista':lista1,'imprimir':imprimir,'Errorlexico':Errorlexico,'ErrorSintactico':ErrorSintactico,'Gramatical':Gramatical,'tablasim':tablasimbolo,'tablamet':tablametodo,'arbol':arbol})


@app.route('/crear', methods=['POST'])
def creardb():
    data = request.get_json()
    entrada = data['entrada']
    lista1=[]
    try:
        print(xml.add_database(entrada))
    except Exception as e:
        print(">>>>> entro en la excepcion")
        return jsonify({'message': 'Creado fallido','lista':lista1})
        
    lista1=xml.recorridoarbol()
    return jsonify({'message': 'Creado con éxito','lista':lista1})


@app.route('/eliminar', methods=['POST'])
def eliminado():
    data = request.get_json()
    entrada = data['entrada']
    lista1=[]
    try:
        print( xml.eliminardb(entrada))  
    except Exception as e:
            print(">>>>> entro en la excepcion")
            return jsonify({'message': 'Creado fallido','lista':lista1})
    
    lista1=xml.recorridoarbol()
    return jsonify({'message': 'Eliminado con éxito','lista':lista1})


@app.route('/get_data', methods=['GET'])
def get_data():
    # Simulando datos del backend
    data = xml.recorridoarbol()
    return jsonify(data)



if __name__ == '__main__':
  app.run(port=5000)




