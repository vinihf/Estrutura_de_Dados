def bubble_sort(dados):
    n = len(dados)

    for i in range(n):
        # Cria uma flag para fazer com o que o algoritmo pare antes no caso
        # de não existir nada para ordenar
        ordenado = True

        # Inicia analisando cada item da lista, um por um, 
        # comparando-o com seu valor adjacente. A cada iteração,
        # a parte da lista que analisa diminui porque os itens restantes já foram ordenados.

        for j in range(n - i - 1):
            if dados[j] > dados[j + 1]:
                # Se o item analisado é maior que o adjancente, realiza a troca
                dados[j], dados[j + 1] = dados[j + 1], dados[j]

                # Como foram necessárias alterações na lista
                # é preciso indicar que não está plenamente ordenado
                ordenado = False

        # Se não houver trocas durante a última iteração,
        # a lista já está ordenada e o algoritmo é encerrado

        if ordenado:
            break

    return dados

C = [10, 8, 7, 4, 3, 11, 13, 15, 10, 11, 1, 4, 7]
bubble_sort(C) 
print(C)