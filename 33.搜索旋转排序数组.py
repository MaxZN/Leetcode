#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if target in nums: return nums.index(target)
        # return -1
        left, right = 0, len(nums)-1
        if not nums: return -1
        while left<=right:
            mid = (left+right) // 2
            
            if nums[mid] == target:
                return mid
            if nums[left]<=nums[mid]: # left inorder
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid + 1
            else:
                if nums[right] >= target > nums[mid]:
                    left = mid+1
                else:
                    right = mid - 1
        return -1

# @lc code=end

