#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ln = len(nums)
        ret = []
        if ln < 4:
            return []
        for i in range(0, ln - 3):
            num1 = nums[i]
            for j in range(i + 1, ln - 2):
                num2 = nums[j]
                left = j + 1
                right = ln - 1
                while left < right:
                    total = num1 + num2 + nums[left] + nums[right]
                    if total == target:
                        tmp = [num1, num2, nums[left], nums[right]]
                        if tmp not in ret:
                            ret.append(tmp)
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return ret

# @lc code=end

