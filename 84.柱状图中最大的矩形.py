#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        # 超时
        for i in range(n):
            if i>0 and heights[i]==heights[i-1]: continue
            left_i = right_i = i
            cur_height = heights[i]
            while left_i>=0 and heights[left_i]>=cur_height:
                left_i -= 1
            while right_i<n and heights[right_i]>=cur_height:
                right_i += 1
            res = max(res, cur_height*(right_i-left_i-1))
        return res

# @lc code=end

