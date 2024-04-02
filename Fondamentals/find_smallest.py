"""DESCRIPTION:
Given an array of integers your solution should find the smallest integer.

For example:

Given [34, 15, 88, 2] your solution will return 2
Given [34, -345, -1, 100] your solution will return -345
You can assume, for the purpose of this kata, that the supplied array will not be empty."""

def find_smallest_int(arr):
    return min(arr)
arr =[34, 15, 88, 2]


array = [34, 15, 88, 2]  
def findSmallestInt(array):  
    array.sort()  # Triez le tableau dans l'ordre croissant
    return array[0]  # Retournez le premier élément, qui est le plus petit
smallest = findSmallestInt(array)
print("Le plus petit entier dans le tableau est :", smallest)

"""pour trier dans l'ordre décroissant, voilà un example:"""
arr = [34, 15, 88, 2]
arr.sort(reverse=True)
print(arr)  # Affiche la liste triée dans l'ordre décroissant

arr = [34, 15, 88, 2]
arr_sorted = sorted(arr, reverse=True)
print(arr_sorted)  # Affiche la liste triée dans l'ordre décroissant

def find_smallest_int(arr):
  return sorted(arr)[0]


def findSmallestInt(arr):
    smallest = []
    for i in range(0,len(arr)):
        if (arr[i] < smallest):
            smallest = arr[i]
    return smallest