#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        def trans(num_str):
            stack = []
            cnt = 0
            out = ''
            for s in num_str:
                if stack==[]:
                    stack.append(s)
                    cnt += 1
                elif s==stack[0]:
                    cnt += 1
                else:
                    s_in = stack.pop()
                    out += (str(cnt)+s_in)
                    stack.append(s)
                    cnt = 1
            s_in = stack.pop()
            out += (str(cnt)+s_in)
            return out

        dp = [0]*n
        dp[0] = '1'
        for i in range(1,n):
            dp[i] = trans(num_str=dp[i-1])
        return dp[n-1]
# @lc code=end

