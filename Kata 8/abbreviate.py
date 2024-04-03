""""DESCRIPTION:
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F"""

def abbrev_name(name):
    name_parts = name.split(" ")
    return name_parts[0][0].upper() + '.' + name_parts[1][0].upper()
    
print(abbrev_name('jules baiw'))
    

def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()


def abbrevName(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]


def abbrevName(name):
    names = name.split()
    return f"{names[0][0]}.{names[1][0]}".upper()