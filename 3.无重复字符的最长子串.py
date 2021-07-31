#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        if len(s) == 1:
            return 1
        L = len(s)

        head = 0
        tail = 1
        # 设置初始窗口大小为1
        cnt = 1
        while tail<L:
            while tail<L and s[tail] not in s[head:tail]:
                tail += 1
            cnt = max(cnt, tail-head)
            if tail != L:
                # 计算头指针的移动步数
                head += s[head:tail].index(s[tail])+1
        return cnt


# @lc code=end

