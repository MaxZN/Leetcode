#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Method1: 
        '''
        intervals.append(newInterval)
        intervals.sort()
        
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
        '''
        # Method2:
        L, R = newInterval
        # 二分查找（左），参考bisect.bisect_left
        pL, r = 0, len(intervals)
        while(pL<r):
            m = (pL+r)//2
            if intervals[m][1]<L: pL = m+1
            else: r = m
        # 二分查找（右），参考bisect.bisect_right
        pR, r =  pL, len(intervals) 
        while(pR<r):
            m = (pR+r)//2
            if intervals[m][0]>R: r = m
            else: pR = m+1

        # python slice替换，待替换片段和原片段等长时，时间复杂度为O(R-L), 否则为O(N-L)
        intervals[pL:pR] = [newInterval] if pL==pR else [[min(L, intervals[pL][0]), max(R, intervals[pR-1][1])]]
        return intervals

# @lc code=end

