#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            predata = dp[i-1]
            if predata >= 0:
                dp[i] = predata + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)

# @lc code=end

