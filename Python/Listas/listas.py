#Inicializa a lista vazia
lista = []

#Insere item
lista.append("2002")

#Insere no início
lista.insert(0,"1958")

#Insere em posição
lista.insert(1,"1962")

#Insere em posição
lista.insert(2,"1970")

#Insere em posição
lista.insert(3,"1994")

#Imprime lista
print(lista)

#Remove do final
ano = lista.pop()

print(lista)

#Remove do início
ano = lista.pop(0)

print(lista)


#Remove de posição
ano = lista.pop(1)

print(lista)