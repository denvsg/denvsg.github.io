from itertools import combinations_with_replacement, combinations
from itertools import product


def use_product():
    """笛卡尔积，以下两部分代码等同"""
    # code 1
    for i in range(1, 35):
        for j in range(1, 35):
            for k in range(1, 35):
                if i * i + j * j == k * k:
                    print(i, j, k)
    # code2
    for i, j, k in product(range(1, 35), repeat=3):
        if i * i + j * j == k * k:
            print(i, j, k)

    for i, j in product("abc", "12"):
        print(i, j)  # a1 a2 b1 b2 c1 c2

    for i, j, k in product("abc", "123", "xyz"):
        print(i, j, k)  # a1x a1y a1z a2x a2y a2z ...


def use_combinations_with_replacement():
    """可重复组合，以下两部分代码等同"""
    # code 1
    for i in range(1, 35):
        for j in range(i, 35):
            for k in range(j, 35):
                if i * i + j * j == k * k:
                    print(i, j, k)

    # code2
    for i, j, k in combinations_with_replacement(range(1, 35), 3):
        if i * i + j * j == k * k:
            print(i, j, k)

    for i, j in combinations_with_replacement("abcd", 2):
        print(i, j)  # aa ab ac ...

    for i, j, k in combinations_with_replacement("abc", 3):
        print(i, j, k)  # aaa aab aac abb abc  acc bbb bbc ccc


def use_combinations():
    """不重复组合，以下两部分代码等同"""
    lst = [3, 4, 5, 7, 8, 9, 12]
    aset = set(range(10, 30))

    # code 1
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            for k in range(j + 1, len(lst)):
                total = lst[i] + lst[j] + lst[k]
                if total in aset:
                    aset.remove(total)

    # code2
    for i, j, k in combinations(lst, 3):
        total = i + j + k
        if total in aset:
            aset.remove(total)

    print(aset)

    for i, j, k in combinations("abcd", 3):
        print(i, j, k)  # abc abd acd


for i, j, k in combinations_with_replacement("abcd", 3):
    print(i, j, k)
