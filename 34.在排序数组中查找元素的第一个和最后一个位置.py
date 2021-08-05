#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums: return [-1,-1]
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if target==nums[mid]:
                if nums[left]==target and nums[right]==target:
                    return [left, right]
                if nums[left]!=target:
                    left += 1
                if nums[right]!=target:
                    right -= 1 
            elif target>nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
                
        return [left, right]
]# @lc code=end

