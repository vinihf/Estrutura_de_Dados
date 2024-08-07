from structlinks.DataStructures import DoublyLinkedList

# Cria a lista
lst = DoublyLinkedList([1, 10, 3, 5])

# Imprime a lista
print(lst)  # [1 <--> 10 <--> 3 <--> 5]

# Tamanho da lista
length = len(lst)  # length = 4

# Adiciona item ao final
lst.append(2)  # lst = [1 <--> 10 <--> 3 <--> 5 <--> 2]

# Adiciona item em posição
lst.insert(0, 200)  # lst = [200 <--> 1 <--> 10 <--> 3 <--> 5 <--> 2]

# Busca e atualização
item = lst[1]  
lst[2] = 100  


# Remove item
# 1) por índice
popped = lst.pop(0)  # lst = [1 <--> 100 <--> 3 <--> 5 <--> 2]
# 2) por valor
lst.remove(1) # lst = [100 <--> 3 <--> 5 <--> 2]

# Pesquisando elemento
cond1 = 2 in lst  # True
cond2 = 1 in lst  # False

# Conta itens
count = lst.count(2)

# Índice de um item
index = lst.index(100)

