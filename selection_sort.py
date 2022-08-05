def selectionSort(lista):
    # Laço externo
    for i in range(len(lista)):
        # Incializa o elemento menor com a posição atual do índice externo
        menor = i
        # Percorre a lista a partir do índice externo + 1
        for j in range(i+1,len(lista)):
            # Se o item da lista for menor que a posição inicial
            if lista[j] < lista[menor]:
                # Passa a ser o menor
                menor = j
        # Se não for o mesmo elemento
        if lista[menor]!=lista[i]:
            # Realiza a troca
            aux = lista[menor]
            lista[menor] = lista[i]
            lista[i] = aux
C = [10, 8, 7, 4, 3, 11, 13, 15, 10, 11, 1, 4, 7] 
selectionSort(C)
print(C)