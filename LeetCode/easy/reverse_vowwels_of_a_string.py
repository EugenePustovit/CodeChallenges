# 345. Reverse Vowels of a String
#
#
# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
#
#
# Example 1:
#
# Input: s = "IceCreAm"
#
# Output: "AceCreIm"
#
# Explanation:
#
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
#
# Example 2:
#
# Input: s = "leetcode"
#
# Output: "leotcede"
#
#
# Constraints:
#
# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.


def reverseVowels(s: str) -> str:
    def is_vowel(ch: str) -> bool:

        v = {key: True for key in ['a', 'e', 'i', 'o', 'u']}

        return v.get(ch.lower())

    s_list = list(s)

    l = 0
    r = len(s) - 1
    while l < r:
        if is_vowel(s_list[l]) and is_vowel(s_list[r]):
            s_list[l], s_list[r] = s_list[r], s_list[l]
            if r - l > 2:
                l += 1
                r -= 1
            else:
                return ''.join(s_list)

        elif is_vowel(s_list[l]):
            r -= 1
        elif is_vowel(s_list[r]):
            l += 1
        elif r - l > 2:
            l += 1
            r -= 1
        else:
            return ''.join(s_list)

    return ''.join(s_list)
