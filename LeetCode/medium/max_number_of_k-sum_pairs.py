#
# 1679. Max Number of K-Sum Pairs
#
#
# You are given an integer array nums and an integer k.
#
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
#
# Return the maximum number of operations you can perform on the array.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.
#
#
# Example 2:
#
# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= k <= 109
#


import collections as c


def maxOperations(nums: list[int], k: int) -> int:

    count = c.Counter(nums)
    pairs = 0
    for num in count.keys():

        num2 = k - num
        if num == num2 and count[num] >= 2:
            pairs += count[num] // 2
            count[num] -= count[num] % 2
        elif num != num2 and count[num] and count[num2]:
            pair = min(count[num], count[num2])
            pairs += pair
            count[num] -= pair
            count[num2] -= pair

    return pairs


nums = [2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2]
k = 3

print(maxOperations(nums, k))
