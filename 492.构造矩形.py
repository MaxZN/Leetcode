#
# @lc app=leetcode.cn id=492 lang=python3
#
# [492] 构造矩形
#

# @lc code=start
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        two = area ** 0.5  
        one = int(two)
        for i in range(one,0,-1):
            re = area/i
            if re % 1 == 0.0:
                return int(re),i



# @lc code=end

