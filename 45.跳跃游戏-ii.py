#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [i for i in range(n)]
        for i in range(n):
            update_range = i+nums[i]
            for upd in range(i, update_range+1):
                if upd<n:
                    dp[upd] = min(dp[i]+1, dp[upd])
        return dp[-1]
# @lc code=end

