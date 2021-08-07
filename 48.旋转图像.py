#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        loop = 0
        cur_w = n
        while cur_w>=1:
            print('working on loop: ',loop, cur_w)
            for i in range(cur_w-1):
                left_top  = (loop, loop+i)
                right_top = (loop+i, cur_w+loop-1)
                right_bot = (cur_w+loop-1, cur_w+loop-1-i)
                left_bot  = (cur_w+loop-1-i, loop)
                matrix[loop][loop+i], \
                    matrix[loop+i][cur_w+loop-1], \
                    matrix[cur_w+loop-1][cur_w+loop-1-i], \
                    matrix[cur_w+loop-1-i][loop] = \
                matrix[cur_w+loop-1-i][loop], \
                    matrix[loop][loop+i], \
                    matrix[loop+i][cur_w+loop-1], \
                    matrix[cur_w+loop-1][cur_w+loop-1-i]
                
                print(matrix)
            loop += 1
            cur_w = n - loop*2
            print(matrix)


# @lc code=end

