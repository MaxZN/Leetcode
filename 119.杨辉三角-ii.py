#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(1, rowIndex+1):
            # update to need list length
            res.append(1)
            print(i, res)
            for upd in range(i-1, 0, -1):
                # from back to front update
                # [1,3,3,1] -> [1,3,3,1,1]
                # -> [1, 3, 3, 1]
                res[upd] = res[upd] + res[upd-1]
            print(i, res)
        return res
# @lc code=end

