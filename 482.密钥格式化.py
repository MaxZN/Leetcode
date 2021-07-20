#
# @lc app=leetcode.cn id=482 lang=python3
#
# [482] 密钥格式化
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        st = S.replace('-','').upper()
        a = len(st)
        if a == 0:
            return ''
        b = a%K
        if b == 0:
            c = (a//K) - 1
            b = K
        else:
            c = a//K
        s = st[:b]
        while c != 0:
            s += '-' + st[b:b+K]
            b = b+K
            c -= 1
        return s

# @lc code=end

