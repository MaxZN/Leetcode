#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, N: int) -> List[List[str]]:
        checkerboard = [ "."*N for i in range(N)]
        result = []

        def check(row, col):
            for row_index in range(row):
                if "Q" == checkerboard[row_index][col]: return False
            return check_left_up(row, col) and check_right_up(row, col)
        
        def check_left_up(row, col):
            while row > 0 and col > 0:
                row -= 1
                col -= 1
                if "Q" in checkerboard[row][col]: return False
            return True
        
        def check_right_up(row, col):
            while row > 0 and col < N - 1:
                row -= 1
                col += 1
                if "Q" in checkerboard[row][col]: return False
            return True            

        def replace_char(string, char, index):
            string = list(string)
            string[index] = char
            return ''.join(string)
        
        def input(row):
            if row >= N: result.append(list(checkerboard))
            for input_col in range(N):
                if check(row, input_col):
                    checkerboard[row] = replace_char(checkerboard[row], "Q", input_col)
                    input(row + 1)
                    checkerboard[row] = replace_char(checkerboard[row], ".", input_col)
                    
        result = []
        input(0)
        return result 


# @lc code=end

