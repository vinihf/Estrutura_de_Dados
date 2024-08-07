class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]   

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0   

    def peek(self):
        if self.isEmpty():
            return None
        return self.head.next.value


    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return None
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

    def valida_expressao(expressao):
        pilha = Stack()
        for char in expressao:
            if char == '(':
                pilha.push(char)
            elif char == ')':
                if pilha.pop() is None:
                    return False
        return pilha.isEmpty()






