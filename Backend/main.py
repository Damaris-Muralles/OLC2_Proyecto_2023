import Analizadores.gramar as g
from Analizadores.instrucciones import *
from BaseDatos.manejoxml import *
from Entornos.Entorno import *
from Entornos.ListaMetodo import *
from Entornos.ListaSimbolos import *

from Separar.Globales import *

xml = XMLManejador("./BaseDatos/BasesDatos.xml")  
lsimbolo = ListaSimbolo()
lmetodo = ListaMetodo()

def procesar_instrucciones(instrucciones) :
    ## lista de instrucciones recolectadas
    entornoG = Entorno(None, "global")
    Globales(instrucciones, entornoG, xml, lsimbolo, lmetodo)

    
    
    

#f = open("./entrada.txt", "r")

#input = f.read()
# otras pruebas de entrada


input = """

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
end;

Valores();
actualizar('datosnuevo', 'Pruebas2');
"""

instrucciones = g.parse(input.lower())
if instrucciones!=None:

    procesar_instrucciones(instrucciones)



