"""Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers."""

def count_sheep(n):
    if n <= 0:
        return 'number invalid'
    else:
        n_list = list(range(1, n +1))
        result_list = []
        for num in n_list:
            result_list.append(str(num) + '...sheep')
