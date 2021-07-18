#
# @lc app=leetcode.cn id=453 lang=python3
#
# [453] 最小操作次数使数组元素相等
#

# @lc code=start
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        sum = 0
        minmum = min(nums)
        for i in nums:
            sum += i-minmum
        return sum
# @lc code=end

