#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==0: return []
        if len(intervals)==1: return intervals
        
        ret = []
        intervals.sort()
        start,end = intervals[0]
        
        for i in intervals[1:]:
            cur_start, cur_end = i
            if cur_start>end:
                ret.append([start, end])
                start,end = i # update
            else:
                end = max(end, cur_end)
        ret.append([start, end])
        return ret


# @lc code=end

