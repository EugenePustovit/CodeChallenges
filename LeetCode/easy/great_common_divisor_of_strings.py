# 1071. Greatest Common Divisor of Strings
#
# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t(i.e., t is concatenated
# with itself one or more times).
#
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
#
# Example 1:
#
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
#
#
# Example 2:
#
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
#
#
# Example 3:
# 
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
#
# Constraints:
#
# - 1 <= str1.length, str2.length <= 1000
# - str1 and str2 consist of English uppercase letters.


def gcd(big, small):

    def gcd_r(b, s):
        if s:
            rsd = b % s
            b, s = s, rsd
            return gcd_r(b, s)
        else:
            return b

    if big < small:
        big, small = small, big

    return gcd_r(big, small)


import math


def gcdOfStrings(str1: str, str2: str) -> str:

    if str1 + str2 != str2 + str1:
        return ''

    divisor = math.gcd(len(str1), len(str2))

    return str1[:divisor]


str1 = 'TAUXXTAUXXTAUXXTAUXXTAUXX'
str2 = 'TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX'

res = gcdOfStrings(str1, str2)

print(str1)
print(str2)
print(f'Great common divisor is: {res}')

# b = 48
# s = 18
#
# # res = gcd(b, s)
# res = math.gcd(b, s)
# print(b)
# print(s)
# print(res)



