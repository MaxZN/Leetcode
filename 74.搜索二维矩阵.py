#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 更加规范的二分法
        row, col = len(matrix), len(matrix[0])
        # 记录找到的位置
        x, y = 0, 0 
        # 查找列
        up, down = 0, row-1
        while up <= down:
            mid = (up + down) // 2
            if target <= matrix[mid][col-1]:
                x = mid
                down = mid - 1
            else:
                up = mid + 1
        
        # 查找行
        left, right = 0, col-1
        while left <= right:
            mid = (left + right) // 2
            if target <= matrix[x][mid]:
                y = mid
                right = mid - 1
            else:
                left = mid + 1
        

        return matrix[x][y] == target


# @lc code=end

