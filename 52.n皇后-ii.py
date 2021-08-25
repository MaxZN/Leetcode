#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        col, pos, neg = set(), set(), set()
        def backtrack(i):
            nonlocal res
            if i == n:
                res += 1
                return
            for j in range(n):
                if j not in col and i - j not in pos and i + j not in neg:
                    col.add(j)
                    pos.add(i - j)
                    neg.add(i + j)
                    backtrack(i + 1)
                    col.remove(j)
                    pos.remove(i - j)
                    neg.remove(i + j)
        res = 0
        backtrack(0)
        return res

# @lc code=end

