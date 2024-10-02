class Fila:
    def __init__(self):
        self.fila = []

    def __str__(self):
        text = ""
        for item in self.fila:
            text += str(item) + " -> "
        return text.strip(" -> ")

    def isEmpty(self):
        return len(self.fila) == 0

    def enqueue(self, item):
        self.fila.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.fila.pop(0)
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.fila[0]
        else:
            return None










class FilaCircular:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.fila = [None] * tamanho
        self.frente = -1
        self.cauda = -1

    def isFull(self):
        return (self.cauda + 1) % self.tamanho == self.frente

    def isEmpty(self):
        return self.frente == -1

    def enqueue(self, item):
        if self.isFull():
            print("Fila está cheia")
        else:
            if self.frente == -1:
                self.frente = 0
            self.cauda = (self.cauda + 1) % self.tamanho
            self.fila[self.cauda] = item
            print(f'Enqueue: {item} Frente: {self.frente}  Cauda: {self.cauda}')

    def dequeue(self):
        if self.isEmpty():
            print("Fila está vazia")
        else:
            data = self.fila[self.frente]
            if self.frente == self.cauda:
                self.frente = -1
                self.cauda = -1
            else:
                self.frente = (self.frente + 1) % self.tamanho
            print(f'Dequeue: {data} Frente: {self.frente}  Cauda: {self.cauda}')
            return data
