#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums: return 1
        n = len(nums)
        for i in range(n):
            if nums[i]>=n+1 or nums[i]<=0: nums[i]=0
        for i in range(n):
            num=nums[i]
            if num==0: continue
            nums[i] = 0
            while num != nums[num-1]:
                if nums[num-1] == 0:
                    nums[num-1] = num
                else:
                    nums[num-1], num = num, nums[num-1]
        try: return 1+nums.index(0) #找到首个空位置nums[i]==0，则i+1号乘客缺席
        except: return 1+len(nums)  #满座，返回N+1


# @lc code=end

