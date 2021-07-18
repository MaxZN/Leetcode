#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        words,ans=s.split(' '),0
        for word in words:
            if word!='':ans+=1
        return ans

# @lc code=end

