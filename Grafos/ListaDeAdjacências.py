grafo = { "0" : ["1"],
          "1" : ["2", "3"],
          "2" : ["1", "4"],
          "3" : ["0"],
          "4" : ["1"]
        }

#Iterar sobre os vértices de um grafo
for v in grafo:
    print(v)

#Iterar sobre os vizinhos de um vértice
for v in grafo:
    for u in grafo[v]:
        print(f'{v}:{u}')