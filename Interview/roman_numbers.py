# input: "VIII"
# output: 8

# input: "CM"
# output: 900

# XIII = 13
# XIV = 14
# IX = 9
# VIII = 8
# III = 3
# XVIII

# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# M = 1000

# XLVIII = 48

# XXV


# LXVIII = 50 + 10 + 5 + 3 = 68

# rom_num = {'I': 1,
#             'V': 5,
#             'X': 10,
#             'II': 2,
#             'III': 3,
#             'IV': 4,
#             }

#     rome_d = {'I': 1
# V = 5
# X = 10
# L = 50
# C = 100
# M = 1000}

#     rome = 'LXVIII'

#     i = 1
#     sum = 0
#     while i < len(rome):
#         if rome_d[rome[i-1]] >= rome_d[rome[i]]:
#             sum += rome_d[rome[i-1]]
#             i += 1
#         else:
#             sum += -rome_d(i-1)

# XXIV

#    X >= X # yes; sum = 10


def to_dec(roman):
    roman_d = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000}

    i = 1
    dec = 0
    while i < len(roman):
        if roman_d[roman[i - 1]] >= roman_d[roman[i]]:
            dec += roman_d[roman[i - 1]]
        else:
            dec -= roman_d[roman[i - 1]]
        i += 1

    dec += roman_d[roman[len(roman) - 1]]

    return dec


def to_rom(decimal):
    dec_d = {1: 'I',
             5: 'V',
             10: 'X',
             50: 'L',
             100: 'C',
             500: 'D',
             1000: 'M'}

    M = 1000
    D = 500
    C = 100
    L = 50
    X = 10
    V = 5
    I = 1

    roman = ''

    # # M - C, D - C
    #     m = decimal // M
    #     roman += dec_d[M]*m

    #     rest = decimal % M
    #     c = rest // (M - C)
    #     if c > 0:
    #         roman += '{}{}'.format(dec_d[C], dec_d[M])
    #         rest %= (M - C)

    #     d = rest // D
    #     roman += dec_d[D]*d

    #     rest %= D
    #     c = rest // (D - C)
    #     if c > 0:
    #         roman += '{}{}'.format(dec_d[C], dec_d[D])
    #         rest %= (D - C)

    # # C - X, L - X
    #     c = rest // C
    #     roman += dec_d[C]*c

    #     rest %= C
    #     x = rest // (C - X)
    #     if x > 0:
    #         roman += '{}{}'.format(dec_d[X], dec_d[C])
    #         rest %= (C - X)

    #     l = rest // L
    #     roman += dec_d[L]*l

    #     rest %= L
    #     x = rest // (L - X)
    #     if x > 0:
    #         roman += '{}{}'.format(dec_d[X], dec_d[L])
    #         rest %= (L - X)

    # # X - I, V - I
    #     x = rest // X
    #     roman += dec_d[X]*x

    #     rest %= X
    #     i = rest // (X - I)
    #     if i > 0:
    #         roman += '{}{}'.format(dec_d[I], dec_d[X])
    #         rest %= (X - I)

    #     v = rest // V
    #     roman += dec_d[V]*v

    #     rest %= V
    #     i = rest // (V - I)
    #     if i > 0:
    #         roman += '{}{}'.format(dec_d[I], dec_d[V])
    #         rest %= (V - I)

    # # I
    #     i = rest // I
    #     roman += dec_d[I]*i

    def parce_pair(hi, low, dec):
        roman = ''

        hi_count = dec // hi
        roman += dec_d[hi] * hi_count

        dec %= hi
        i = dec // (hi - low)
        if i > 0:
            roman += '{}{}'.format(dec_d[low], dec_d[hi])
            dec %= (hi - low)

        return roman, dec

    rom, dec = parce_pair(M, C, decimal)
    roman += rom

    rom, dec = parce_pair(D, C, dec)
    roman += rom

    rom, dec = parce_pair(C, X, dec)
    roman += rom

    rom, dec = parce_pair(L, X, dec)
    roman += rom

    rom, dec = parce_pair(X, I, dec)
    roman += rom

    rom, dec = parce_pair(V, I, dec)
    roman += rom

    i = dec // I
    roman += dec_d[I] * i

    return roman


if __name__ == '__main__':

    roman_set = ['LXVIII', 'IX', 'XIV', 'XLVIII']

    for rom_num in roman_set:
        dec = to_dec(rom_num)
        print(' {}: {} '.format(rom_num, dec))

    dec_set = [2018, 5383, 14, 7, 9, 93, 939, 959]

    for dec_num in dec_set:
        roman = to_rom(dec_num)
        print(' {}: {} '.format(dec_num, roman))
