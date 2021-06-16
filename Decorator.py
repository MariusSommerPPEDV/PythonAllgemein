import time


def decoration(func):
    def wrapper(*kwargs):
        print("Hier passiert was vor der Funktion.")
        return func(*kwargs)
        print("Hier passiert was nach der Funktion.")
    return wrapper


def zweimal(func):
    def wrapper(*kwargs):
        return func(*kwargs), func(*kwargs)
        print("Funktion wurde erfolgreich zweimal ausgeführt")
    return wrapper


@zweimal
@decoration
def test_func(x):
    return x + 25


x,y = test_func(12)
print(x,y)


def add_one(list):
    new_list = list.copy()
    for i in range(len(list)):
        new_list[i] += 1
    return new_list


def add_two(list):
    new_list = list.copy()
    for i in range(len(list)):
        new_list[i] += 2
    return new_list


def test_ho(list, func):
    new_list = list.copy()
    for i in range(len(list)):
        new_list[i] = func(list[i])
    return new_list


test_list = list(range(0, 101))
text_list = ["Hallo", "Mein", "Name", "Ist", "Marius"]
x = add_one(test_list)
y = add_two(test_list)
z = test_ho(test_list, lambda x: x+2)
z = test_ho(test_list, lambda x: x-20)
txet_tsil = test_ho(text_list, lambda s: s[::-1])
print(txet_tsil)
print(x)
print(y)
print(z)
print(tuple(filter(lambda x: len(x) < 2, text_list)))