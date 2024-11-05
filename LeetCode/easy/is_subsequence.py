#
# 392. Is Subsequence
#
#
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters
# without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
#
#
#
# Example 1:
#
# Input: s = "abc", t = "ahbgdc"
# Output: true
#
#
# Example 2:
#
# Input: s = "axc", t = "ahbgdc"
# Output: false
#
#
# Constraints:
#
# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.
#
#
# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109,
# and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
#


def isSubsequence(s: str, t: str) -> bool:

    if not s:
        return True

    i = 0
    n = len(s)
    for ch in t:

        if s[i] == ch:
            i += 1

        if i >= n:
            return True

    return False


    # sl = list(s)
    #
    # for ch in t:
    #
    #     if sl[0] == ch:
    #         sl.pop(0)
    #
    #     if len(sl) == 0:
    #         return True
    #
    # return False


t = "ahbgdc"
s = "abc"

print(isSubsequence(s, t))
