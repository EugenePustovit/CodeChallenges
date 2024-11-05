
def find_max_subarray(arr):

    print(f'List: {arr}')

    def find_max_crossing_subarray(arr, begin_index, median, end_index):

        print(f'begin index: {begin_index}, median: {median}, end index: {end_index}, arr: {arr}')

        sum_l = arr[median - 1]
        sum = arr[median - 1]
        index_l = median - 1
        for i in range(median - 2, begin_index - 1, -1):
            sum += arr[i]
            if sum > sum_l:
                sum_l = sum
                index_l = i

        sum_r = arr[median]
        sum = arr[median]
        index_r = median
        for i in range(median + 1, end_index):
            sum += arr[i]
            if sum > sum_r:
                sum_r = sum
                index_r = i

        print(f'index_l: {index_l}, index_r: {index_r}, sum: {sum_l + sum_r}')
        return index_l, index_r, sum_l + sum_r

    def find_max_subarray_rec(arr, begin_index, end_index):

        print(f'begin index: {begin_index}, end index: {end_index}')

        if end_index - begin_index <= 1:
            print(f'begin_index: {begin_index}, end_index: {end_index}, sum: {arr[begin_index]}')
            return begin_index, end_index, arr[begin_index]

        median = (begin_index + end_index) // 2
        low_left, high_left, sum_left = find_max_subarray_rec(arr, begin_index, median)
        low_right, high_right, sum_right = find_max_subarray_rec(arr, median+1, end_index)
        low_cross, high_cross, sum_cross = find_max_crossing_subarray(arr, begin_index, median, end_index)

        if sum_left >= sum_right and sum_left >= sum_cross:
            print(f'low_left: {low_left}, high_left: {high_left}, sum_left: {sum_left}')
            return low_left, high_left, sum_left

        elif sum_right >= sum_left and sum_right >= sum_cross:
            print(f'low_right: {low_right}, high_right: {high_right}, sum_right: {sum_right}')
            return low_right, high_right, sum_right

        else:
            print(f'low_cross: {low_cross}, high_cross: {high_cross}, sum_cross: {sum_cross}')
            return low_cross, high_cross, sum_cross

    arr_len = len(arr)
    index_left, index_right, max_sum = find_max_subarray_rec(arr, 0, arr_len)

    print('Max subarray:')
    print(f'index left: {index_left}')
    print(f'index right: {index_right}')
    print(f'max sum: {max_sum}')


a_list = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
find_max_subarray(a_list)
