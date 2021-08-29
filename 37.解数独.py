#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def iscorrect_block(x, y):
            numbers = []
            block_r = x // 3
            block_c = y // 3
            for i in range(block_r*3, block_r*3+3):
                for j in range(block_c*3, block_c*3+3):
                    tmp = board[i][j]
                    if tmp == '.': continue
                    elif tmp in numbers: return False
                    else: numbers.append(tmp)
            return True

        def iscorrect_row(x, y):
            numbers = []
            i = x
            for j in range(0, 9):
                tmp = board[i][j]
                if tmp == '.': continue
                elif tmp in numbers: return False
                else: numbers.append(tmp)
            return True

        def iscorrect_col(x, y):
            numbers = []
            j = y
            for i in range(0, 9):
                tmp = board[i][j]
                if tmp == '.': continue
                elif tmp in numbers: return False
                else: numbers.append(tmp)
            return True
        
        def iscorrect(x,y):
            return iscorrect_block(x,y) and iscorrect_col(x,y) and iscorrect_row(x,y)

        def get_next():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        return i, j

        def dfs(num):
            if num == 81:
                return  True
            x , y = get_next()
            for i in range(1,10):
                board[x][y] = str(i)
                if iscorrect(x,y):
                    if dfs(num+1):
                        return True
                board[x][y] = '.'
            return False
        num = 0
        for i in range(9):
                for j in range(9):
                    if board[i][j] != '.':
                        num += 1
        dfs(num)  

# @lc code=end

