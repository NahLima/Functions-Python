def clear(iterable):
    """Remove all items from the list. Equivalent to del a[:]."""
    for x in iterable:
        del(x)
    return []

# delete_list = ['B', 'amora', 'a', 'a', 1, 8, 60]
# print(clear(delete_list))
