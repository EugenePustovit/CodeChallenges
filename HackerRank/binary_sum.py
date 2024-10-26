# sum of two binary integers
int1 = [1, 0, 1, 1]
int2 = [0, 0, 1, 0]


def sum_binary(i1, i2):

    if len(i1) != len(i2):
        print(f'Length of integers does not match. Int1: {int1}, Int2: {int2}')
        return None

    buf = 0
    res = [0] * (len(int1) + 1)
    for i in range(len(i1)-1, -1, -1):

        res[i + 1] = i1[i] ^ i2[i]
        if buf == 0:
            buf = i1[i] & i2[i]
        else:
            temp = buf
            buf = res[i + 1] & temp
            res[i + 1] = res[i + 1] ^ temp

    res[0] = buf

    return res


res_bin = sum_binary(int1, int2)
print(f'Int1: {int1}')
print(f'Int2: {int2}')
print(f'Sum of binaries: {res_bin}')
