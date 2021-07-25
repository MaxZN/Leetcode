#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n=len(mat),len(mat[0])
        if m*n!=r*c:
            return mat
        res=[i for j in mat for i in j]    
        return [res[i:i+c] for i in range(0,len(res),c)]

# @lc code=end

