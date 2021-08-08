#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums: return -1
        return target in nums
        # left, right = 0, len(nums) - 1
        # while left <= right:
        #     mid = (left + right) / 2
        #     if nums[mid] == target:
        #         return mid
        #     if nums[mid] <= nums[right]:
        #         if target > nums[mid] and target <= nums[right]:
        #             left = mid + 1
        #         else:
        #             right = mid - 1
        #     else:
        #         if target < nums[mid] and target >= nums[left]:
        #             right = mid - 1
        #         else:
        #             left = mid + 1
        # return -1

# @lc code=end

