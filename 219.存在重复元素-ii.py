#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for idx,num in enumerate(nums):
            if num not in dic:
                dic[num] = idx
            elif idx-dic[num]<=k:
                return True
            else:
                dic[num] = idx
        return False
# @lc code=end

