""""Messi goals function
Messi is a soccer player with goals in three leagues:

LaLiga
Copa del Rey
Champions
Complete the function to return his total number of goals in all three leagues.

Note: the input will always be valid.

For example:
5, 10, 2  -->  17
"""
def goals(laLiga, copaDelRey, championsLeague):
    list =[laLiga, copaDelRey, championsLeague]
    return sum(list)
print(goals(5, 10, 2))



def goals(laLiga, copaDelRey, championsLeague):
    return laLiga+copaDelRey+championsLeague

def goals(*a):
    return sum(a)
"""Dans cette fonction goals, l'utilisation de *a dans la signature de la fonction est une technique appelée "empaquetage des arguments". Cela permet à la fonction de prendre un nombre variable d'arguments positionnels et de les regrouper dans un seul paramètre a, qui est traité comme un tuple.
Cette approche est très flexible car elle vous permet de passer un nombre variable d'arguments à la fonction sans avoir à spécifier à l'avance combien il y en aura."""


goals = lambda a,b,c: a + b + c