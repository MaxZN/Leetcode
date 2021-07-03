#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target not in nums:
            nums = sorted(nums+[target])
            return nums.index(target)
        else:
            return nums.index(target)
# @lc code=end

