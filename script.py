""""Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value."""


def sum_array(arr):
    if arr is None or not arr or len(arr) == 1:
        return 0  
    highest = max(arr)
    lowest = min(arr)
    total_sum = sum(arr)
    result = total_sum - highest - lowest
    return result


            
def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)

def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0


def sum_array(arr):
    return 0 if arr == None else sum(sorted(arr)[1:-1])