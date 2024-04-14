"""Beginner - Lost Without a Map
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]"""

a =[1, 2, 3]

def maps(a):
    result = [ x * 2 for x in a]
    return result
print(maps(a))

def maps(a):
    return [2 * x for x in a]
"""Cette ligne utilise une compréhension de liste pour créer une nouvelle liste appelée result. La syntaxe de base est [expression for élément in séquence]"""

def maps(a):
    return map(lambda x:2*x, a)

def maps(a):
    num = []
    for i in a:
        num.append(i * 2)
    return num

def maps(a):
    return list(map(lambda s: s*2, a))