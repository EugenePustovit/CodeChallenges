
def merge_sort(arr):

    len_arr = len(arr)
    if len_arr <= 1:
        return arr

    median = len_arr // 2
    arr_l = merge_sort(arr[:median])
    arr_r = merge_sort(arr[median:])

    res_arr = []
    index_l = 0
    index_r = 0
    while index_r < len(arr_r) and index_l < len(arr_l):
        if arr_l[index_l] <= arr_r[index_r]:
            res_arr.append(arr_l[index_l])
            index_l += 1
        else:
            res_arr.append(arr_r[index_r])
            index_r += 1

    if index_l != len(arr_l):
        res_arr.extend(arr_l[index_l:])
    else:
        res_arr.extend(arr_r[index_r:])

    return res_arr


a = [5, 2, 4, 6, 1, 3]

print(f'initial list: {a}')
res = merge_sort(a)
print(f'sorted list: {res}')
