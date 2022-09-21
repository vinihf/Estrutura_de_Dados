def pesquisa_binaria_recursiva(lista, esquerda, direita, item):
    # 1. Caso base: o elemento não está presente. 
    if direita < esquerda:
        return -1
    meio = (esquerda + direita) // 2
    # 2. Nosso palpite estava certo: o elemento está no meio do arranjo. 
    if lista[meio] == item:
        return meio
    # 3. O palpite estava errado: atualizamos os limites e continuamos a busca. 
    elif lista[meio] > item:
        return pesquisa_binaria_recursiva(lista, esquerda, meio - 1, item)
    else: # A[meio] < item
        return pesquisa_binaria_recursiva(lista, meio + 1, direita, item)

def pesquisa_binaria(lista, item):
    """Implementa pesquisa binária iterativamente."""
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == item:
            return meio
        elif lista[meio] > item:
            direita = meio - 1
        else: # A[meio] < item
            esquerda = meio + 1
    return -1

teste = [0, 10, 20, 30, 40, 50, 60, 70]

print(pesquisa_binaria(teste,20))
print(pesquisa_binaria(teste,700))