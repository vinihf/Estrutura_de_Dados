from Grafo import Grafo

# Cria a lista de arestas.
arestas = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'B'), ('C', 'E'), ('D', 'A'), ('E', 'B')]

# Cria e imprime o grafo.
grafo = Grafo(arestas, direcionado=True)
print(grafo.adj)

#Imprime vértices
print(grafo.get_vertices())

#Imprime arestas
print(grafo.get_arestas())

#Imprime verificação se há caminho
print(grafo.existe_aresta('A', 'B'), grafo.existe_aresta('E', 'C'))
