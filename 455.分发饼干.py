#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g_rev = sorted(g, reverse=True)
        s_rev = sorted(s, reverse=True)
        flag_g = 0
        flag_s = 0
        account = 0
        while flag_g<len(g_rev) and flag_s<len(s_rev):
            if s_rev[flag_s] >= g_rev[flag_g]:
                flag_g += 1
                flag_s += 1
                account += 1
            else:
                flag_g += 1
        return account 
# @lc code=end

