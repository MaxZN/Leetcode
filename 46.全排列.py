#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(node,nums):
            if len(node) == len(nums):
                results.append(node[:])
            
            for i in nums:
                if i not in node:
                    node.append(i)
                    dfs(node,nums)
                    node.pop()
        root=[]
        results=[]
        dfs(root,nums)
        return results

# @lc code=end

