def mergeSort(lista):
    if len(lista) > 1:
        # Identifica o elemento do meio
        meio = len(lista)//2
        # Divide a lista em duas partes a partir do meio
        listaDaEsquerda = lista[:meio]
        listaDaDireita = lista[meio:]
        # Invoca recursivamente a função para ordenar cada parte da lista
        mergeSort(listaDaEsquerda)
        mergeSort(listaDaDireita)
        i = 0
        j = 0
        k = 0
        while i < len(listaDaEsquerda) and j < len(listaDaDireita):
            # Insere na nova lista ordenada o menor elemento das duas
            if listaDaEsquerda[i] > listaDaDireita[j]:
                lista[k]=listaDaEsquerda[i]
                # Incrementa o índice da lista da esquerda
                i += 1
            else:
                lista[k]=listaDaDireita[j]
                # Incrementa o índice da lista da direita
                j += 1
            # Incrementa o índice da lista final
            k += 1
        # Caso restem elementos
        while i < len(listaDaEsquerda):
            lista[k]=listaDaEsquerda[i]
            i += 1
            k += 1
        while j < len(listaDaDireita):
            lista[k]=listaDaDireita[j]
            j += 1
            k += 1
    return lista

C = [10, 8, 7, 4, 3, 11, 13, 15, 10, 11, 1, 4, 7]
mergeSort(C) 
print(C)