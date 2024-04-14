"""Grasshopper - Summation
Summation
Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0. Your function only needs to return the result, what is shown between parentheses in the example below is how you reach that result and it's not part of it, see the sample tests
For example (Input -> Output):

2 -> 3 (1 + 2)
8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)"""

def summation(num):
    total = 0
    for numbers in range(0 , num + 1 ):
         total += numbers
    return total


def summation(num):
    total = 0
    for i in range(0, num+1):
        total = total + i
    return total


def summation(num):
    return sum(range(1,num+1))

"""return num*(num+1)//2: Cette ligne calcule la somme des nombres de 1 à num en utilisant la formule de la somme des n premiers nombres entiers. Elle multiplie num par num + 1, puis divise le résultat par 2 en utilisant l'opérateur de division entière //. Cette formule est dérivée de la somme arithmétique des premiers nombres entiers.
num: représente la valeur de num spécifiée en entrée de la fonction."""

summation = lambda x: sum(range(1, x + 1))