def selectionSort(lista):
    for i in range(len(lista)):
        menor = i
        for j in range(i+1,len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        if lista[menor]!=lista[i]:
            aux = lista[menor]
            lista[menor] = lista[i]
            lista[i] = aux
    
C = [10, 8, 7, 4, 3, 11, 13, 15, 10, 11, 1, 4, 7] 
selectionSort(C)
print(C)