#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续 1 的个数
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        count = 0
        for n in nums:
            if n == 1:
                count += 1
                if count > maxCount:
                    maxCount = count
            else:
                count = 0
        return maxCount

# @lc code=end

