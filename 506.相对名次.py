#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_sort = sorted(score, reverse=True)
        rank_list = ["Gold Medal", "Silver Medal",
                     "Bronze Medal"]+[str(i+4) for i in range(len(score)-3)]
        dic = dict(zip(score_sort, rank_list))
        res = [dic.get(i) for i in score]
        return res

# @lc code=end

