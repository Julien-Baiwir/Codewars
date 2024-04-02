def better_than_average(class_points, your_points):

 average__class__points = sum(class_points) / len(class_points) 

 if average__class__points> your_points:
  return False

 else: 
  return True

class_points= [10, 14, 18]
your_points= 15
print(better_than_average(class_points, your_points))

# best practice
# def better_than_average(class_points, your_points):
#     return your_points > sum(class_points) / len(class_points)


# import statistics
# def better_than_average(class_points, your_points):
#     return your_points > statistics.mean(class_points)