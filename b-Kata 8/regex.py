"""Regex validate PIN code

ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples (Input --> Output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false"""

def validate_pin(pin):
    return (len(pin) == 4 or len(pin) == 6) and pin.isdigit()

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

"""Cette partie de la fonction vérifie si la longueur de la chaîne pin est soit 4, soit 6. Cela se fait en utilisant l'opérateur in qui vérifie si la longueur de pin est présente dans le tuple (4, 6). Si c'est le cas, cette partie de la condition sera True."""

def validate_pin(pin):
    return len(pin) in [4, 6] and pin.isdigit()

"""Cette partie de la fonction vérifie si la longueur de la chaîne pin est soit 4, soit 6. Cela se fait en utilisant l'opérateur in qui vérifie si la longueur de pin est présente dans la liste [4, 6]."""

validate_pin = lambda pin: len(pin) in (4, 6) and pin.isdigit()