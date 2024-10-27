# You’re working with an intern that keeps coming to you with JavaScript code that won’t run because the braces, brackets, and parentheses are off. To save you both some time, you decide to write a braces/brackets/parentheses validator.

# Let’s say:

# ‘(‘, ‘{‘, ‘[‘ are called “openers.”
# ‘)’, ‘}’, ‘]’ are called “closers.”
# Write an efficient function that tells us whether or not an input string’s openers and closers are properly nested.

# Examples:

# “{ [] ( ) }” should return 1
# “{ [(] ) }” should return 0
# “{ [ }” should return 0


def parentheses_check(s):
    if not s:
        return 0

    if len(s) % 2 > 0:
        return 0

    if s[0] not in ['{', '[', '(']:
        return 0

    o_dict = {
        '{': '}',
        '[': ']',
        '(': ')'
    }

    b_list = []
    b_list.append(s[0])

    for i in range(1, len(s)):
        # print(f's: {s[i]}, stack: {b_list}')
        if not o_dict.get(b_list[-1]):
            return 0
        elif o_dict[b_list[-1]] == s[i]:
            # print('first if')
            if not b_list:
                return 0
            b_list.pop()
        # elif s[i] in o_dict.keys():
        else:
            # print('second if')
            b_list.append(s[i])

    if b_list:
        return 0

    return 1


s_list = [
    '{[({[()}])]}'
]

for s in s_list:
    print('---')
    print(parentheses_check(s))
