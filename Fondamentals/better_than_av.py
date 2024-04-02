"""How good are you really?
There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return True if you're better, else False!

Note:
Your points are not included in the array of your class's points. For calculating the average point you may add your point to the given array!"""


def better_than_average(class_points, your_points):

 average__class__points = sum(class_points) / len(class_points) 

 if average__class__points> your_points:
  return False

 else: 
  return True

class_points= [10, 14, 18]
your_points= 15
print(better_than_average(class_points, your_points))


def better_than_average(class_points, your_points):
     return your_points > sum(class_points) / len(class_points)


import statistics
def better_than_average(class_points, your_points):
     return your_points > statistics.mean(class_points)