#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def findcombination(ans, target, candidates):
            if not candidates:
                return []
            if sum(candidates) < target:
                return []
            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i - 1]:
                    continue
                new_ans = [candidates[i]]
                new_target = target - candidates[i]
                if new_target == 0:
                    return result.append(ans + new_ans)
                if new_target > 0:
                    new_candidates = [c for c in candidates[i + 1:] if c <= new_target]
                    findcombination(ans + new_ans, new_target, new_candidates)
        
        findcombination([], target, candidates)
        return result

# @lc code=end

