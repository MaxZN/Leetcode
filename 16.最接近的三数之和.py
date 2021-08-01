#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ret = float('inf')
        nums.sort()
        n = len(nums)

        for i in range(n-2):
            left = i+1
            right = n-1
            while left<right:
                tmp = nums[i] + nums[left] + nums[right]
                ret = tmp if abs(tmp-target)<abs(ret-target) else ret
                if tmp == target:
                    return target
                elif tmp > target:
                    right -= 1
                else:
                    left += 1
        return ret
# @lc code=end

