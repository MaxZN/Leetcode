#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        line1 = "qwertyuiop"
        line2 = "asdfghjkl"
        line3 = "zxcvbnm"

        result = []
        for word in words:
            count_1 = 0
            count_2 = 0
            count_3 = 0
            word_lower = word.lower()
            for letter in word_lower:
                if letter in line1:
                    count_1 += 1
                if letter in line2:
                    count_2 += 1
                if letter in line3:
                    count_3 += 1
            if count_1==len(word) or count_2==len(word) or count_3 == len(word):
                result.append(word)            
        return result

# @lc code=end

