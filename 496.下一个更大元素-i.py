#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def get_bigger_idx(tgt, nums):
            if len(nums)==0:
                return -1
            for i in range(len(nums)):
                if nums[i] > tgt:
                    return nums[i]
            return -1
        idxs = []
        for n in nums1:
            idx = nums2.index(n)
            idx_ref = get_bigger_idx(n, nums2[idx+1:])
            idxs.append(idx_ref)
        return idxs
# @lc code=end

