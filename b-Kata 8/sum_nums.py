"""Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples (a, b) --> output (explanation)
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)"""

def get_sum(a, b):
    # Si a et b sont égaux, retourner n'importe lequel
    if a == b:
        return a  
    # Assurer que a est plus petit que b
    if a > b:
        a, b = b, a
    # Utiliser sum() pour calculer la somme des entiers entre a et b inclusivement
    return sum(range(a, b + 1))

def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))

def get_sum(a, b):
    return (a + b) * (abs(a - b) + 1) // 2

def get_sum(a,b):
    soma=0
    if a==b:
        return a
    elif a > b:
        for i in range(b,a+1):
            soma += i
        return soma
    else:
        for i in range(a,b+1):
            soma += i
        return soma