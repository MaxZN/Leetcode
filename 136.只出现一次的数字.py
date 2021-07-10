#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        res = 0
        for i in range(len(nums)):
            if i%2==0:
                res += nums[i]
            else:
                res -= nums[i]
        return res
# @lc code=end

