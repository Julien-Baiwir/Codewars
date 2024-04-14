"""Mumbling
This time no story, no theory. The examples below show you how to write function accum:
Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z."""

def accum(st):
    liste = list(st)
    new_liste = []
    for index, element in enumerate(liste):
        new_word = (element * (index + 1)).capitalize()  
        new_liste.append(new_word)
    return "-".join(new_liste)    
 
        
st = "rvcd"
print(accum(st))


def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

def accum(s):
    return '-'.join((a * i).title() for i, a in enumerate(s, 1))

def accum(s):
    output = ""
    for i in range(len(s)):
        output+=(s[i]*(i+1))+"-"
    return output.title()[:-1]

def accum(s):
    str = ""
    for i in range(0, len(s)):
        str += s[i].upper()
        str += s[i].lower()*i
        if i != len(s)-1:
            str += "-"
    return str

def accum(s):
    a = list(s)
    res = ""
    for i, c in enumerate(a):
        res += c * (i + 1) + "-"
    return res.strip("-").title()