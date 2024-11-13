def bfs(grafo, inicio):
    visitados = set()  # Set dos nós visitados
    fila = [inicio]  # Lista para simular fila
    while fila:
        vertice_atual = fila.pop(0)  # Remove o vértice da fila
        if vertice_atual not in visitados:
            print(vertice_atual)  # Imprime o vértice atual
            visitados.add(vertice_atual)  # Marca o vértice como visitado
            # Adiciona os vizinhos do vértice atual à fila, se ainda não foram visitados
            for vizinho in grafo[vertice_atual]:
                if vizinho not in visitados:
                    fila.append(vizinho)