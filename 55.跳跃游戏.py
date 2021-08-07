#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_i = 0 
        for i,step in enumerate(nums):
            if max_i<i: return False
            max_i = max(step + i, max_i)
        return max_i >= i


# @lc code=end

