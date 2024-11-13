from BuscaProfundidade import dfs
from BuscaLargura import bfs

def main():
    grafo = { "0" : ["1"],
              "1" : ["2", "3"],
              "2" : ["1", "4"],
              "3" : ["0"],
              "4" : ["1"]
            }

    #Iterar sobre os vértices de um grafo
    print("Imprime vértices")
    for v in grafo:
        print(v)

    #Iterar sobre os vizinhos de um vértice
    print("Imprime vizinhos do vértice")
    for v in grafo:
        for u in grafo[v]:
            print(f'{v}:{u}')

    print("Imprime Busca em Profundidade")
    dfs(grafo,"0")

    print("Imprime Busca em Largura")
    bfs(grafo, "0")

if __name__ == "__main__":
    main()