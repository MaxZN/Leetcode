#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        num = 0
        while True:
            if length <=1:
                break
            if nums[num] == nums[num + 1]:
                nums.pop(num + 1)
            else:
                num = num + 1
            length = len(nums)
            if num == length - 1:
                break

# @lc code=end

