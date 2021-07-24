#
# @lc app=leetcode.cn id=495 lang=python3
#
# [495] 提莫攻击
#

# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) <= 0: return 0
        if len(timeSeries) == 1: return duration
        res = duration
        last = -1
        for id,t in enumerate(timeSeries):
            if id==0:
                last = t
            else:
                res += duration if t-last>=duration else t-last
                last = t
        return res
# @lc code=end

