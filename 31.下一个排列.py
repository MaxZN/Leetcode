#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1]>=nums[i]:
                pass
            else:
                swap_left_idx = i-1
                # find bigger one
                swap_left_val = nums[swap_left_idx]
                right_seq = sorted(nums[i:])
                for r in right_seq:
                    if r <= swap_left_val:
                        pass
                    else:
                        idx = nums[i:].index(r)
                        break
                swap_right_idx = idx + i
                nums[swap_left_idx], nums[swap_right_idx] = \
                    nums[swap_right_idx], nums[swap_left_idx]

                nums[i:] = sorted(nums[i:])
                return
        nums.sort()

# @lc code=end

