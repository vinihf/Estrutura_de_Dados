from random import randint

def quickSort(lista):
    # Se a lista contém menos de dois elementos, 
    # retorna a própria lista
    if len(lista) < 2:
        return lista
    # Cria três listas
    menor, igual, maior = [], [], []
    # Seleciona o pivô aleatoriamente
    pivot = lista[randint(0, len(lista) - 1)]
    for item in lista:
        # Compara e adiciona os valores no array correspondente
        if item < pivot:
            menor.append(item)
        elif item == pivot:
            igual.append(item)
        elif item > pivot:
            maior.append(item)
    # No final combina os três arrays ordenados
    return quickSort(menor) + igual + quickSort(maior)

C = [10, 8, 7, 4, 3, 11, 13, 15, 10, 11, 1, 4, 7]
print(quickSort(C) )