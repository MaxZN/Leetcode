#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = []
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True
# @lc code=end

