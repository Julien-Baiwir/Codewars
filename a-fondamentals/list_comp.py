"""Exercice 1 : Générer une liste de carrés des nombres pairs de 1 à 10."""
list = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_square = [(x**2) for x in list if x % 2 == 0 ]

"""Exercice 2 : Créer une liste de tous les mots dans une chaîne de caractères qui ont une longueur supérieure à 3.
"""
list = ["ok", "vin", "manger", "boire"]
list_length =[x for x in list if len(x)>3]

"""Exercice 3 : À partir d'une liste de nombres, créer une liste de tous les nombres impairs et leur carré."""
list = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_square2 = [(x **2) for x in list if x % 2 != 0]

"""Créer une liste de tous les nombres premiers inférieurs à 50."""
primes = [x for x in range(2, 50) if all(x % y != 0 for y in range(2, int(x ** 0.5) + 1))]
"""print(primes)"""
"""La fonction all() en Python retourne True si tous les éléments d'une séquence sont évalués comme True, sinon elle retourne False"""
# Vérifier si tous les nombres dans une liste sont supérieurs à 5
numbers = [6, 7, 8, 9]
result = all(x > 5 for x in numbers)# Output: True
# Autre solution nombre premier
primes = []
for x in range(2, 50):
    is_prime = True
    for y in range(2, int(x ** 0.5) + 1):
        if x % y == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(x)
"""print(primes)"""


"""Exercice 5 : À partir d'une liste de chaînes de caractères, créer une liste de tous les mots qui commencent par une voyelle."""

my_list = ["ok", "vin", "manger", "boire", "image"]
vowels = "aeiou"
list_voyelle = [word for word in my_list if word[0].lower() in vowels]
"""print(list_voyelle)"""


"""Exercice 6 : Générer une liste de tous les tuples (x, y) où x est un chiffre de 1 à 3 et y est un chiffre de 4 à 6."""
list_tuples = [ (x , y) for x in range(1,4) for y in range(4, 7) ]
"""print(list_tuples)"""

"""Exercice 7 : À partir d'une liste de mots, créer une liste de tous les mots qui sont des palindromes."""
my_list = ["ok", "radar", "manger", "level", "image"]
plalindrome = [ word for word in my_list if word == word[::-1]]
print(plalindrome)

"""Exercice 8 : Créer une liste de tous les nombres pairs compris entre 1 et 100, qui sont également des carrés parfaits."""
even_perfect_squares = [x for x in range(1, 101) if x % 2 == 0 and int(x ** 0.5) ** 2 == x]
print(even_perfect_squares)