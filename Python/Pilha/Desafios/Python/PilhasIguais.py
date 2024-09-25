from Classes import Stack

def main():
    pilha1 = Stack()
    pilha2 = Stack()

    pilha1.push(1)
    pilha1.push(2)
    pilha1.push(3)

    pilha2.push(1)
    pilha2.push(2)
    pilha2.push(2)

    diferentes = False

    if pilha1.getSize()!=pilha2.getSize():
        print("Pilhas não são iguais.")
    else:
        while pilha1.getSize()>0:
            if pilha1.pop()!=pilha2.pop():
                diferentes = True

    if diferentes:
        print("Pilhas não são iguais")
    else:
        print("Pilhas são iguais")

if __name__ == "__main__":
    main()
