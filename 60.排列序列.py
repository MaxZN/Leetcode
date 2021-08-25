#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 排列序列
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        allFactorial = [1, 1]
        for i in range(2, n+1):
            allFactorial.append(allFactorial[-1]*i)

        s, k, res = list(range(1, n+1)), k-1, ""
        for i in range(len(s)-1, -1, -1):
            res += str(s[k // allFactorial[i]])
            del s[k // allFactorial[i]]
            k %= allFactorial[i]
        return res

# @lc code=end

