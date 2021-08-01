#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        start, max_len = 0, 1
        dp = [[False] * n for _ in range(n)]
        # m[i][i] = 1
        # m[i][i+1] = 1 + m[i][i] if s[i]==s[i+1]
        # m[i][right] = 2 + m[i+1][right-1] if m[i+1][right-1] and s[i]==s[right]

        for i in range(0, n):
            dp[i][i] = True

        for right in range(1, n):
            for left in range(right-1, -1, -1):
            # need to update dp_insdie last
            # (>>>>>>>>>>>> right >>>>>>>>>)
            #  |  f  f  f
            #  |  |  f  f
            #  |  | t+2 f
            #  | t+1 -  - 
            #  t  -  -  -
            #  t+1 must after t
            # for left in range(0, n-1):
            #     for right in range(left, n):
                length = right-left+1
                if s[left]==s[right]:
                    if length<=1:
                        pass
                    elif length==2:
                        dp[left][right] = True
                    else:
                        dp[left][right] = dp[left+1][right-1]
                # print(left, right, length, dp[left])
                if dp[left][right]:
                    if length > max_len:
                        start = left
                        max_len = length

        return s[start:start+max_len]

# @lc code=end

