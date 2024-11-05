# 605. Can Place Flowers
#
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
#
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
# and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
#
# Example 1:
#
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:
#
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
#
#
# Constraints:
#
# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length


def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    if n == 0:
        return True

    avail = 0
    count = 0
    if flowerbed[0] == 0:
        count += 1

    for flower in flowerbed:

        if flower:
            if count:
                avail += (count - 1) // 2
                if avail >= n:
                    return True

                count = 0
        else:
            count += 1

    if count and count // 2 >= n - avail:
        return True

    return False


f = [1,0,0,0,1]
n = 1

print(f)
print(n)
print(canPlaceFlowers(f, n))