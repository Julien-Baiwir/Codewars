def positive_sum(arr):
    new_array = list(filter(lambda x: x >= 0, arr))
    if sum(new_array) > 0:
        return sum(new_array)
    else:
        return 0

arr = [1, -2, 3, 4, 5]
print(positive_sum(arr))

# best practice
# def positive_sum(arr):
#     return sum(x for x in arr if x > 0)