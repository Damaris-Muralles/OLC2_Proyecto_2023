
from instrucciones import *
# Lista de palabras reservadas
reservadas = {
    # instrucciones
    'create' : 'CREATE',
    'alter' : 'ALTER',
    'usar' : 'USAR',
    'drop' : 'DROP',
    'truncate' : 'TRUNCATE',
    'select' : 'SELECT',
    'update' : 'UPDATE',
    'delete' : 'DELETE',
    'insert' : 'INSERT',
    'function' : 'FUNCTION',    
    'procedure' : 'PROCEDURE',
    'if' : 'IF',
    'case' : 'CASE',

    # adicioneales
    'data' : 'DATA',
    'base' : 'BASE',
    'into' : 'INTO',
    'table' : 'TABLE',
    'declare' : 'DECLARE',
    'add'  : 'ADD', 
    'set' : 'SET',
    'exc' : 'EXC',
    'begin' : 'BEGIN',
    'when' : 'WHEN',
    'then' : 'THEN',
    'else' : 'ELSE',
    'from' : 'FROM',
    'where' : 'WHERE',
    'end' : 'END',
    'as' : 'AS',
    'key' : 'KEY',
    'values' : 'VALUES',
    'primary' : 'PRIMARY',
    'foreing' : 'FOREIGN',
    'references' : 'REFERENCES',
    'column'   : 'COLUMN',

    # funciones
    'cast' : 'CAST',
    'suma' : 'SUMA',
    'contar' : 'CONTAR',
    'return' : 'RETURN',
    'concatena' : 'CONCATENA',
    'hoy' : 'HOY',
    'substraer' : 'SUBSTRAER',
    
    # tipos de datos
    'null' : 'NULL',
    'not' : 'NOT',
    'varchar' : 'VARCHAR',
    'char' : 'CHAR',
    'int' : 'INT',
    'integer' : 'INTEGER',
    'decimal' : 'DECIMAL',
    'bit' : 'BIT',
    'date' : 'DATE',
    'datetime' : 'DATETIME'
   
    
}

tokens  =  [
   
    # simbolos     
    'PARIZQ',
    'PARDER',
    'COMA',
    'PUNTO',
    'PTCOMA',
    'IGUALSIMPLE',
    
    # operadores
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',    
    'AND',
    'OR',
    'NEGACION',
    'IGUAL',
    'DIFERENTE',
    'MAYORQUE',
    'MENORQUE',
    'MAYORIGUAL',
    'MENORIGUAL',
    
    # expresiones regulares
    'ENTERO',
    'DECIMALES',
    'IDENTIFICADOR',
    'CADENA',
    'FECHA',
    'FECHAHORA',
    'IDENT'

] + list(reservadas.values())

# Tokens
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_COMA      = r','
t_PUNTO     = r'\.'
t_PTCOMA    = r';'
t_AND       = r'&&'
t_OR        = r'\|\|'
t_NEGACION   = r'!'
t_IGUAL     = r'=='
t_DIFERENTE = r'!='
t_MAYORQUE  = r'>'
t_MENORQUE  = r'<'
t_MAYORIGUAL= r'>='
t_MENORIGUAL= r'<='
t_IGUALSIMPLE = r'='

# Expresiones regulares
def t_FECHAHORA(t):
    r'\d{2}-\d{2}-\d{4}\s\d{2}:\d{2}:\d{2}'
    return t

def t_FECHA(t):
    r'\d{2}-\d{2}-\d{4}'
    return t

def t_DECIMALES(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("El valor float es muy largo %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("El valor del entero es muy largo %d", t.value)
        t.value = 0
    return t

def t_IDENTIFICADOR(t):
    r'@[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_CADENA(t):
    r'(\'[^\']*\'|\"[^\"]*\")'
    t.value = t.value[1:-1] # remuevo las comillas
    return t

def t_IDENT(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(),'IDENT')
    return t


# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Error lexico: Caracter '%s' no es valido" % t.value[0])
    t.lexer.skip(1)
    
# Construyendo el analizador lexico
import ply.lex as lex
lexer = lex.lex()


# prueba del analizador lexico
'''
data="""
CREATE FUNCTION Retornasuma(@ProductID int)
RETURN int
AS
BEGIN
    DECLARE @ret int;
    SELECT @ret == SUM(Cantidad) FROM inventario WHERE ProductoId == @ProductID; 

    IF (@ret == NULL)
        SET @ret = 0;
    END;

    RETURN @ret;
END;
"""
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok: break
    print(tok)
'''


# Asociación de operadores y precedencia
precedence = (
    ('right', 'NEGACION'), 
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIDO'),
    ('nonassoc', 'PARDER', 'PARIZQ'),
    ('left', 'IGUAL', 'DIFERENTE', 'MAYORQUE','MENORQUE', 'MENORIGUAL', 'MAYORIGUAL'),
    ('right', 'OR'),
    ('right', 'AND'),
    )

# Definición de la gramática

def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]
   

def p_instrucciones_lista(t) :
    'instrucciones    : instrucciones instruccion'
    t[0] = t[1]
    t[1].append(t[2])


def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    t[0] = [t[1]]
    


def p_instruccion(t) :
    '''instruccion      : use_database
                        | createtab_instr
                        | createbase_instr  
                        | alter_instr
                        | truncate_instr
                        | drop_instr
                        | delete_instr
                        | update_instr
                        | select_instr
                        | insert_instr
                        | declaracionvariable
                        | asignacionvariable
                        | if_instr
                        | create_procedure
                        | create_funcion
                        | retornar
                        | case_instr


    '''
    t[0] = t[1]


#TIPOS DE DATOS
def p_tipodato(t):
    '''
    tipodato   : DECIMAL PARIZQ ENTERO COMA ENTERO PARDER
                | INT
                | INTEGER
                | DECIMAL
                | BIT
                | DATE
                | DATETIME
                | VARCHAR PARIZQ ENTERO PARDER
                | CHAR PARIZQ ENTERO PARDER
                | VARCHAR
                | CHAR
                
    '''
    if len(t)==2:
        t[0] = TipoDato(t[1],None,None)
    elif len(t)==5:
        t[0] = TipoDato(t[1],t[3],None)
    elif len(t)==7:
        t[0] = TipoDato(t[1],t[3],t[5])

# SINTAXIS PARA USAR BASE DE DATOS
def p_use_database(t):
    'use_database : USAR IDENT PTCOMA'
    t[0] = UseDatabase(t[2])

# SINTAXIS PARA CREAR BASE DE DATOS
def p_createbase_instr(t):
    'createbase_instr : CREATE DATA BASE IDENT PTCOMA'
    t[0] = CreateDatabase(t[3])

# SINTAXIS PARA CREATE TABLE
def p_create_table_instr(t) :
    'createtab_instr     : CREATE TABLE IDENT PARIZQ listacolumnas PARDER PTCOMA'
    t[0] = CreateTable(t[3], t[5])

def p_listacolumnas(t) :
    ''' listacolumnas   : listacolumnas columna
                        | columna'''
    if len(t) ==3:
        t[0] = t[1]
        t[1].append(t[2])
    else:
        t[0] = [t[1]]

def p_columna(t):
    '''
    columna    : IDENT tipodato atributo COMA
                | IDENT tipodato atributo 
                | IDENT tipodato COMA
                | IDENT tipodato
    '''
    if len(t)==5:
        t[0] = ColumnaTable(t[1],t[2],t[3])
    else:
        t[0] = ColumnaTable(t[1],t[2],None)

# atributos de la columna
def p_atributo(t):
    '''

    atributo   : PRIMARY KEY
                | REFERENCES IDENT PARIZQ IDENT PARDER
                | NULL
                | NOT NULL
    '''
    if len(t)==3:
        t[0] = Atributo(t[1],None, None)
    elif len(t)==6:
        t[0] = Atributo(t[1],t[2],t[4])
    else:
        t[0] = Atributo(t[1],None,None)



# SINTAXIS PARA ALTER TABLE
def p_alter_table_instr(t) :
    ''' alter_instr     : ALTER TABLE IDENT ADD COLUMN IDENT tipodato PTCOMA
                        | ALTER TABLE IDENT DROP COLUMN IDENT PTCOMA
    '''
    if len(t) == 9:
        t[0] = AlterAgregar(t[3], t[6], t[7])
    else:
        t[0] = AlterDrop(t[3], t[6])                   

# SINTAXIS PARA TRUNCATE TABLE
def p_truncate_instr(t):
    'truncate_instr : TRUNCATE TABLE IDENT PTCOMA'
    t[0] = TruncateTable(t[3])

# SINTAXIS DROP TABLE
def p_drop_instr(t):
    '''drop_instr : DROP TABLE IDENT PTCOMA
    '''
    t[0] = DropTable(t[3])

# SINTAXIS CONCATENAR
def p_concater(t):
    '''concater : CONCATENA PARIZQ CADENA COMA CADENA PARDER '''
    t[0] = Concatena(t[3], t[5])

# SITAXIS SUBSTRAER
def p_substraer(t):
    '''subtrae : SUBSTRAER PARIZQ CADENA COMA ENTERO COMA ENTERO PARDER '''
    t[0] = Substraer(t[3], t[5], t[7])

# SINTAXIS PARA HOY
def p_hoy(t):
    '''hoyy : HOY PARIZQ PARDER'''
    t[0] = Hoy()

# SINTAXIS PARA CONTAR
def p_contar(t):
    '''contarr : CONTAR PARIZQ POR PARDER'''
    t[0] = Contar()

# SINTAXIS PARA SUMA
def p_suma(t):
    '''sumaa : SUMA PARIZQ IDENT PARDER
            | SUMA PARIZQ ENTERO PARDER'''
    t[0] = Suma(t[3])

# SINTAXIS PARA CAST
def p_cast(t):
    '''castt : CAST PARIZQ variable_operar AS tipodato PARDER '''
    t[0] = Cast(t[3], t[5])

def p_variable_operar(t):
    '''variable_operar : IDENT
                        | IDENTIFICADOR'''
    t[0] = t[1]
    
# SINTAXIS PARAUPDATE
def p_update_instr(t):
    '''update_instr : UPDATE IDENT SET expresiones WHERE expresiones PTCOMA
                    '''
    t[0] = UpdateTable(t[2], t[4], t[6])

# SINTAXIS PARA DELETE
def p_delete_instr(t):
    '''delete_instr : DELETE FROM IDENT WHERE expresiones PTCOMA
                    '''
    t[0] = DeleteTable(t[3], t[5])

# SINTAXIS PARA SELECT
def p_select(t):
    '''select_instr :   SELECT tablaselect FROM tablaselect PTCOMA 
                | SELECT tablaselect FROM tablaselect WHERE expresiones PTCOMA
    '''
    if len(t)==6:
        t[0] = SelectTable(t[2],t[4],None)
    else:
        t[0] = SelectTable(t[2],t[4],t[6])

def  p_tablaselect(t):
    '''tablaselect : tablaselect tablas
                    | tablas
    '''
    if len(t) == 3:
        t[0] = t[1]
        t[1].append(t[2])
    else:
        t[0] = [t[1]]

def p_tablas(t):
    '''tablas : POR
    | expresiones COMA
    | expresiones
    '''
    t[0] = t[1]

# SINTAXIS PARA INSERT
def p_insert(t):
    '''insert_instr : INSERT INTO IDENT VALUES PARIZQ tablaselect PARDER PTCOMA
                    | INSERT INTO IDENT PARIZQ tablaselect PARDER VALUES PARIZQ tablaselect PARDER PTCOMA
    '''
    if len(t)==9:
        t[0] = InsertTable(t[3],None,t[6])
    else:
        t[0] = InsertTable(t[3],t[5],t[9])

# SINTAXIS PARA DECLARACION DE VARIABLES
def p_declaracion(t):
    '''declaracionvariable : DECLARE IDENTIFICADOR tipodato PTCOMA
                            | DECLARE IDENTIFICADOR tipodato IGUALSIMPLE expresiones PTCOMA
    '''
    if len(t)==5:
        t[0] = DeclararVariable(t[2],t[3],None)
    else:
        t[0] = DeclararVariable(t[2],t[3],t[5])

# SINTAXIS PARA ASIGNACION DE VARIABLES
def p_asignacion(t):
    '''asignacionvariable : SET IDENTIFICADOR IGUALSIMPLE expresiones PTCOMA
    '''
    t[0] = AsignacionVariable(t[2],t[4])

# SINTAXIS PARA IF
def p_if(t):
    '''if_instr : IF PARIZQ expresiones PARDER instrucciones END PTCOMA '''
    t[0] = sslIf(t[3],t[5])

# SINTAXIS CREAR PROCEDURE 
def p_create_procedure(t):
    '''create_procedure : CREATE PROCEDURE IDENT PARIZQ listparam PARDER AS BEGIN instrucciones END PTCOMA
                        | CREATE PROCEDURE IDENT PARIZQ PARDER AS BEGIN instrucciones END PTCOMA
    '''
    if len(t)==12:
        t[0] = sslprocedure(t[3],t[5],t[9])
    else:
        t[0] = sslprocedure(t[3],None,t[8])

# SINTAXIS FUNCIONES
def p_funciones(t):
    ''' create_funcion : CREATE FUNCTION IDENT PARIZQ listparam PARDER RETURN tipodato AS BEGIN instrucciones END PTCOMA
                        | CREATE FUNCTION IDENT PARIZQ PARDER RETURN tipodato AS BEGIN instrucciones END PTCOMA
    '''
    if len(t)==14:
        t[0] = sslfunction(t[3],t[5],t[8],t[11])
    else:
        t[0] = sslfunction(t[3],None,t[7],t[10])

# SINTAXIS PARA PARAMETROS
def p_listparam(t):
    '''listparam : listparam param
                    | param
    '''
    if len(t)==3:
        t[0] = t[1]
        t[1].append(t[2])
    else:
        t[0] = [t[1]]

def p_param(t):
    '''param : IDENTIFICADOR tipodato COMA
               | IDENTIFICADOR tipodato 
    '''
    if len(t)==4:
        t[0] = Parametro(t[1],t[2])
    else:
        t[0] = Parametro(t[1],t[2])

# SINTAXIS PARA CASE
def p_case_instr(t):
    '''case_instr : CASE sentencias END PTCOMA'''
    t[0] = Case(t[2])

def p_sentencias(t):
    '''sentencias : sentencias sentencia
                    | sentencia
    '''
    if len(t)==3:
        t[0] = t[1]
        t[1].append(t[2])
    else:
        t[0] = [t[1]]

def p_sentencia(t):
    '''sentencia : WHEN expresiones THEN expresiones
                    | ELSE expresiones
    '''
    if len(t)==4:
        t[0] = Sentencia(t[1],t[2],t[3])
    else:
        t[0] = Sentencia(t[1],None,t[2])

# EXPRESIONES
def p_expresiones(t):
    '''expresiones : FECHAHORA
                    | FECHA
                    | expresiones AND expresiones
                    | expresiones OR expresiones
                    | expresiones IGUAL expresiones
                    | expresiones DIFERENTE expresiones
                    | expresiones MAYORQUE expresiones
                    | expresiones MENORQUE expresiones 
                    | expresiones MAYORIGUAL expresiones
                    | expresiones MENORIGUAL expresiones
                    | expresiones MAS expresiones
                    | expresiones MENOS expresiones
                    | expresiones POR expresiones
                    | expresiones DIVIDIDO expresiones
                    | PARIZQ expresiones PARDER
                    | NEGACION expresiones
                    | llaves
                    | ENTERO
                    | DECIMALES
                    | CADENA
                    | IDENTIFICADOR
                    | IDENT
                    | NULL
                    | func_sistema
                   
                '''
    if t[1] == '(':
        print("es parentesis")
        t[0] = t[2]
    elif len(t)==3:
        print("es negacion")
        t[0] = Expresion(t[2],t[1],None)
    elif len(t)==4: 
        
        print("es expresion")
        t[0] = Expresion(t[1],t[2],t[3])
    elif len(t)==2:
        t[0] = t[1]

def p_llaves(t):
    '''llaves : IDENT PUNTO IDENT'''
    t[0] = Llaves(t[2],t[1],t[3])
  
def p_func_sistema(t):
    '''func_sistema : contarr
                    | sumaa
                    | hoyy
                    | subtrae
                    | concater
                    | castt
    '''
    t[0] = t[1]

# SINTAXIS PARA RETORNAR
def p_retornarr(t):
    '''retornar : RETURN expresiones PTCOMA'''
    t[0] = Retornar(t[2])


def p_error(t):
    print(t)
    print("Error sintactico en '%s'" % t.value)





# Construyendo el analizador sintactico
import ply.yacc as yacc
parser = yacc.yacc()


input = """

CREATE FUNCTION Retornasuma(@ProductID int)
RETURN int
AS
BEGIN
    DECLARE @ret int;
    SELECT @ret == SUM(Cantidad) FROM inventario WHERE ProductoId == @ProductID; 

    IF (@ret == NULL)
        SET @ret = 0;
    END;

    RETURN @ret;
END;

CREATE PROCEDURE inicializacomisiones (@Ciudad varchar(30), @Departamento varchar(10))
AS
begin
    UPDATE tbcomision set comision == 0 where ciudad == @Ciudad;
    TRUNCATE TABLE tbreportecomisiones;
END;



"""

result = parser.parse(input.lower())
#print(result)

#recorrer la matriz y diccionario
for a in result:
    print(a)
    print("=====================================")
