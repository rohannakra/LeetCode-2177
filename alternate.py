# NOTE: This is a solution which is in one line for the problem.

from math import floor

def consecutive_ints(num):
    return [floor(num/3)-1, floor(num/3), floor(num/3)+1] if num/3 == floor(num/3) else []

print(consecutive_ints(33))
print(consecutive_ints(102))
print(consecutive_ints(99))
print(consecutive_ints(3))
print(consecutive_ints(4))

# -- Accepted LeetCode Solution --

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        return [floor(num/3)-1, floor(num/3), floor(num/3)+1] if num/3 == floor(num/3) else []        

# NOTE: However, this solution is not as quick as the one in main.py because there
#       is no use of variable, so it has to compute each step again and again.
