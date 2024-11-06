from structlinks.DataStructures import BinarySearchTree

# Criando uma árvore a partir de uma lista
bst = BinarySearchTree.create_tree([1958,1962,1970,1994])

# Imprimindo a árvore
print(bst)

# Inserindo item na árvore
bst.insert(2002)

# Imprimindo a árvore
bst.display()

# Raiz da árvore
print(bst.root)

# Altura da árvore
print(bst.height)

# É balanceada?
print(bst.is_balanced)

# Contém item?
print(2022 in bst)

bst.insert(1990)

bst.display()

# Remove item
bst.remove(1994)

bst.display()