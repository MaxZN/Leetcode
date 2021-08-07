#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def sort_string(strs):
            str_list = list(strs)
            str_list = sorted(str_list)
            return ''.join(str_list)
        out = []
        dic = {}
        for s in strs:
            s_sorted = sort_string(s)
            if s_sorted not in dic:
                dic[s_sorted] = [s]
            else:
                dic[s_sorted].append(s)
        print(dic)
        for li in dic:
            out.append(dic[li])
        return out

# @lc code=end

