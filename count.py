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