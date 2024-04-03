"""Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers."""

def count_sheep(n):
    if n <= 0:
        return ''
    else:
        n_list = list(range(1, n + 1))
        result = ''
        for num in n_list:
            result += str(num) + ' sheep...'
        return result

def count_sheep(n):
    sheep=""
    for i in range(1, n+1):
        sheep+=str(i) + " sheep..."
    return sheep



def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))

""" f string / format string, une f-string permet de créer des chaînes de caractères formatées de manière concise et lisible en incorporant des valeurs d'expressions Python dans la chaîne elle-même. """
name = "Alice"
age = 30
message = f"My name is {name} and I am {age} years old."
print(message)


def count_sheep(n):
    return "".join("{} sheep...".format(i) for i in range(1, n+1))

"{} est un placeholder dans la chaîne de formatage "{} sheep...". Lorsque vous utilisez format(i), cela insère la valeur de i dans le placeholder {}.

""""La compréhension de liste ( "{} sheep...".format(i) for i in range(1, n + 1)) crée une liste de chaînes de caractères en utilisant la méthode format() pour insérer chaque nombre i dans la chaîne "{} sheep...".

"".join() est utilisé pour concaténer toutes les chaînes de caractères de la liste ensemble en une seule grande chaîne, en utilisant "" (une chaîne vide) comme séparateur.""""