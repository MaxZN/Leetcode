#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        dp=[0]*(n+1)
        dp[0] = 1
        for i in range(1,n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-1-j]
        return dp[n]

        # still too slow
        # if n <= 1:
        #     return 1
        # else:
        #     ans = 0
        #     for i in range(n):
        #         ans += self.numTrees(i) * self.numTrees(n - 1 - i)
        #     return ans

        # too slow
        # ans = 0
        # if n<=0: return 1
        # def buildtree(left, right):
        #     cnt = 0
        #     # if left>right: return 0
        #     if right-left<1: return 1
        #     for i in range(left, right+1):
        #         left_cnt = buildtree(left, i-1)
        #         right_cnt = buildtree(i+1, right)
        #         tmp_cnt = left_cnt*right_cnt
        #         # print(left, right, i, left_cnt, right_cnt)
        #         cnt += tmp_cnt
        #     return cnt
        # cnt = buildtree(1,n)
        # return cnt

        
# @lc code=end

