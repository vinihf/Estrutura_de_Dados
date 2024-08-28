def mergeSort_Netflix(lista):
    if len(lista) > 1:
        # Identifica o elemento do meio
        meio = len(lista)//2
        # Divide a lista em duas partes a partir do meio
        listaDaEsquerda = lista[:meio]
        listaDaDireita = lista[meio:]
        # Invoca recursivamente a função para ordenar cada parte da lista
        mergeSort_Netflix(listaDaEsquerda)
        mergeSort_Netflix(listaDaDireita)
        i = 0
        j = 0
        k = 0
        while i < len(listaDaEsquerda) and j < len(listaDaDireita):
            # Insere na nova lista ordenada o menor elemento das duas
            if listaDaEsquerda[i][1] < listaDaDireita[j][1]:
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

def pesquisa_binaria_recursiva_netflix(lista, esquerda, direita, item):
    # 1. Caso base: o elemento não está presente.
    if direita < esquerda:
        return -1
    meio = (esquerda + direita) // 2
    # 2. Nosso palpite estava certo: o elemento está no meio do arranjo.
    if lista[meio][1] == item:
        return meio
    # 3. O palpite estava errado: atualizamos os limites e continuamos a busca.
    elif lista[meio][1] > item:
        return pesquisa_binaria_recursiva_netflix(lista, esquerda, meio - 1, item)
    else: # A[meio] < item
        return pesquisa_binaria_recursiva_netflix(lista, meio + 1, direita, item)


itens = []
with open ("netflix_titles.csv", 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        itens.append(linha.split(";"))

mergeSort_Netflix(itens)

print(f'O filme mais antigo é: {itens[0][1]} de {itens[0][4]}')
print(f'O filme mais anovo é: {itens[-2][1]} {itens[-2][4]}')

titulo_pesquisa = input("Informe o nome do filme?")
if pesquisa_binaria_recursiva_netflix(itens,0,len(itens)-1,titulo_pesquisa) == -1:
    print("Não existe o filme")
else:
    print("Existe")