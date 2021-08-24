#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words_len = len(words[0])
        words_num = len(words)
        win_len = words_len * words_num
        n = len(s)

        words_dict = {}
        for w in words:
            if w not in words_dict: words_dict[w] = 1
            else: words_dict[w] += 1
        ans = []
        start = 0
        while start < n - win_len + 1:
            temp_dict = copy.deepcopy(words_dict)
            for i in range(start, start+win_len, words_len):
                temp_word = s[i: i+words_len]
                if temp_word not in temp_dict: break
                else:
                    temp_dict[temp_word] -= 1
                    if temp_dict[temp_word] < 0: break
            else:
                ans.append(start)
            start += 1
        return ans


        

# @lc code=end

