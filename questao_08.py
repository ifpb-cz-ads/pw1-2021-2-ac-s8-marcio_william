def comparar(palavra, palavras):
    if palavra in palavras:
        return True
    else:
        return False

palavras = ['a','b','c','d','e']
print(comparar('a',palavras))
print(comparar('z',palavras))
