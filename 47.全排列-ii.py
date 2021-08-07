#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 1. 直接切片即可
        res = []
        n = len(nums)
        def helper(nums, tmp_li, length):
            # 长度为n时直接加入即可
            if length == n and tmp_li not in res:
                res.append(tmp_li)
            for i in range(len(nums)):
                helper(nums[:i]+nums[i+1:], tmp_li+[nums[i]], length+1)
        helper(nums, [], 0)
        return res

# @lc code=end

