def dfs(grafo, inicio, visitados=None):
    if visitados is None:
        visitados = set()  # Set para rastrear os vértices visitados
    visitados.add(inicio)  # Marca o vértice atual como visitado

    print(inicio)  # Imprime o vértice atual
    # Para cada vizinho do vértice atual
    for vizinho in grafo[inicio]:
        if vizinho not in visitados:  # Se o vizinho não foi visitado
            dfs(grafo, vizinho, visitados)  # Chama a algoritmo recursivamente
    return visitados
