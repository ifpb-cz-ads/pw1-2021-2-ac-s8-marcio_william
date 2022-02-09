def validacao(frase,maximo, minimo):
    if len(frase) < maximo and len(frase) > minimo:
        return True
    else:
        return False


print(validacao("teste",10,1))
print(validacao("teste",20,10))
print(validacao("teste",4,1))
