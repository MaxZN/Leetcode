#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums, m, n = sorted(nums1+nums2), len(nums1), len(nums2)
        return (nums[(m+n-1)//2] + nums[(m+n)//2]) / 2

# @lc code=end

