def insertionSort(lista):
    # Loop do segundo elemento da matriz até o último elemento
    for i in range(1, len(lista)):
        # Este é o elemento que queremos posicionar corretamente
        chave = lista[i]
        # Inicializa a variável que será usada para achar a posição correta
        # do elemento referenciado em chave
        j = i - 1
        # Percorra a lista de itens (a parte esquerda da matriz) 
        # e encontre a posição correta do elemento referenciado como chave. 
        # Faça isso apenas se a chave for menor que seus valores adjacentes.
        while j >= 0 and lista[j] > chave:
            # Desloque o valor uma posição para a esquerda e reposicione j 
            # para apontar para o próximo elemento (da direita para a esquerda)
            lista[j + 1] = lista[j]
            j -= 1
        # Quando você terminar de mudar os elementos, 
        # você pode posicionar a chave em seu local correto
        lista[j + 1] = chave
    return lista

C = [10, 8, 7, 4, 3, 11, 13, 15, 10, 11, 1, 4, 7]
insertionSort(C) 
print(C)