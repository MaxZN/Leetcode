#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        out = [[] for _ in range(2**n)]
        for i in range(2**n):
            bi = bin(i)[2:][::-1]
            for idx,b in enumerate(bi):
                if b=='1': out[i].append(nums[idx])
        return out

# @lc code=end

