#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        self.his = []
        if n==1:
            return True
        else:
            while n!=1:
                s = list(str(n))
                n = sum([ (int(i))**2 for i in s])
                print(n)
                if n in self.his:
                    return False
                if n < 10:
                    self.his.append(n)
            return True

# @lc code=end

