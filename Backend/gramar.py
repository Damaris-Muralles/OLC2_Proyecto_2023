
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
    'table' : 'TABLE',
    'declare' : 'DECLARE',
    'add'  : 'ADD', 
    'set' : 'SET',
    'exc' : 'EXC',
    'begin' : 'BEGIN',
    'from' : 'FROM',
    'where' : 'WHERE',
    'end' : 'END',
    'as' : 'AS',
    'key' : 'KEY',
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
    'PTCOMA',
    
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

# Expresiones regulares
def t_FECHAHORA(t):
    r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}'
    return t

def t_FECHA(t):
    r'\d{4}-\d{2}-\d{2}'
    return t

def t_DECIMALES(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Floaat value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_IDENTIFICADOR(t):
    r'[@]([a-zA-ZÑñ]|("_"[a-zA-ZÑñ]))([a-zA-ZÑñ]|[0-9]|"_")*'
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
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Construyendo el analizador lexico
import ply.lex as lex
lexer = lex.lex()


# prueba del analizador lexico
'''
data="""if 1 == 1
end
+
intol
database"""
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok: break
    print(tok)
'''


# Asociación de operadores y precedencia
"""
precedence = (
    ('left','CONCAT'),
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO'),
    ('right','UMENOS'),
    )"""

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
        t[0] = AlterDrop (t[3], t[6])                   

# SINTAXIS PARA TRUNCATE
def p_truncate_instr(t):
    'truncate_instr : TRUNCATE TABLE IDENT PTCOMA'
    t[0] = TruncateTable(t[3])

# SINTAXIS DROP

def p_drop_instr(t):
    '''drop_instr : DROP TABLE IDENT PTCOMA
    '''
    t[0] = DropTable(t[3])



def p_error(t):
    print(t)
    print("Error sintactico en '%s'" % t.value)





# Construyendo el analizador sintactico
import ply.yacc as yacc
parser = yacc.yacc()


input = """CREATE TABLE products (
 productno int,
 name varchar,
 price decimal(8,2)
);

CREATE TABLE tbfactura (
Idfactura int PRIMARY KEY,
Fechafactura date not null,
Nit varchar not null,
Nombrecliente varchar(50) not null,
Referencia varchar(10)
);

Alter table tbfactura add column formapago int;
Alter table tbfactura add column tipotarjeta int;

Truncate table tbfactura;
Truncate table tbdetallefactura;

Alter table tbfactura drop column tipotarjeta;

DROP TABLE tbproducts;

"""

result = parser.parse(input.lower())
#print(result)

#recorrer la matriz y diccionario
for a in result:
    print(a)
    print("=====================================")
