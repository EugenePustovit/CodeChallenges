#
# 1456. Maximum Number of Vowels in a Substring of Given Length
#
#
# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
#
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
#
#
# Example 1:
#
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
#
#
# Example 2:
#
# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
#
#
# Example 3:
#
# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of lowercase English letters.
# 1 <= k <= s.length
#
#


def maxVowels(s: str, k: int) -> int:

    vow = {
        'a': 1,
        'e': 1,
        'i': 1,
        'o': 1,
        'u': 1,
    }

    max_v = 0
    for ch in s[:k]:
        max_v += vow.get(ch, 0)
        # if vow.get(ch):
        #     max_v += 1

    count_v = max_v
    for i in range(len(s) - k):
        count_v -= vow.get(s[i], 0)
        # if vow.get(s[i]):
        #     count_v -= 1
        count_v += vow.get(s[i+k], 0)
        # if vow.get(s[ i +k]):
        #     count_v += 1

        max_v = max(count_v, max_v)

    return max_v


s = 'leetcode'
k = 3

print(maxVowels(s, k))


