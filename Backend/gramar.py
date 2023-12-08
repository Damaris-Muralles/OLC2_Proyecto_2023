
# Lista de palabras reservadas
reservadas = {
    'usar' : 'USAR',
    'create' : 'CREATE',
    'database' : 'DATABASE',
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
""" # reservadas
    'USAR',
    'CREATE',
    'DATABASE',
    'ALTER',
    'TABLE',
    'DROP',
    'TRUNCATE',
    'SELECT',
    'UPDATE',
    'DELETE',
    'INSERT',
    'FUNCTION',
    'PROCEDURE',
    'DECLARE',
    'ADD',
    'SET',
    'EXC',
    'BEGIN',
    'FROM',
    'WHERE',
    'END',
    'CASE',
    'CAST',
    'SUMA',
    'CONTAR',
    'IF',
    'AS',
    'RETURN',
    'KEY',
    'PRIMARY',
    'FOREIGN',
    'REFERENCES',
    'NULL',
    'NOT',
    'NVARCHAR',
    'NCHAR',
    'INT',
    'DECIMAL',
    'BIT',
    'DATE',
    'DATETIME',
    'CONCATENA',
    'HOY',
    'SUBSTRAER',
"""
   

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
"""
t_USAR      = r'usar'
t_CREATE    = r'create'
t_DATABASE  = r'database'
t_ALTER     = r'alter'
t_TABLE     = r'table'
t_DROP      = r'drop'
t_TRUNCATE  = r'truncate'
t_SELECT    = r'select'
t_UPDATE    = r'update'
t_DELETE    = r'delete'
t_INSERT    = r'insert'
t_FUNCTION  = r'function'
t_PROCEDURE = r'procedure'
t_DECLARE   = r'declare'
t_ADD       = r'add'
t_SET       = r'set'
t_EXC       = r'exc'
t_BEGIN     = r'begin'
t_FROM      = r'from'
t_WHERE     = r'where'
t_END       = r'end'
t_CASE      = r'case'
t_CAST      = r'cast'
t_SUMA      = r'suma'
t_CONTAR    = r'contar'
t_IF        = r'if'
t_AS        = r'as'
t_RETURN    = r'return'
t_KEY       = r'key'
t_PRIMARY   = r'primary'
t_FOREIGN   = r'foreing'
t_REFERENCES= r'references'
t_NULL      = r'null'
t_NOT       = r'not'
t_NVARCHAR  = r'nvarchar'
t_NCHAR     = r'nchar'
t_INT       = r'int'
t_DECIMAL   = r'decimal'
t_BIT       = r'bit'
t_DATE      = r'date'
t_DATETIME  = r'datetime'
t_CONCATENA = r'concatena'
t_HOY       = r'hoy'
t_SUBSTRAER = r'substraer'
"""
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
precedence = (
    ('left','CONCAT'),
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO'),
    ('right','UMENOS'),
    )

import instrucciones as instruccionApi


def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t) :
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    t[0] = [t[1]]
    

def p_instruccion(t) :
    '''instruccion      : create_instr
                        | alter_instr
                        | drop_instr
                        | truncate_instr
                        | select_instr
                        | update_instr
                        | delete_instr
                        | insert_instr
                        | use_instr
                    '''
    t[0] = t[1]

def p_select_instr(t) :
    'select_instr     : SELECT listacampos FROM listatablas PTCOMA'
    t[0] = instruccionApi.Select(t[2], t[4], None)
def p_select_instr_where(t) :
    'select_instr     : SELECT listacampos FROM listatablas WHERE condiciones PTCOMA'
    
    t[0] = instruccionApi.Select(t[2], t[4], t[6])

def p_listacampos(t) :
    'listacampos      : listacampos COMA campo'
    t[1].append(t[3])
    t[0] = t[1]
def p_listacampos_campo(t) :
    'listacampos      : campo'
    t[0] = [t[1]]
    
def p_campo(t) :
    '''campo            : IDENTIFICADOR'''
    t[0] = t[1]

def p_listatablas(t) :
    'listatablas      : listatablas COMA tablas'
    t[1].append(t[3])
    t[0] = t[1]
def p_listatablas_tablas(t) :
    'listatablas      : tablas'
    t[0] = [t[1]]
def p_tablas(t) :
    '''tablas           : IDENTIFICADOR'''
    t[0] = t[1]


def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()


def parse(input) :
    return parser.parse(input)