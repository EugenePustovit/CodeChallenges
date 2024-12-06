### Disney

# Print the count of two the most repeated characters in a given string.
# "Hello world" => “l” (3 times), “o” (2 times) so the result => [3, 2]

def the_most_repetition(s: str) -> list[int]:
    d = {}

    for ch in s:
        if d.get(ch):
            d[ch] += 1
        else:
            d[ch] = 1

    max1 = 0
    max2 = 0
    for rep in d.values():
        if max1 < rep:
            max2 = max1
            max1 = rep
        elif max2 < rep:
            max2 = rep

    return [max1, max2]


# s = "Hello world"
s = 'qwerty'

print(the_most_repetition(s))
