from structlinks.DataStructures import LinkedList

# Cria a lista
lst = LinkedList([1, 10, 3, 5])

# Imprime a lista
print(lst)  #  [1 -> 10 -> 3 -> 5]

# Tamanho da lista
length = len(lst)  # length = 4

# Adiciona item ao final
lst.append(2)  # [1 -> 10 -> 3 -> 5 -> 2]

# Adiciona na posição
lst.insert(0, 200)  # [200 -> 1 -> 10 -> 3 -> 5 -> 2]

# Busca e define valor
item = lst[1]  
lst[2] = 100  

# Remoção de elementos
# 1) por índice
popped = lst.pop(0)  # [1 -> 100 -> 3 -> 5 -> 2]
# 2) pelo valor do item
lst.remove(1) # [100 -> 3 -> 5 -> 2]

# Verifica se está na lista
cond1 = 2 in lst  # True
cond2 = 1 in lst  # False

# Inserção de listas
lst1 = LinkedList([1, 10, 3, 5])
lst2 = LinkedList([2, 100, 4, 0])
lst3 = lst1 + lst2  # [1 -> 10 -> 3 -> 5 -> 2 -> 100 -> 4 -> 0]

# Contagem de itens
count = lst.count(2)  

# Retorna a posição de um item (-1 se não estiver na lista)
index = lst.index(100)  
