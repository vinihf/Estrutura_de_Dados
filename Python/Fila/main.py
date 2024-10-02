from Classes import Fila, FilaCircular


def mainSimples():
    fila = Fila()

    fila.enqueue("A")
    fila.enqueue("B")
    fila.enqueue("C")
    fila.enqueue("D")
    fila.enqueue("E")

    print(fila)

    while fila.isEmpty()!=True:
        dado = fila.dequeue()
        print(f'Removendo elemento ({dado}) que está no começo da fila')

def mainCircular():
    fila = FilaCircular(4)
    fila.enqueue(6)
    fila.enqueue(2)
    fila.enqueue(5)
    fila.enqueue(7)
    fila.dequeue()
    fila.dequeue()
    fila.enqueue(1)
    fila.enqueue(2)
    fila.dequeue()
    fila.dequeue()


if __name__ == "__main__":
    mainCircular()  