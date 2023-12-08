import ply.lex as lex
import ply.yacc as yacc

# Lista de palabras reservadas
reservadas = {
    'usar' : 'USAR',
    'create' : 'CREATE',
    'data base' : 'DATABASE',
    'alter' : 'ALTER',
    'table' : 'TABLE',
    'drop' : 'DROP',
    'truncate' : 'TRUNCATE',
    'select' : 'SELECT',
    'update' : 'UPDATE',
    'delete' : 'DELETE',
    'insert' : 'INSERT',
    'function' : 'FUNCTION',    
    'procedure' : 'PROCEDURE',
    'declare' : 'DECLARE',
    'add'  : 'ADD', 
    'set' : 'SET',
    'exc' : 'EXC',
    'begin' : 'BEGIN',
    'from' : 'FROM',
    'where' : 'WHERE',
    'end' : 'END',
    'case' : 'CASE',
    'cast' : 'CAST',
    'suma' : 'SUMA',
    'contar' : 'CONTAR',
    'if' : 'IF',
    'as' : 'AS',
    'return' : 'RETURN',
    'key' : 'KEY',
    'primary' : 'PRIMARY',
    'foreing' : 'FOREIGN',
    'references' : 'REFERENCES',
    'null' : 'NULL',
    'not' : 'NOT',
    'nvarchar' : 'NVARCHAR',
    'nchar' : 'NCHAR',
    'int' : 'INT',
    'decimal' : 'DECIMAL',
    'bit' : 'BIT',
    'date' : 'DATE',
    'datetime' : 'DATETIME',
    'concatena' : 'CONCATENA',
    'hoy' : 'HOY',
    'substraer' : 'SUBSTRAER',
}

tokens  = [ 
    'PARIZQ',
    'PARDER',
    'COMA',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'ENTERO',
    'DECIMALES',
    'PTCOMA',
    'AND',
    'OR',
    'NEGACION',
    'IGUAL',
    'DIFERENTE',
    'MAYORQUE',
    'MENORQUE',
    'MAYORIGUAL',
    'MENORIGUAL',
    'IDENTIFICADOR',
    'CADENA',
    'FECHA',
    'FECHAHORA',
    'IDENT',
] + list(reservadas.values())

# Expresiones regulares para tokens simples
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

# Definición de las funciones para los tokens más complejos
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
    t.value = t.value[1:-1]  # Remover las comillas
    return t

def t_IDENT(t):
    r'([a-zA-ZÑñ]|("_"[a-zA-ZÑñ]))([a-zA-ZÑñ]|[0-9]|"_")*'
    return t

# Caracteres ignorados
t_ignore = " \t"

# Nueva línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Error léxico
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()

# Asociación de operadores y precedencia
precedence = (
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO'),
    ('right','UMENOS'),
)


def p_instrucciones_lista(t):
    '''instrucciones : instruccion instrucciones
                     | instruccion'''


def p_instruccion_crear(t):
    '''instruccion : crear'''

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)


import ply.yacc as yacc
parser = yacc.yacc()

f = open("./entrada.txt", "r")
input = f.read()
print(input)
parser.parse(input)
