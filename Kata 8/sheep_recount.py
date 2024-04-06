"""Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

For example,

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined"""

sheep = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

def count_sheeps(sheep):
    return sheep.count(True)

print(count_sheeps(sheep))

def count_sheeps(arrayOfSheeps):
  return arrayOfSheeps.count(True)

def count_sheeps(array_of_sheep):
  # TODO May the force be with you
  count = 0
  for sheep in array_of_sheep:
      if sheep:
          count += 1 
  return count

count_sheeps = lambda x: x.count(1)