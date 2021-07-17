#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # small, big = 1, num
        # while small < big:
        #     small = max(small+1, num//big)
        #     big = num // small
        # return small==big and small*big==num
        if num == 1: return True
        half = num//2
        
        while half*half > num: # 折半
            half = half//2
            
        for i in range(half, 2*half+1): # 搜索目标
            if i*i == num: return True
        return False


            
# @lc code=end

