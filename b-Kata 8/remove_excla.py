"""Remove exclamation marks
Write function RemoveExclamationMarks which removes all exclamation marks from a given string."""

def remove_exclamation_marks(s):
    return s.replace('!', '')

s = "ok!"
print(remove_exclamation_marks(s))

def remove_exclamation_marks(s):
    return ''.join([x for x in s if x != '!'])

remove_exclamation_marks=lambda s: s.replace("!","")


def remove_exclamation_marks(s):
    s_list = s.split('!')
    s = ''.join(s_list)
    return s

def remove_exclamation_marks(s):
    lst = [i for i in s if i not in '!+(?=.*\!)']
    return ''.join(lst)