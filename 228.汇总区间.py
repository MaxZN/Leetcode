#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        l_str = []
        if len(nums) == 1:
            l_str.append('%d'%nums[0])
            return l_str
        l = r = nums[0]
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                r = nums[i + 1]
                if i == len(nums) - 2:
                    if r == l:
                        l_str.append('%d'%l)
                    else:
                        l_str.append('%d'%l + '->' + '%d'%r)
                    l = r = nums[i + 1]
                    
            else:
                if r == l:
                    l_str.append('%d'%l)
                else:
                    l_str.append('%d'%l + '->' + '%d'%r)
                l = r = nums[i + 1]
                if i + 1 == len(nums) - 1:
                     l_str.append('%d'%l)
        return l_str

# @lc code=end

