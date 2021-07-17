#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # for i in s:
        #     if s.count(i)==1:
        #         return s.index(i)
        # return -1
        d = {}
        length = len(s)
        for i in range(length):
            if s[i] not in d:
                d[s[i]] = i
            else:
                d[s[i]] = length + 1
        ret = min(d.values())
        return -1 if ret > length else ret

# @lc code=end

