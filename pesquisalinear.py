def pesquisa_linear(lista, elemento_desejado):
    for i in range(0,len(lista)):
        if lista[i] == elemento_desejado:
            return i
    return -1


def pesquisa_linear_in(lista, elemento_desejado):
    return elemento_desejado in lista


def pesquisa_linear_index(lista,elemento_desejado):
    try:
        return lista.index(elemento_desejado)
    except ValueError:
        return -1

teste = list(range(0,1000))

print(pesquisa_linear(teste,10011))
print(pesquisa_linear(teste,1))