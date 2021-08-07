#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        if n==0: return []
        if n==1: return [[1]]

        cnt = 0
        cur_h = cur_w = 0
        # represent ->right ->bot ->left ->top
        status = [0,1,2,3]
        cur_status = 0
        while cnt!=n*n:
            while cur_status==0 and \
                0<=cur_h<n and 0<=cur_w<n:
                if matrix[cur_h][cur_w]==0:
                    cnt += 1
                    matrix[cur_h][cur_w] = cnt
                else:
                    break
                cur_w += 1
            cur_status = status[(cur_status+1)%4]
            cur_h += 1
            cur_w -= 1
            print(matrix,cur_h,cur_w)

            while cur_status==1 and \
                0<=cur_h<n and 0<=cur_w<n:
                if matrix[cur_h][cur_w]==0:
                    cnt += 1
                    matrix[cur_h][cur_w] = cnt
                else:
                    break
                cur_h += 1
            cur_status = status[(cur_status+1)%4]
            cur_w -= 1
            cur_h -= 1
            print(matrix,cur_h,cur_w)

            while cur_status==2 and \
                0<=cur_h<n and 0<=cur_w<n:
                if matrix[cur_h][cur_w]==0:
                    cnt += 1
                    matrix[cur_h][cur_w] = cnt
                else:
                    break
                cur_w -= 1 
            cur_status = status[(cur_status+1)%4]
            cur_h -= 1
            cur_w += 1 
            print(matrix,cur_h,cur_w)

            while cur_status==3 and \
                0<=cur_h<n and 0<=cur_w<n:
                if matrix[cur_h][cur_w]==0:
                    cnt += 1
                    matrix[cur_h][cur_w] = cnt
                else:
                    break
                cur_h -= 1
            cur_status = status[(cur_status+1)%4]
            cur_w += 1
            cur_h += 1
            print(matrix,cur_h,cur_w)
        return matrix
            

                

# @lc code=end

