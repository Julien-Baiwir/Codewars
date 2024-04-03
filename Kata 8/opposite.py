"""Very simple, given a number (integer / decimal / both depending on the language), find its opposite (additive inverse).
1: -1
14: -14
-34: 34
"""

def opposite(number):
   return - number

def opposite(number):
    return f"{number} : {-number}"


def opposite(number):
 if (type(number) is int) or (type(number) is float) or (type(number) is complex):
        number = number * -1
        return number
 else:
        try:
            number = complex(number) * -1
            return number
        except ValueError:
            print("Input data cannot be represented as a number")
            return None
        
        
opposite = lambda x: -x