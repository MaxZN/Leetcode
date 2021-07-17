#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # if n<=0:
        #     return False
        # if n==1:
        #     return True
        # if n % 4 != 0:
        #     return False
        # return self.isPowerOfFour(n//4)
        return bin(n).count('1') == 1 and bin(n).count('0') % 2 == 1 if n > 0 else False

        
# @lc code=end

