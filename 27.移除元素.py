#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        num = 0
        while num < len(nums):
            if nums[num] == val:
                nums.pop(num)
            else:
                num += 1
        return len(nums)
# @lc code=end

