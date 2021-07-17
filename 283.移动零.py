#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_num = 0 
        for i in range(len(nums)):
            idx = i-zero_num
            if nums[idx] == 0:
                nums.pop(idx)
                nums.append(0)
                zero_num+=1


# @lc code=end

