
def countTriplets(arr, r):
    # trip_count = 0
    # len_arr = len(arr)

    # if len_arr < 3:
    #     return 0

    # lib_d = collections.defaultdict(list)
    # for i in range(len_arr):
    #     lib_d[arr[i]].append(i)

    # for n in arr:
    #     val2 = n*r
    #     if lib_d[val2]:
    #         val2_count = len(lib_d[val2])
    #         val3 = val2*r
    #         if lib_d[val3]:
    #             val3_count = len(lib_d[val3])
    #             trip_count += val2_count*val3_count

    # return trip_count
    res = 0
    d = {x: [0, 0] for x in arr}
    for e in arr:
        a = e / r
        b = a / r
        if b in d:
            res += d[b][1]
        if a in d:
            d[a][1] += d[a][0]
        d[e][0] += 1
    return res

# arr = [1,2,2,4]
# r = 2
arr = [1] * 100
r = 1
res = countTriplets(arr, r)
print(res)
