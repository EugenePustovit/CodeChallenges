#
# 283. Move Zeroes
#
#
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
#
#
#
#
# Example 1:
#
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
#
# Example 2:
#
# Input: nums = [0]
# Output: [0]
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
#
#
#
# Follow up: Could you minimize the total number of operations done?
#


def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    left = 0
    right = len(nums)

    while left < right:
        if nums[left] == 0:
            nums.pop(left)
            nums.append(0)
            right -= 1
        else:
            left += 1


    # left = 0
    # right = len(nums) - 1
    #
    # while left < right:
    #
    #     if nums[left] == 0:
    #
    #         i = left
    #         while i < right:
    #             nums[i], nums[i + 1] = nums[i + 1], nums[i]
    #             i += 1
    #
    #         right -= 1
    #
    #     else:
    #         left += 1


nums = [0, 0, 1]
moveZeroes(nums)

print(nums)
