import lex

tokens = ["a","b","c","d"]

t_a = r'a'
t_b = r'b'
t_c = r'c'
t_d = r'd'


# Error handling rule
def t_error(t):
    print("Hay un caracter no valido")
    t.lexer.skip(1)

lex.lex() # Build the lexer

lex.input("abcx")
while True:
    tok = lex.token()
    if not tok: break
    print (str(tok.value))
