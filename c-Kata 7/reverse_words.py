"""Reverse words
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"""

text = "hello world"

def reverse_words(text):
    print(text)
   
    words = text.split()
    print(words)
   
    reversed_words = [''.join(reversed(word)) for word in words]
    print(reversed_words)
 
    reversed_text = " ".join(reversed_words)
    print(reversed_text)

print(reverse_words(text))


def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))


def reverse_words(str):
  #go for it
  newStr = []
  for i in str.split(' '):
      newStr.append(i[::-1])
  return ' '.join(newStr)


def reverse_words(str):
  return ' '.join(w[::-1] for w in str.split(' '))