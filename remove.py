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