#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            left ,right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right]  == target:
                return [left + 1, right + 1]
            if numbers[left] + numbers[right]  < target:
                left += 1
            if numbers[left] + numbers[right]  > target: 
                right -= 1

# @lc code=end

