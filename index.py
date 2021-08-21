


teste = ['Guru', 'Siya', 'Tiya', 'Guru', 'Daksh', 'Riya', 'Guru'] 


def showIndex(iterable, x):
    position = []
    for key, value in enumerate(iterable):
        if value == x:
            return key 

print(showIndex(teste, 'Riya'))
