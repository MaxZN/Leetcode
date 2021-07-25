#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#

# @lc code=start
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dicts={}
        for i in nums:
            if i not in dicts:
                dicts[i]=1
            else:
                dicts[i]+=1
                
        res=0
        for i in dicts:
            if i+1 in dicts:
                res=max(res,dicts[i]+dicts[i+1])
        return res

# @lc code=end

