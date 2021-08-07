#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        M, N = len(matrix), len(matrix[0])
        row0, col0 = False, False
        for i in range(M):
            if matrix[i][0] == 0:
                col0 = True
        for j in range(N):
            if matrix[0][j] == 0:
                row0 = True
        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if row0:
            for j in range(N):
                matrix[0][j] = 0
        if col0:
            for i in range(M):
                matrix[i][0] = 0

# @lc code=end

