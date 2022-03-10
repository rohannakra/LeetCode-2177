# https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

from math import floor

def consecutive_ints(num):
    middle = floor(num/3)
    lst = [middle-1, middle, middle+1]

    return lst if sum(lst) == num else []

print(consecutive_ints(33))
print(consecutive_ints(102))
print(consecutive_ints(99))
print(consecutive_ints(3))
print(consecutive_ints(4))

# -- LeetCode Accepted Solution --

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        middle = floor(num/3)
        lst = [middle-1, middle, middle+1]

        return lst if sum(lst) == num else []
