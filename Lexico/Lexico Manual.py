class lexico:
    def __init__(self):
        self.tokens=[]
        
    def recibirTokens(self,lista):
        self.tokens = lista

    def evaluarTokens(self, lexema):
        for caracter in lexema:
            estado=False
            print(caracter)
            for token in self.tokens:
                if caracter==token:
                    estado=True
                    break
            if estado==False:
                break
        return estado

    def evaluarLexema(self, lista):
        if lex.evaluarTokens(lista):
            print("No hubo fallos")
        else:
            print("Error")

def leerArchivo(archivo):
    return[x.split() for x in open(archivo).readlines()]
                
lista = "ab"
tokens = ["a","b","c","d"]
lex=lexico()
lex.recibirTokens(tokens)
lex.evaluarLexema(lista)

lista = "abcdacda"
lex.evaluarLexema(lista)        
        
lista = "abcdacdxa"
lex.evaluarLexema(lista)
