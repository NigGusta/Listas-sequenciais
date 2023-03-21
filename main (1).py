class List:
    def __init__(lista):
        lista.items = []

    def vazia(lista):
        if len(lista.items) == 0:
           print("Lista vazia")

    def cheia(lista):
        # Como a lista em Python é dinâmica, ela não pode estar cheia
        # por definição. Então, vamos sempre retornar False.
        return False

    def tamanho(lista):
        return len(lista.items)

    def mostre(lista, index):
        return lista.items[index]

    def mude(lista, index, value):
        lista.items[index] = value

    def insira(lista, index, value):
        lista.items.insert(index, value)

    def remova(lista, index):
        return lista.items.pop(index)


def main():
    lst = List()

    print("Lista vazia:", lst.vazia())
    print("Tamanho da lista:", lst.tamanho())

    lst.insert(0, 11)
    lst.insert(1, 83)
    print("Elementos da lista:", [lst.mostre(i) for i in range(lst.tamanho())])

    lst.set(1, 21)
    print("Elementos da lista:", [lst.mostre(i) for i in range(lst.tamanho())])

    lst.remove(2)
    print("Elementos da lista:", [lst.mostre(i) for i in range(lst.tamanho())])
    
main()
