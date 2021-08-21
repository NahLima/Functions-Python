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
