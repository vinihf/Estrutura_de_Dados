class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self):
        self.first = None
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0   

    def insere(self, value):
        new_node = Node(value)
        if self.first == None:
            self.first = new_node
        else:
            aux = Node(self.first)
            while aux.next!=None:
                aux = aux.next
            aux.next = new_node
        self.size+=1

    def remove(self):
        assert self.first != None, "Impossível remover elemento de fila vazia."
        dado = self.first
        self.first = self.first.next
        self.size-=1
        if self.first == None:
            self.last = None
        return dado



