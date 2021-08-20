def count(iterable, x):
    """Return the number of times x appears in the list."""
    contagem = {}
    for x in iterable:
        if x in iterable:
            contagem[x] = contagem.get(x, 0) + 1
        else:
            contagem[x] = 1

    return contagem


lista = [2, 56, 2, 9, 8, 'B', 56, 56, 2, 56, 'a', 'a']
print(count(lista, 0))


def clear(iterable):
    """Remove all items from the list. Equivalent to del a[:]."""
    for x in iterable:
        del(x)
    return []

# delete_list = ['B', 'amora', 'a', 'a', 1, 8, 60]
# print(clear(delete_list))


def ordenation(iterable):
    """Sort the items of the list in place
    (the arguments can be used for sort customization, see sorted()
    for their explanation)."""
    if len(iterable) < 1:
        return iterable  # caso base
    else:
        pivot = iterable[0]  # caso recursivo
        # sublista com os numeros menores
        smaller = [i for i in iterable[1:] if i <= pivot]
        # sublista com os numeros maiores
        greater = [i for i in iterable[1:] if i > pivot]
        # concatenação
        return ordenation(smaller) + [pivot] + ordenation(greater)


teste = [5, 6, 9, 19, 21, 100, 56, 85]
teste2 = ["a", "z", "f", "m", "n"]
teste3 = ["cachoro", "dog", "girafa", "zebra", "amora"]
teste4 = ["A", "z", "a", "D"]  # ele retorna a ordem por maiuscula e
# depois minuscula

# print(ordenation(teste))
# print(ordenation(teste2))
# print(ordenation(teste3))
# print(ordenation(teste4))


def remove(iterable, x):
    """Remove the first item from the list whose value is equal to x. It raises
    a ValueError if there is no such item."""

    position = None
    for key, value in enumerate(iterable):
        if value == x:
            position = key
            break
    del iterable[position]
    return iterable


# lista = [1,4,8,10,15]
# remove(lista,10)
# print(lista)


#teste novo git push
