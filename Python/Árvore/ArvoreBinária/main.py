from Árvore.ArvoreBinária.BinarySearchTree import BinarySearchTree

def main():
    tree = BinarySearchTree(3)
    tree.insert_node(5)
    tree.insert_node(1)
    tree.insert_node(2)
    tree.in_order()

if __name__ == '__main__':
    main()