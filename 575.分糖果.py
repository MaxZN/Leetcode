#
# @lc app=leetcode.cn id=575 lang=python3
#
# [575] 分糖果
#

# @lc code=start
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        if len(set(candyType)) < len(candyType)//2:
            return len(set(candyType))
        else:
            return len(candyType)//2
# @lc code=end

