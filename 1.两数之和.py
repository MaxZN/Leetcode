# @before-stub-for-debug-begin
from python3problem1 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        Hashable = dict()
        for id, num in enumerate(nums):
            res = target - num
            if res in Hashable:
                return [Hashable[res], id]
            else:
                Hashable[num] = id
        return []

# @lc code=end

