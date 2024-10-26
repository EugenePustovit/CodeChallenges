
def quick_sort(a_list):

    def partition(a_list, begin_index, end_index):

        key_val = a_list[end_index]
        index = begin_index - 1
        for i in range(begin_index, end_index):
            if a_list[i] <= key_val:
                index += 1
                a_list[i], a_list[index] = a_list[index], a_list[i]

        index += 1
        a_list[index], a_list[end_index] = a_list[end_index], a_list[index]

        return index

    def quick_sort_rec(a_list, begin_index, end_index):
        if begin_index < end_index:
            index = partition(a_list, begin_index, end_index)
            quick_sort_rec(a_list, begin_index, index - 1)
            quick_sort_rec(a_list, index + 1, end_index)

    print(f'initial list: {a_list}')
    if a_list:
        quick_sort_rec(a_list, 0, len(a_list) - 1)

    print(f'sorted list: {a_list}')


a = [2, 8, 7, 1, 3, 5, 6, 4]
quick_sort(a)
