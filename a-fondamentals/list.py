"""Ecrivez une fonction qui prend une liste en entrée et retourne la somme de tous ses éléments."""
list_num =[ 1, 3 , 4 , 2 , 7]
def sum_elem(list_num):
    return sum(list_num)
"""print(sum_elem(list_num))"""


"""Implémentez une fonction qui prend une liste de nombres et retourne une nouvelle liste contenant uniquement les nombres pairs."""
list_even =[ 1, 3 , 4 , 2 , 7]
def sort_even(list_even):
    return sorted([x for x in list_even if x % 2 == 0 ], reverse = True)
"""print(sort_even(list_even))"""


"""Créez une fonction qui prend deux listes en entrée et retourne une nouvelle liste contenant les éléments communs aux deux listes, sans doublons."""
list1 =[ 1, 3 , 8 , 2 , 7]
list2 =[ 1, 5 , 4 , 2 , 9]
def list_join(list1 , list2):
     common_list = []
     for x in list1:
             if x in list2 and x not in common_list:
                 common_list.append(x)
     return common_list
"""print(list_join(list1 , list2))"""

"""autre possibilité en utilisant les set"""
def list_join2(list1, list2):
    return list(set(list1) & set(list2))
list1 = [1, 3, 8, 2, 7]
list2 = [1, 5, 4, 2, 9]
"""print(list_join2(list1, list2))"""



"""Écrivez une fonction qui prend une liste de mots en entrée et retourne une nouvelle liste contenant la longueur de chaque mot."""
list_word =[ "ok", "bonjour", "oui"]
def sort_even(list_word):
    return [ len(x) for x in list_word ]
"""print(sort_even(list_word))"""



"""Implémentez une fonction qui prend une liste de nombres en entrée et retourne la liste des nombres triés par ordre croissant, en utilisant l'algorithme de tri à bulles."""
list_bulles =[ 1, 3 , 4 , 2 , 7]
def sort_bull(list_bulles):
    return sorted(list_bulles)
"""print(sort_bull(list_bulles))"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Le dernier i éléments sont déjà triés, donc on les ignore
        for j in range(0, n-i-1):
            # Parcourez la liste de 0 à n-i-1
            # Échangez si l'élément trouvé est plus grand que le suivant
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Exemple d'utilisation :
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
"""print("Liste triée:", my_list)"""



"""Créez une fonction qui prend une liste de chaînes de caractères en entrée et retourne une nouvelle liste contenant uniquement les chaînes de caractères qui sont des palindromes."""
mypal = ["ok", "radar", "john", "level"]
def sort_pal(mypal):
    return [word for word in mypal if word == word[::-1]]
"""print(sort_pal(mypal))"""

word = "hello"
"""print (word[::1])"""
"""Dans l'expression word[::1], le premier double deux-points : indique le début du slicing, le deuxième double deux-points : indique la fin du slicing, et le nombre 1 indique le pas (step)."""



"""Écrivez un programme qui prend une liste de nombres en entrée et retourne la moyenne des nombres."""
list_moy =[ 1, 3 , 4 , 2 , 7]
def sort_moy(list_moy):
    return round(sum(list_moy) / len(list_moy))
"""print(sort_moy(list_moy))"""


"""Implémentez une fonction qui prend une liste de nombres en entrée et retourne une nouvelle liste où chaque élément est élevé au carré."""
list_car =[ 1, 3 , 4 , 2 , 7]
def sort_car(list_moy):
    return [x**2 for x in list_car]
"""print(sort_car(list_car))"""


"""Créez une fonction qui prend une liste de chaînes de caractères en entrée et retourne la liste des chaînes de caractères triées par longueur, du plus court au plus long."""
phrase = ["ok", "radar", "devastated", "john"]
def sort_phrase (phrase):
    return sorted(phrase, key= lambda x: len(x))  
"""return sorted(phrase, key=len)   fonctionne aussi"""
print(sort_phrase (phrase ))


"""Écrivez un programme qui prend une liste de nombres en entrée et retourne une nouvelle liste contenant uniquement les nombres uniques, c'est-à-dire sans doublons."""
list_u =[ 1, 1, 3, 3, 2, 3 , 4 , 2, 2 , 7]
def sort_u(list_u):
    new_list= []
    for x in list_u:
        if x not in new_list:
            new_list.append(x)
    return new_list
    
print(sort_u(list_u))