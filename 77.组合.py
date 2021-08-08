#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        out = []
        def dfs(waiting, flags):
            if len(waiting)==k:
                out.append(waiting[:])
                return
            else:
                for i in range(flags, n+1):
                    waiting.append(i)
                    dfs(waiting, i+1)
                    waiting.pop()
        dfs([], 1)
        return out

            
# @lc code=end

