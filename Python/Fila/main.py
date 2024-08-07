from Classes import Queue

fila = Queue()

print("Fila vazia")
print(fila)

fila.enqueue("A")
fila.enqueue("B")
fila.enqueue("C")
fila.enqueue("D")
fila.enqueue("E")

print("Fila cheia")
print(fila)

while fila.first != None:
    dado = fila.dequeue()
    print(f'Removendo elemento ({dado}) que está no começo da fila')
    print(fila)
    