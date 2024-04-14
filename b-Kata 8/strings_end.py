"""String ends with?
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false"""

def solution(text, ending):
    new_list = list(text)[len(text)-len(ending):]
    return new_list == list(ending)
    
print(solution("hello", "llo"))

def solution(string, ending):
    return string.endswith(ending)

def solution(string, ending):
    return ending in string[-len(ending):]

def solution(string, ending):
    return string[-(len(ending))::] == ending

def solution(string, ending):
    # your code here...
    return ending == string[len(string)-len(ending):]