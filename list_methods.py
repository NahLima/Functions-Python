def count(iterable, x):
    """Return the number of times x appears in the list."""
    contagem = {}
    for x in iterable:
        if x in iterable:
            contagem[x] = contagem.get(x, 0) + 1
        else:
            contagem[x] = 1

    for x, value in contagem.items():
        if value > 1:
            print(str(x)+':'+str(value))


# lista = [2, 56, 2, 9, 8, 'B', 56, 56, 2, 56, 'a', 'a']
# print(count(lista, 0))


def clear(iterable):
    """Remove all items from the list. Equivalent to del a[:]."""
    for x in iterable:
        del(x)
    return []

# delete_list = ['B', 'amora', 'a', 'a', 1, 8, 60]
# print(clear(delete_list))


def sort(iterable):
    """Sort the items of the list in place
    (the arguments can be used for sort customization, see sorted()
    for their explanation)."""
    lista = []
    for x in range(0, len(iterable)):
        if x == 0 or x > lista[-1]:
            lista.append(x)
        else:
            pos = 0
            while pos < len(lista):
                if x <= lista[pos]:
                    lista.insert(pos, x)
                    break
                pos += 1
    return lista


teste = [5, 6, 9, 19, 21, 100, 56, 85]
print(sort(teste))


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
