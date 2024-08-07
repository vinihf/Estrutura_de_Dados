class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next
    
    def __repr__(self):
        return '%s -> %s' % (self.value, self.next)

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0   

    def enqueue(self, value):
        new = Node(value)
        if self.first == None:
            self.first = new
            self.last =  new
        else:
            self.last.next = new
            self.last = new
        self.size+=1

    def dequeue(self):
        data = self.first.value
        self.first = self.first.next
        if self.first is None:
            self.last = None
        self.size-=1
        return data

    def __repr__(self):
        return "[" + str(self.first) + "]"



