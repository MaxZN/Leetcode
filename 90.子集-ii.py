#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        print(nums)
        new_subsets =[]
        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i-1]:
                new_subsets = [subset + [nums[i]] \
                    for subset in new_subsets]
            else:
                new_subsets = [subset + [nums[i]] \
                    for subset in res]
            res = new_subsets + res
        return res


# @lc code=end

