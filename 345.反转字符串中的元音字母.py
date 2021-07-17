#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        dic = {'a', 'e', 'i', 'o', 'u'}
        s = list(s)
        left, right = 0, len(s)-1
        while left < right:
            if s[left].lower() not in dic:
                left += 1
                continue
            if s[right].lower() not in dic:
                right -= 1 
                continue 
            s[right], s[left] = s[left], s[right]
            left += 1
            right -= 1
        return ''.join(s)
# @lc code=end

