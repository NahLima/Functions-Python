newList = []


def copia(iterable):
    for x in iterable:
        newList.append(x)
    return("nova lista: " + str(newList))


teste = [15, 1, "a", 75, 7, 9, 10]

print(copia(teste))
