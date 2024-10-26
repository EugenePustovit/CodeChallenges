
def sort_insertion(arr):
    for i in range(1, len(arr)):
        j = i - 1
        val = arr[i]
        while j >= 0 and val < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = val

    return arr


def sort_insertion_desc(arr):
    for i in range(1, len(arr)):
        j = i - 1
        val = arr[i]
        while j >= 0 and val > arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = val

    return arr


a = [5, 2, 4, 6, 1, 3]
b = [31, 41, 59, 26, 41, 58]

res = sort_insertion(b)
print(f'Asc: {res}')

res_desc = sort_insertion_desc(b)
print(f'Desc: {res_desc}')
