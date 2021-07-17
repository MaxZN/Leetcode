#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        need = (size+0)*(size+1)/2
        print(size,need)
        return int(need-sum(nums))
# @lc code=end

