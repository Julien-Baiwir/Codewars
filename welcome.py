"""The Task
Think of a way to store the languages as a database. The languages are listed below so you can copy and paste!
Write a 'welcome' function that takes a parameter 'language', with a type String, and returns a greeting - if you have it in your database. It should default to English if the language is not in the database, or in the event of an invalid input."""

language_database = {
    "english": "Welcome",
    "czech": "Vitejte",
    "danish": "Velkomst",
    "dutch": "Welkom",
    "estonian": "Tere tulemast",
    "finnish": "Tervetuloa",
    "flemish": "Welgekomen",
    "french": "Bienvenue",
    "german": "Willkommen",
    "irish": "Failte",
    "italian": "Benvenuto",
    "latvian": "Gaidits",
    "lithuanian": "Laukiamas",
    "polish": "Witamy",
    "spanish": "Bienvenido",
    "swedish": "Valkommen",
    "welsh": "Croeso"
}

def greet(language):
    if language in language_database:
        return language_database[language]
    else:
        return "Welcome"


print(greet("polish"))

"""Dans l'expression if language in language_database:, Python vérifie si la variable language est présente parmi les clés du dictionnaire language_database.

Lorsque vous utilisez l'opérateur in avec un dictionnaire en Python, il vérifie uniquement la présence de la clé, pas de la valeur. Donc, si language est une clé dans le dictionnaire language_database, l'expression sera évaluée comme True, sinon elle sera évaluée comme False."""


def greet(language):
    return {
        'czech': 'Vitejte',   
        'welsh': 'Croeso'
    }.get(language, 'Welcome')
    
    
def greet(language):
    dict = {'english': 'Welcome',
            'welsh': 'Croeso'}

    if language in dict.keys():
        return (dict[language])
    else:
        return ('Welcome')