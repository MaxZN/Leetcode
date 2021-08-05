#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        outdic = []
        candidates.sort()

        def deep_search(remain, flag, used_dic):
            for idx in range(flag, len(candidates)):
                cur = candidates[idx]
                if cur==remain:
                    outdic.append(used_dic+[cur])
                if cur<remain:
                    deep_search(remain-cur, idx, used_dic+[cur])
                if cur>remain:
                    return
        deep_search(target, flag=0, used_dic=[])
        return outdic

# @lc code=end

