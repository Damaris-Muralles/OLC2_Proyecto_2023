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
    r'([a-zA-ZÑñ]|("_"[a-zA-ZÑñ]))([a-zA-ZÑñ]|[0-9]|"_")*'
    return t

# Caracteres ignorados
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()




import ply.yacc as yacc
parser = yacc.yacc()

def parse(input) :
    global lexer
    input = input.replace("\r","")
    lexer = lex.lex()
    return parser.parse(input)


