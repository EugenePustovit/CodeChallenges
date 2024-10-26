
def sort_selection(arr):

    for i in range(len(arr)-1):
        min_i = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j
        if min_i != i:
            arr[i], arr[min_i] = arr[min_i], arr[i]

    return arr


a = [5, 2, 4, 6, 1, 3]

print(f'initial list: {a}')
res = sort_selection(a)
print(f'sorted list: {res}')
