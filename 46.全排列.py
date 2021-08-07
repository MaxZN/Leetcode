#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(wait_list,nums):
            if len(wait_list) == len(nums):
                results.append(wait_list[:])
            for n in nums:
                if n not in wait_list:
                    wait_list.append(n)
                    dfs(wait_list, nums)
                    wait_list.pop()
                else:
                    pass

        root=[]
        results=[]
        dfs(root,nums)
        return results

# @lc code=end

