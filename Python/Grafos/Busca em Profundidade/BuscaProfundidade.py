def dfs(grafo, vertice):
    visitados = set()
    def dfs_recursiva(grafo, vertice):
        print(vertice)
        visitados.add(vertice)
        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                dfs_recursiva(grafo, vizinho)
    dfs_recursiva(grafo, vertice)

grafo = [ [1],           # Vizinhos do vértice 0.
          [2, 3],        # Vizinhos do vértice 1.
          [1, 4],        # Vizinhos do vértice 2.
          [0],           # Vizinhos do vértice 3.
          [1]            # Vizinhos do vértice 4.
        ]