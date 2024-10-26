
def binary_search(arr, val):

    def binary_search_rec(a, v, begin_index, end_index):
        len_a = len(a[begin_index:end_index])

        if len_a == 1:
            if a[begin_index] == v:
                return begin_index
            else:
                return None

        median = len_a // 2
        median += begin_index

        if a[median] == v:
            return median
        elif a[median] > v:
            return binary_search_rec(a, v, begin_index, median)
        else:
            return binary_search_rec(a, v, median, end_index)

    if arr[0] > val:
        return None

    if arr[-1] < val:
        return None

    return binary_search_rec(arr, val, 0, len(arr))


sort_a = [0, 2, 3, 4, 5, 6, 7]
v = 9

res_find = binary_search(sort_a, v)
print(f'Indexes for {v} in array {sort_a}: {res_find}')
