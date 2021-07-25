#
# @lc app=leetcode.cn id=561 lang=python3
#
# [561] 数组拆分 I
#

# @lc code=start
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        res = 0
        for idx,num in enumerate(sorted(nums)):
            if idx%2==0:
                res+=num
        return res

# @lc code=end

