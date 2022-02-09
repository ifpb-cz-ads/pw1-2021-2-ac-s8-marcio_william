def pesquisar(lista, valor):
    return valor if valor in lista else None


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(pesquisar(lista,5))
print(pesquisar(lista,10))